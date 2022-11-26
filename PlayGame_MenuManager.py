import time
import tkinter as tk
from tkinter import ttk
from lib.AppObject import *
from lib.playgame.Frame_WaitUntilPlay import *
from lib.playgame.Menu_MoveToEditConfirm import *

class PlayGame_MenuManager(AppObject):
    MENU_MAIN = 0
    MENU_WAITSTART = 1
    MENU_BACKTOEDIT = 2
    def __init__(self, tkRoot):
        super().__init__(tkRoot)
        
        self.intMenu = self.MENU_MAIN
        self.methodMoveToEdit = None
        self.intIDAfter = 0
        
        self.createScreen()
        self.gridify()
        self.hideSelf()
        
    def createScreen(self):
        self["bg"] = "#000000"
        self.createWaitUntilPlay()
        self.createMenuMoveToEditConfirm()
               
    def createWaitUntilPlay(self):
        self.frameWaitUntilPlay = Frame_WaitUntilPlay(self)
        self.frameWaitUntilPlay.bindMethodAfterFinished(self.startGameTimer)
        self.propagateWidget(self.frameWaitUntilPlay)
        
    def createMenuMoveToEditConfirm(self):
        self.menuMoveToEditConfirm = Menu_MoveToEditConfirm(self, self.bindYes_MoveToEdit, self.bindNo_MoveToEdit)
        
    def gridify(self): 
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.grid(column=0,row=0,sticky="NSEW")
        for i in range(intMainFrameCols):
            self.columnconfigure(i,weight=1, uniform="gridUniform")
        for i in range(intMainFrameRows):
            self.rowconfigure(i,weight=1, uniform="gridUniform")
            
        self.menuMoveToEditConfirm.grid(column=0,row=0,sticky="NSEW")
        self.menuMoveToEditConfirm.closeSelf()
            
        self.frameWaitUntilPlay.grid(column=0,row=0,sticky="NSEW")
        self.frameWaitUntilPlay.closeSelf()
        
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
        elif self.frameGameboard.frameGameTimer.isTimerPaused():
            self.intMenu = self.MENU_MAIN
            self.frameGameboard.frameGameTimer.unpauseTimer()
            self.showSelf()
        else:
            self.intMenu = self.MENU_MAIN
        self.showSelf()
        self.updateScreen()
            
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
        if self.frameGameboard.frameGameTimer.isTimerActive() and not self.frameGameboard.frameGameTimer.isTimerPaused():
            self.frameGameboard.frameGameTimer.pauseTimer()
            strFormattedTimeRemaining = self.frameGameboard.frameGameTimer.getFormattedTimeRemaining()
            self.menuMoveToEditConfirm.setTimerPausedHead(strFormattedTimeRemaining)
        self.root.update()
        
    def startWaitTimer(self):
        self.intMenu = self.MENU_WAITSTART
        self.showSelf()
        self.frameWaitUntilPlay.showSelf()
        self.frameWaitUntilPlay.beginCount()
        self.setValidIDsFromScoreboard()
        self.updateScreen()
        
    def endWaitTimer(self):
        self.frameWaitUntilPlay.endCount()
        self.frameWaitUntilPlay.hideSelf()
        
    def startGameTimer(self):
        self.frameGameboard.frameGameTimer.startTimer()
        self.floatHighScoreFlashLastTime = time.time()
        
    def resetGameTimer(self):
        self.frameGameboard.frameGameTimer.stopTimer()
        self.frameGameboard.frameGameTimer.updateTimerStrLabel("6:00")
        self.floatHighScoreFlashLastTime = 0.0
        
    def bind_MoveToEdit(self, method):
        self.methodMoveToEdit = method
        self.menuMoveToEditConfirm.bindYes(self.methodMoveToEdit)
        
    def bindYes_MoveToEdit(self):
        self.openMoveToEditMenu()
    def bindNo_MoveToEdit(self):
        self.closeMoveToEditMenu()