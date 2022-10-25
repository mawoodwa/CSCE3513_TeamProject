import tkinter as tk
from tkinter import ttk
from lib.AppObject import *
from lib.playgame.Frame_TeamScore import *

class Frame_Scoreboard(AppObject):
    def __init__(self, tkRoot):
        super().__init__(tkRoot)
        
        self.createSelf()
        
    def createSelf(self):
        strBGColor = "#000000"
    
        #self["bg"]=strBGColor
        
        self.frameTeamRed = Frame_TeamScore(self)
        self.frameTeamRed.setMaxTopPlayers(15)
        self.frameTeamRed.setTeamName("TEAM RED")
        self.frameTeamRed.setTeamColor("#ff6666")
        self.frameTeamRed.setTopTeamColor("#ff0000")
        self.frameTeamRed.createSelf()
        self.propagateWidget(self.frameTeamRed)
        self.frameTeamGreen = Frame_TeamScore(self)
        self.frameTeamGreen.setMaxTopPlayers(15)
        self.frameTeamGreen.setTeamName("TEAM GREEN")
        self.frameTeamGreen.setTeamColor("#66ff66")
        self.frameTeamGreen.setTopTeamColor("#00ff00")
        self.frameTeamGreen.createSelf()
        self.propagateWidget(self.frameTeamGreen)
        
    def gridify(self):
        intCols = 2
        intRows = 1
    
        for i in range(intCols):
            self.columnconfigure(i,weight=1, uniform="gridUniform")
        for i in range(intRows):
            self.rowconfigure(i,weight=1, uniform="gridUniform")
        
        self.frameTeamRed.grid(column=0, row=0, padx=(10,20), sticky="NSEW")
        self.frameTeamRed.gridify()
        self.frameTeamGreen.grid(column=1, row=0, padx=(20,10), sticky="NSEW")
        self.frameTeamGreen.gridify()
        
    def setPlayersUsingList(self, listPlayers):
        self.frameTeamRed.setPlayersUsingList(listPlayers[0])
        self.frameTeamGreen.setPlayersUsingList(listPlayers[1])