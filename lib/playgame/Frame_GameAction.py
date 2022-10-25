import tkinter as tk
from tkinter import ttk
from lib.AppObject import *

class Frame_GameAction(AppObject):
    def __init__(self, tkRoot):
        super().__init__(tkRoot)
        
        self.createSelf()
        
    def createSelf(self):
        strBGColor = "#292f98" # Mid/Ocean Blue
        strGAColor = "#FFFFFF"
        strRedPColor = "#ff6666" # Light Red
        strGreenPColor = "#66ff66" # Light Green
        strFontGA = self.strDefaultFont
        intTextsizeGA = 20
        intTextsizePlayers = 14
        
        self["bg"] = strBGColor
        
        self.labelGameAction = tk.Label(self,
            text="Current Game Action",
            fg = strGAColor, bg = strBGColor, font=(strFontGA, intTextsizeGA))
        self.propagateWidget(self.labelGameAction)
        
        self.maxGARecords = 6
        self.midBGFrameAction = [None] * self.maxGARecords
        self.labelGAPlayer1 = [None] * self.maxGARecords
        self.labelGAHit = [None] * self.maxGARecords
        self.labelGAPlayer2 = [None] * self.maxGARecords
        for i in range(self.maxGARecords):
            self.midBGFrameAction[i] = tk.Frame(self, 
                bg=strBGColor)
            self.labelGAPlayer1[i] = tk.Label(self.midBGFrameAction[i],
                text="",
                fg = strRedPColor, bg=strBGColor, font=(strFontGA, intTextsizePlayers))
            self.labelGAHit[i] = tk.Label(self.midBGFrameAction[i],
                text="",
                fg = strGAColor, bg=strBGColor, font=(strFontGA, intTextsizePlayers))
            self.labelGAPlayer2[i] = tk.Label(self.midBGFrameAction[i],
                text="",
                fg = strGreenPColor, bg=strBGColor, font=(strFontGA, intTextsizePlayers))
        
    def gridify(self):
        intCols = 1
        intRows = 8
    
        for i in range(intCols):
            self.columnconfigure(i,weight=1, uniform="uniformMid")
        for i in range(intRows):
            self.rowconfigure(i,weight=1, uniform="uniformMid")
            
        self.labelGameAction.grid(row=0,column=0,columnspan=4,rowspan=2,sticky="NSEW")
        
        intRecordRowspan = 1
        for i in range(self.maxGARecords):
            self.midBGFrameAction[i].grid(row=i*intRecordRowspan+2,column=0,columnspan=1,rowspan=intRecordRowspan)
            self.labelGAPlayer1[i].pack(side=tk.LEFT, padx=(10,0))
            self.labelGAHit[i].pack(side=tk.LEFT,padx=4)
            self.labelGAPlayer2[i].pack(side=tk.LEFT, padx=(0,10))