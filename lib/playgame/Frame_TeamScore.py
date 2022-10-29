import tkinter as tk
from tkinter import ttk
from lib.AppObject import *

class Frame_TeamScore(AppObject):
    def __init__(self, tkRoot):
        super().__init__(tkRoot)
        self.intMaxTopPlayers = 15
        self.strTeamName = "RED TEAM"
        self.strTeamColor = "#ff6666" # Light Red
        self.strTopTeamColor = "#ff0000"
        
    def setMaxTopPlayers(self, intMax):
        self.intMaxTopPlayers = intMax
        
    def setTeamName(self, strName):
        self.strTeamName = strName
        
    def setTeamColor(self, strColor):
        self.strTeamColor = strColor
        
    def setTopTeamColor(self, strColor):
        self.strTopTeamColor = strColor
        
    def createSelf(self):
        strBGColor = "#000000"
        strTeamHeadColor = "#FFFFFF" # White
        strPlayerColor = self.strTeamColor
        strTeamName = self.strTeamName
        strFont = self.strDefaultFont
        intTextsizeTeamHead = 20
        intTextsizePlayer = 14
        intTextsizeTeamScore = 20
        
        self["bg"] = strBGColor
        # self.propagateWidget(self.frameRedTeam)
        
        self.labelTeamHead = tk.Label(self, 
            text=strTeamName,
            bg=strBGColor, fg=strTeamHeadColor, font=(strFont, intTextsizeTeamHead,"bold"))
        self.propagateWidget(self.labelTeamHead)
        
        self.labelTopPlayers = [None] * self.intMaxTopPlayers
        self.labelTopScore = [None] * self.intMaxTopPlayers
        for i in range(self.intMaxTopPlayers):
            self.labelTopPlayers[i] = tk.Label(self, 
                text="Player "+str(i+1), 
                fg=strPlayerColor, bg=strBGColor, font=(strFont,intTextsizePlayer))
            self.labelTopScore[i] = tk.Label(self, 
                text=str((self.intMaxTopPlayers-i)*1000), 
                fg=strPlayerColor, bg=strBGColor, font=(strFont,intTextsizePlayer))
            if i < 3:
                self.labelTopPlayers[i]["font"]=(strFont,intTextsizePlayer,"bold")
                self.labelTopPlayers[i]["fg"]=self.strTopTeamColor
                self.labelTopScore[i]["font"]=(strFont,intTextsizePlayer,"bold")
                self.labelTopScore[i]["fg"]=self.strTopTeamColor
            self.propagateWidget(self.labelTopPlayers[i])
            self.propagateWidget(self.labelTopScore[i])
            
        self.labelTeamScoreHead = tk.Label(self,
            text="TEAM SCORE", 
            fg=strPlayerColor, bg=strBGColor, font=(strFont,intTextsizeTeamScore))
        self.labelTeamScoreAmount = tk.Label(self,
            text="0",
            fg=strPlayerColor, bg=strBGColor, font=(strFont,intTextsizeTeamScore))
        self.propagateWidget(self.labelTeamScoreHead)
        self.propagateWidget(self.labelTeamScoreAmount)
        
    def gridify(self):
        intCols = 4
        intRows = 20
    
        for i in range(intCols):
            self.columnconfigure(i,weight=1, uniform="gridUniformTeam")
        for i in range(intRows):
            self.rowconfigure(i,weight=1, uniform="gridUniformTeam")
            
        self.labelTeamHead.grid(column=0,row=0,columnspan=4,rowspan=2, sticky="NEW")
            
        for i in range(self.intMaxTopPlayers):
            self.labelTopPlayers[i].grid(column=0,row=i+2, rowspan=1,columnspan=3,sticky="NSW")
            self.labelTopScore[i].grid(column=3,row=i+2,rowspan=1,sticky="NSE")
        
        self.labelTeamScoreHead.grid(column=0,row=18,rowspan=2,columnspan=3,sticky="SW", pady=(0,10))
        self.labelTeamScoreAmount.grid(column=3,row=18,rowspan=2,sticky="SE", pady=(0,10))
        
    def setPlayersUsingList(self, listPlayers):
        self.clearAllPlayers()
        labelPos = 0
        for i in range(len(listPlayers)):
            if listPlayers[i][0] != "" and listPlayers[i][0] != None:
                self.labelTopPlayers[labelPos]["text"] = listPlayers[i][1]
                self.labelTopScore[labelPos]["text"] = "0"
                labelPos = labelPos + 1
                
    def clearAllPlayers(self):
        for i in range(self.intMaxTopPlayers):
            self.labelTopPlayers[i]["text"] = ""
            self.labelTopScore[i]["text"] = ""