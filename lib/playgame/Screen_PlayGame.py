import time
import tkinter as tk
from tkinter import ttk
from lib.AppObject import *
from lib.Frame_FKeys import *
from lib.playgame.Frame_GameBoard import *
from lib.playgame.Frame_WaitUntilPlay import *
from lib.playgame.Menu_MoveToEditConfirm import *
from lib.playgame.TrafficGenerator import *
from lib.Network import *

class Screen_PlayGame(AppObject):
    MENU_MAIN = 0
    MENU_WAITSTART = 1
    MENU_BACKTOEDIT = 2
    def __init__(self, tkRoot):
        super().__init__(tkRoot)
        
        self.intMenu = self.MENU_MAIN
        self.methodMoveToEdit = None
        self.intIDAfter = 0
        self.floatHighScoreFlashLastTime = 0.0
        
        self.listValidRedIDs = []
        self.listValidGreenIDs = []
        
        self.network = Network()
        self.trafficGenerator = TrafficGenerator()
        self.trafficGenerator.bindBroadcastingSocket(self.network.getReceivingSocket())
        
        self.network.startThread()
        
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
        self.frameWaitUntilPlay.bindMethodAfterFinished(self.startGameTimer)
        self.propagateWidget(self.frameWaitUntilPlay)
        
    def createFKeys(self):
        self.frameFKeys = Frame_FKeys(self)
        self.frameFKeys.clearAllKeyText()
        self.frameFKeys.setKeyText(5, "F5 \nMove to \nEdit Game", 12)
        self.frameFKeys.setKeyText(4, "F4 \n(Debug)\nSimulator", 12)
        
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
        
    def updateHitEventByLastTrans(self):
        if self.network.hasNewTransmission():
            lastTransmission = self.network.getLastTransmission()
            listID = lastTransmission.split(":")
            self.updateHitEvent(int(listID[0]), int(listID[1]))
        
    def updateScreen(self):
        if self.frameGameboard.frameGameTimer.isTimerActive() and not self.frameGameboard.frameGameTimer.isTimerPaused():
            self.updateHitEventByLastTrans()
            self.frameGameboard.frameGameTimer.updateTimer()
            if abs(time.time() - self.floatHighScoreFlashLastTime) >= 0.25:
                self.flashTeamScore()
                self.floatHighScoreFlashLastTime = time.time()
            self.intIDAfter = self.root.after(1, self.updateScreen)
        elif self.frameWaitUntilPlay.isCountActive() and not self.frameWaitUntilPlay.isPaused():
            self.frameWaitUntilPlay.updateCount()
            self.intIDAfter = self.root.after(1, self.updateScreen)
            
    def updateHitEvent(self, intIDFrom, intIDTo):
        charFromColor = 'r'
        if intIDFrom in self.listOfListIntPlayerIDs[1]:
            charFromColor = 'g'
        charToColor = 'r'
        if intIDTo in self.listOfListIntPlayerIDs[1]:
            charToColor = 'g'
        if charFromColor == charToColor:
            print("Both IDs from same color! Ignoring...")
        elif self.isValidID(charFromColor, intIDFrom) == False or self.isValidID(charToColor, intIDTo) == False:
            print("updateHitEvent: Error - One or more invalid IDs given!")
            if self.isValidID(charFromColor, intIDFrom) == False:
                print("\tID: {} is invalid for given team color!".format(intIDFrom))
            if self.isValidID(charToColor, intIDTo) == False:
                print("\tID: {} is invalid for given team color!".format(intIDTo))
        else:
            strPlayerFrom = self.frameGameboard.getCodenameFromID(intIDFrom, charFromColor)
            #print("strPlayerFrom: {}".format(strPlayerFrom))
            strPlayerTo = self.frameGameboard.getCodenameFromID(intIDTo, charToColor)
            #print("strPlayerTo: {}".format(strPlayerTo))
            self.frameGameboard.frameGameAction.pushEvent(
                                        charFromColor, strPlayerFrom,
                                        charToColor, strPlayerTo)
            if intIDFrom in self.listOfListIntPlayerIDs[0]:
                self.frameGameboard.frameScoreboard.frameTeamRed.updatePlayerScore(intIDFrom,10)
            else:
                self.frameGameboard.frameScoreboard.frameTeamGreen.updatePlayerScore(intIDFrom,10)
            
    def flashTeamScore(self):
        charHighestTeam = self.frameGameboard.frameScoreboard.getListHighestTeamScore()[0]
        self.frameGameboard.frameScoreboard.flashTeamScore(charHighestTeam)
    
    def getGeneratedIDList(self):
        listIntID = [[None]*15 for i in range(2)]
        for i in range(0,15):
            listIntID[0][i]=i
            listIntID[1][i]=i+15
        return listIntID
        
    def setPlayersUsingList(self, listPlayers, listIDs):
        listIntID = self.getGeneratedIDList()
        print(listPlayers)
        print(listIntID)
        print(listIDs)
        self.frameGameboard.setPlayersUsingList(listPlayers, listIDs)
        self.listOfListIntPlayerIDs = self.frameGameboard.getValidListIntID()
        print(self.listOfListIntPlayerIDs)
        self.trafficGenerator.setIDList(self.listOfListIntPlayerIDs[0], 
                                        self.listOfListIntPlayerIDs[1])
        
    def setValidIDsFromScoreboard(self):
        self.listValidRedIDs = self.frameGameboard.frameScoreboard.getValidIDList_RedTeam()
        self.listValidGreenIDs = self.frameGameboard.frameScoreboard.getValidIDList_GreenTeam()
        
    def isValidID(self, charTeam, intID):
        if charTeam.upper() == "R":
            return (intID in self.listValidRedIDs)
        elif charTeam.upper() == "G":
            return (intID in self.listValidGreenIDs)
        else:
            return False
    
    def isTrafficGeneratorRunning(self):
        return self.trafficGenerator.isRunning()
        
    def startTrafficGenerator(self):
        self.trafficGenerator.startThread()
    
    def endTrafficGenerator(self):
        self.trafficGenerator.stopThread()
        
    def resetScoreboard(self):
        self.frameGameboard.resetScoreboard()
        
    def clearGameAction(self):
        self.frameGameboard.clearGameAction()
        
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
        
