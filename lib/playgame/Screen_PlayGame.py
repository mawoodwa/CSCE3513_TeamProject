import tkinter as tk
from tkinter import ttk
from lib.AppObject import *
from lib.Frame_FKeys import *
from lib.playgame.Frame_GameBoard import *
from lib.playgame.Frame_WaitUntilPlay import *
from lib.playgame.Menu_MoveToEditConfirm import *

class Screen_PlayGame(AppObject):
    MENU_MAIN = 0
    MENU_WAITSTART = 1
    MENU_BACKTOEDIT = 2
    def __init__(self, tkRoot):
        super().__init__(tkRoot)
        
        self.intMenu = self.MENU_MAIN
        self.methodMoveToEdit = None
        
        self.createScreen()
        self.gridify()
        self.showSelf()
        self.hideSelf()
        
    def createScreen(self):
        self["bg"] = "#000000"
        self.createGameboardFrame()
        self.createWaitUntilPlay()
        self.createFKeys()
        self.createMenuMoveToEditConfirm()
        
    def createLabelScoreboard(self):
        strTextColor = "#5b5bc3" # Light Blue
        strBGColor = "#000000" # Black 
        strFont = self.strDefaultFont
        intTextSize = 30
    
        self.labelScoreboard = tk.Label(self, 
        text="Scoreboard",
        fg=strTextColor, bg=strBGColor, font=(strFont,intTextSize))
        
    def createGameboardFrame(self):
        self.frameGameboard = Frame_GameBoard(self)
        self.propagateWidget(self.frameGameboard)
        
    def createWaitUntilPlay(self):
        self.frameWaitUntilPlay = Frame_WaitUntilPlay(self)
        self.propagateWidget(self.frameWaitUntilPlay)
        
    def createFKeys(self):
        self.frameFKeys = Frame_FKeys(self)
        self.frameFKeys.clearAllKeyText()
        self.frameFKeys.setKeyText(5, "F5 \nMove to \nEdit Game", 12)
        
    def createMenuMoveToEditConfirm(self):
        self.menuMoveToEditConfirm = Menu_MoveToEditConfirm(self, self.bindYes_MoveToEdit, self.bindNo_MoveToEdit)
        
    def gridify(self):
        intMainFrameCols = 24
        intMainFrameRows = 40
        # Position F Key - Row
        intPosFKeyRow = 35
        intFKeyRowSpan = 5
        intFKeyColSpan = 2
        
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.grid(column=0,row=0,sticky="NSEW")
        for i in range(intMainFrameCols):
            self.columnconfigure(i,weight=1, uniform="gridUniform")
        for i in range(intMainFrameRows):
            self.rowconfigure(i,weight=1, uniform="gridUniform")
            
        self.menuMoveToEditConfirm.grid(column=6,row=8,columnspan=12,rowspan=20,sticky="NSEW")
        self.menuMoveToEditConfirm.closeSelf()
            
        self.frameWaitUntilPlay.grid(column=6,row=8,columnspan=12,rowspan=20,sticky="NSEW")
        self.frameWaitUntilPlay.hideSelf()
        
        self.frameGameboard.grid(column=2, row=1, columnspan=20, rowspan=32, padx=2,pady=2,sticky="NSEW")
        self.frameGameboard.gridify()
        
        self.frameFKeys.grid(column=0, row=intPosFKeyRow, rowspan=intFKeyRowSpan, columnspan=intMainFrameCols, sticky="NSEW")
        self.frameFKeys.gridify()
        
    def getMenuState(self):
        return self.intMenu
        
    def closeAllMenus(self):
        self.endWaitTimer()
        self.closeMoveToEditMenu()
        
    def closeMoveToEditMenu(self):
        self.menuMoveToEditConfirm.closeSelf()
        if self.frameWaitUntilPlay.isCountActive() and self.frameWaitUntilPlay.isPaused():
            self.intMenu = self.MENU_WAITSTART
            self.frameWaitUntilPlay.unpauseCount()
            self.frameWaitUntilPlay.showSelf()
        else:
            self.intMenu = self.MENU_MAIN
        self.showSelf()
            
    def openMoveToEditMenu(self):
        self.intMenu = self.MENU_BACKTOEDIT
        self.menuMoveToEditConfirm.openSelf()
        if self.frameWaitUntilPlay.isCountActive() and not self.frameWaitUntilPlay.isPaused():
            self.frameWaitUntilPlay.pauseCount()
            intTimeRemaining = self.frameWaitUntilPlay.getTimeRemaining()
            if intTimeRemaining < 0.0:
                self.menuMoveToEditConfirm.setTimerPausedHead("0:00 (BEGIN)")
            else:
                self.menuMoveToEditConfirm.setTimerPausedHead(intTimeRemaining)
        self.root.update()
        
    def setPlayersUsingList(self, listPlayers):
        self.frameGameboard.setPlayersUsingList(listPlayers)
        
    def startWaitTimer(self):
        self.intMenu = self.MENU_WAITSTART
        self.showSelf()
        self.frameWaitUntilPlay.showSelf()
        self.frameWaitUntilPlay.beginCount()
        
    def endWaitTimer(self):
        self.frameWaitUntilPlay.endCount()
        self.frameWaitUntilPlay.hideSelf()
        
    def bind_MoveToEdit(self, method):
        self.methodMoveToEdit = method
        self.menuMoveToEditConfirm.bindYes(self.methodMoveToEdit)
        
    def bindYes_MoveToEdit(self):
        self.openMoveToEditMenu()
    def bindNo_MoveToEdit(self):
        self.closeMoveToEditMenu()