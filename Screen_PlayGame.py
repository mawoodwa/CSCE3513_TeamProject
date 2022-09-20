import tkinter as tk
from tkinter import ttk

class Screen_PlayGame(tk.Frame):
    def __init__(self, tkRoot):
        super().__init__(tkRoot)
        self.root = tkRoot
        
        self.strDefaultFont = "Arial"
        self.intMaxTopPlayers = 3
        
        self.createScreen()
        self.gridify()
        
        
    # Size control - prevent widget from over-expanding outside grid cell
    # This should be applied to most widgets
    def propagateWidget(self, widget):
        widget.pack_propagate(False)
        widget.grid_propagate(False)
        
    def destroyMain(self):
        self.mainFrame.destroy()
        
    def hideSelf(self):
        self.mainFrame.grid_remove()
        
    def showSelf(self):
        self.mainFrame.grid()
        
    def createScreen(self):
        self.createMainFrame()
        self.createLabelScoreboard()
        self.createBGFrame()
        self.createFKeys()
        
    def gridify(self):
        intMainFrameCols = 24
        intMainFrameRows = 40
        # Position F Key - Row
        intPosFKeyRow = 35
        intFKeyRowSpan = 5
        intFKeyColSpan = 2
        
        self.mainFrame.grid(column=0,row=0,sticky="NSEW")
        #self.mainFrame.pack(side="top", fill="both", expand=True)
        for i in range(intMainFrameCols):
            self.mainFrame.columnconfigure(i,weight=1, uniform="gridUniform")
        for i in range(intMainFrameRows):
            self.mainFrame.rowconfigure(i,weight=1, uniform="gridUniform")
            
        self.labelScoreboard.grid(column=2,row=0,columnspan=20,rowspan=2,sticky="SEW")
        
        self.backgroundFrame.grid(column=2, row=2, columnspan=20, rowspan=30, padx=2,pady=2,sticky="NSEW")
        self.gridifyBG()
            
        self.frameFKey[0].grid(column=0, row=intPosFKeyRow, rowspan=intFKeyRowSpan, columnspan=intFKeyColSpan, sticky="NSEW") # F1
        self.frameFKey[1].grid(column=2, row=intPosFKeyRow, rowspan=intFKeyRowSpan, columnspan=intFKeyColSpan,sticky="NSEW") # F2
        self.frameFKey[2].grid(column=4, row=intPosFKeyRow, rowspan=intFKeyRowSpan, columnspan=intFKeyColSpan,sticky="NSEW") # F3
        self.frameFKey[3].grid(column=8, row=intPosFKeyRow, rowspan=intFKeyRowSpan, columnspan=intFKeyColSpan,sticky="NSEW") # F5
        self.frameFKey[4].grid(column=12, row=intPosFKeyRow, rowspan=intFKeyRowSpan, columnspan=intFKeyColSpan,sticky="NSEW") # F7
        self.frameFKey[5].grid(column=14, row=intPosFKeyRow, rowspan=intFKeyRowSpan, columnspan=intFKeyColSpan,sticky="NSEW") # F8
        self.frameFKey[6].grid(column=18, row=intPosFKeyRow, rowspan=intFKeyRowSpan, columnspan=intFKeyColSpan,sticky="NSEW") # F10
        self.frameFKey[7].grid(column=22, row=intPosFKeyRow, rowspan=intFKeyRowSpan, columnspan=intFKeyColSpan,sticky="NSEW") # F12
        
        self.gridifyFKeys()
        
        
    def gridifyBG(self):
        intBackgroundCols = 10
        intBackgroundRows = 10
        
        for i in range(intBackgroundCols):
            self.backgroundFrame.columnconfigure(i,weight=1, uniform="gridUniform")
        for i in range(intBackgroundRows):
            self.backgroundFrame.rowconfigure(i,weight=1, uniform="gridUniform")
            
        self.topBGinBGFrame.grid(column=0, row=0, columnspan=10, rowspan=4, padx=2, pady=2, sticky="NSEW")
        self.gridifyBGTop()
        self.midBGinBGFrame.grid(column=0, row=4, columnspan=10, rowspan=5, padx=2, pady=2, sticky="NSEW")
        self.gridifyBGMid()
        self.lowBGinBGFrame.grid(column=0, row=9, columnspan=10, rowspan=1, padx=2, pady=2, sticky="NSEW")
        self.gridifyBGLow()
    
    def gridifyBGTop(self):
        intBGTopCols = 2
        intBGTopRows = 1
    
        for i in range(intBGTopCols):
            self.topBGinBGFrame.columnconfigure(i,weight=1, uniform="gridUniform")
        for i in range(intBGTopRows):
            self.topBGinBGFrame.rowconfigure(i,weight=1, uniform="gridUniform")
            
        self.frameRedTeam.grid(column=0, row=0, padx=(10,20), sticky="NSEW")
        self.gridifyBGTopRed()
        self.frameGreenTeam.grid(column=1, row=0, padx=(20,10), sticky="NSEW")
        self.gridifyBGTopGreen()
    
    def gridifyBGTopRed(self):
        intBGRedCols = 4
        intBGRedRows = 12
    
        for i in range(intBGRedCols):
            self.frameRedTeam.columnconfigure(i,weight=1, uniform="gridUniformRed")
        for i in range(intBGRedRows):
            self.frameRedTeam.rowconfigure(i,weight=1, uniform="gridUniformRed")
            
        self.labelRedTeamHead.grid(column=0,row=0,columnspan=4,rowspan=3, sticky="NSEW")
            
        for i in range(self.intMaxTopPlayers):
            self.labelRedTopP[i].grid(column=0,row=i*2+3, rowspan=2,columnspan=3,sticky="NW")
            self.labelRedTopScore[i].grid(column=3,row=i*2+3,rowspan=2,sticky="NE")
        
        self.labelRedTeam.grid(column=0,row=10,columnspan=3,rowspan=2,sticky="SW")
        self.labelRedTeamScore.grid(column=3,row=10,rowspan=2,sticky="SE")

    
    def gridifyBGTopGreen(self):
        intBGGreenCols = 4
        intBGGreenRows = 12
    
        for i in range(intBGGreenCols):
            self.frameGreenTeam.columnconfigure(i,weight=1, uniform="gridUniformGreen")
        for i in range(intBGGreenRows):
            self.frameGreenTeam.rowconfigure(i,weight=1, uniform="gridUniformGreen")
            
        self.labelGreenTeamHead.grid(column=0,row=0,columnspan=4,rowspan=3, sticky="NSEW")
            
        for i in range(self.intMaxTopPlayers):
            self.labelGreenTopP[i].grid(column=0,row=i*2+3, rowspan=2, columnspan=3,sticky="NW")
            self.labelGreenTopScore[i].grid(column=3,row=i*2+3,rowspan=2,sticky="NE")
        
        self.labelGreenTeam.grid(column=0,row=10,columnspan=3,rowspan=2,sticky="SW")
        self.labelGreenTeamScore.grid(column=3,row=10,rowspan=2,sticky="SE")
    
    def gridifyBGMid(self):
        for i in range(1):
            self.midBGinBGFrame.columnconfigure(i,weight=1, uniform="uniformMid")
        for i in range(10):
            self.midBGinBGFrame.rowconfigure(i,weight=1, uniform="uniformMid")
            
        self.labelGameAction.grid(row=0,column=0,columnspan=4,rowspan=2,sticky="NSEW")
        
        intRecordRowspan = 1
        for i in range(self.maxGARecords):
            self.midBGFrameAction[i].grid(row=i*intRecordRowspan+2,column=0,columnspan=1,rowspan=intRecordRowspan,sticky="NEW")
            self.labelGAPlayer1[i].pack(side=tk.LEFT, padx=(10,0))
            self.labelGAHit[i].pack(side=tk.LEFT,padx=4)
            self.labelGAPlayer2[i].pack(side=tk.LEFT, padx=(0,10))
    
    def gridifyBGLow(self):
        intBGCols = 1
        intBGRows = 1
        for i in range(intBGCols):
            self.lowBGinBGFrame.columnconfigure(i,weight=1, uniform="gridUniform")
        for i in range(intBGRows):
            self.lowBGinBGFrame.rowconfigure(0,weight=1, uniform="gridUniform")
        self.labelTimeRemaining.grid(column=0, row=0, sticky="E")
    
    def gridifyFKeys(self):
        intPadX = 2
        tuplePadY = (2,0)
        
        self.labelF1.pack(padx=intPadX,pady=tuplePadY,fill="both", expand=True)
        self.labelF2.pack(padx=intPadX,pady=tuplePadY,fill="both", expand=True)
        self.labelF3.pack(padx=intPadX,pady=tuplePadY,fill="both", expand=True)
        self.labelF5.pack(padx=intPadX,pady=tuplePadY,fill="both", expand=True)
        self.labelF7.pack(padx=intPadX,pady=tuplePadY,fill="both", expand=True)
        self.labelF8.pack(padx=intPadX,pady=tuplePadY,fill="both", expand=True)
        self.labelF10.pack(padx=intPadX,pady=tuplePadY,fill="both", expand=True)
        self.labelF11.pack(padx=intPadX,pady=tuplePadY,fill="both", expand=True)
        
    def createMainFrame(self):
        strBGColor = "#000000"
    
        self.mainFrame = tk.Frame(self.root, 
            bg=strBGColor) 
        self.propagateWidget(self.mainFrame)
        
    def createLabelScoreboard(self):
        strTextColor = "#5b5bc3" # Light Blue
        strBGColor = "#000000" # Black 
        strFont = self.strDefaultFont
        intTextSize = 30
    
        self.labelScoreboard = tk.Label(self.mainFrame, 
        text="Scoreboard",
        fg=strTextColor, bg=strBGColor, font=(strFont,intTextSize))
        
    def createBGFrame(self):
        strBorderColor = "#FFFFFF"
    
        self.backgroundFrame = tk.Frame(self.mainFrame, bg=strBorderColor)
        self.propagateWidget(self.backgroundFrame)
        
        self.createTopBGInBGFrame()
        self.createMidBGInBGFrame()
        self.createLowBGInBGFrame()
        
    def createTopBGInBGFrame(self):
        strBGColor = "#000000"
    
        self.topBGinBGFrame = tk.Frame(self.backgroundFrame, bg=strBGColor)
        self.propagateWidget(self.topBGinBGFrame)
        
        self.createRedTeamBGFrame()
        self.createGreenTeamBGFrame()
        
    def createRedTeamBGFrame(self):
        strBGColor = "#000000"
        strTeamHeadColor = "#FFFFFF" # White
        strPlayerColor = "#ff6666" # Light Red
        strFont = self.strDefaultFont
        intTextsizeTeamHead = 20
        intTextsizePlayer = 18
        intTextsizeTeamScore = 20
        
        self.frameRedTeam = tk.Frame(self.topBGinBGFrame, bg=strBGColor)
        self.propagateWidget(self.frameRedTeam)
        
        self.labelRedTeamHead = tk.Label(self.frameRedTeam, 
            text="RED TEAM",
            bg=strBGColor, fg=strTeamHeadColor, font=(strFont, intTextsizeTeamHead,"bold"))
        self.propagateWidget(self.labelRedTeamHead)
        
        self.labelRedTopP = [None] * self.intMaxTopPlayers
        self.labelRedTopScore = [None] * self.intMaxTopPlayers
        for i in range(self.intMaxTopPlayers):
            self.labelRedTopP[i] = tk.Label(self.frameRedTeam, 
                text="Player "+str(i+1), 
                fg=strPlayerColor, bg=strBGColor, font=(strFont,intTextsizePlayer))
            self.labelRedTopScore[i] = tk.Label(self.frameRedTeam, 
                text=str((3-i)*1000), 
                fg=strPlayerColor, bg=strBGColor, font=(strFont,intTextsizePlayer))
            self.propagateWidget(self.labelRedTopP[i])
            self.propagateWidget(self.labelRedTopScore[i])
            
        self.labelRedTeam = tk.Label(self.frameRedTeam,
            text="TEAM SCORE", 
            fg=strPlayerColor, bg=strBGColor, font=(strFont,intTextsizeTeamScore))
        self.labelRedTeamScore = tk.Label(self.frameRedTeam,
            text="9001",
            fg=strPlayerColor, bg=strBGColor, font=(strFont,intTextsizeTeamScore))
        self.propagateWidget(self.labelRedTeam)
        self.propagateWidget(self.labelRedTeamScore)
        
    def createGreenTeamBGFrame(self):
        strBGColor = "#000000"
        strTeamHeadColor = "#FFFFFF" # White
        strPlayerColor = "#66ff66" # Light Green
        strFont = self.strDefaultFont
        intTextsizeTeamHead = 20
        intTextsizePlayer = 18
        intTextsizeTeamScore = 20
        
        
        self.frameGreenTeam = tk.Frame(self.topBGinBGFrame, bg=strBGColor)
        self.propagateWidget(self.frameGreenTeam)
           
        self.labelGreenTeamHead = tk.Label(self.frameGreenTeam, 
            text="GREEN TEAM",
            bg=strBGColor, fg=strTeamHeadColor, font=(strFont, intTextsizeTeamHead,"bold"))
        self.propagateWidget(self.labelGreenTeamHead)
        
        self.labelGreenTopP = [None] * self.intMaxTopPlayers
        self.labelGreenTopScore = [None] * self.intMaxTopPlayers
        for i in range(self.intMaxTopPlayers):
            self.labelGreenTopP[i] = tk.Label(self.frameGreenTeam, 
                text="Player "+str(i+1), 
                fg=strPlayerColor, bg=strBGColor,font=(strFont,intTextsizePlayer))
            self.labelGreenTopScore[i] = tk.Label(self.frameGreenTeam, 
                text=str((3-i)*1000), 
                fg=strPlayerColor, bg=strBGColor, font=(strFont,intTextsizePlayer))
            
            self.propagateWidget(self.labelGreenTopP[i])
            self.propagateWidget(self.labelGreenTopScore[i])

        self.labelGreenTeam = tk.Label(self.frameGreenTeam,
            text="TEAM SCORE",
            fg=strPlayerColor, bg=strBGColor, font=(self.strDefaultFont,intTextsizeTeamScore))
        self.labelGreenTeamScore = tk.Label(self.frameGreenTeam,
            text="9001",
            fg=strPlayerColor, bg=strBGColor, font=(self.strDefaultFont,intTextsizeTeamScore))
        self.propagateWidget(self.labelGreenTeam)
        self.propagateWidget(self.labelGreenTeamScore)
        
    def createMidBGInBGFrame(self):
        strBGColor = "#292f98" # Mid/Ocean Blue
        strGAColor = "#FFFFFF"
        strRedPColor = "#ff6666" # Light Red
        strGreenPColor = "#66ff66" # Light Green
        strFontGA = self.strDefaultFont
        intTextsizeGA = 20
        intTextsizePlayers = 16
        
        self.midBGinBGFrame = tk.Frame(self.backgroundFrame, bg=strBGColor)        
        self.propagateWidget(self.midBGinBGFrame)
        
        self.labelGameAction = tk.Label(self.midBGinBGFrame,
            text="Current Game Action",
            fg = strGAColor, bg = strBGColor, font=(strFontGA, intTextsizeGA))
        self.propagateWidget(self.labelGameAction)
        
        self.maxGARecords = 5
        self.midBGFrameAction = [None] * self.maxGARecords
        self.labelGAPlayer1 = [None] * self.maxGARecords
        self.labelGAHit = [None] * self.maxGARecords
        self.labelGAPlayer2 = [None] * self.maxGARecords
        for i in range(self.maxGARecords):
            self.midBGFrameAction[i] = tk.Frame(self.midBGinBGFrame, 
                bg=strBGColor)
            self.labelGAPlayer1[i] = tk.Label(self.midBGFrameAction[i],
                text="Player1",
                fg = strRedPColor, bg=strBGColor, font=(strFontGA, intTextsizePlayers))
            self.labelGAHit[i] = tk.Label(self.midBGFrameAction[i],
                text="hit",
                fg = strGAColor, bg=strBGColor, font=(strFontGA, intTextsizePlayers))
            self.labelGAPlayer2[i] = tk.Label(self.midBGFrameAction[i],
                text="Player2",
                fg = strGreenPColor, bg=strBGColor, font=(strFontGA, intTextsizePlayers))
            
    
    def createLowBGInBGFrame(self):
        strBGColor = "#000000"
        strTextColor = "#FFFFFF"
        strFont = self.strDefaultFont
        strTextsizeTime = 24
    
        self.lowBGinBGFrame = tk.Frame(self.backgroundFrame, bg=strBGColor)        
        self.propagateWidget(self.lowBGinBGFrame)
        
        self.labelTimeRemaining = tk.Label(self.lowBGinBGFrame, 
            text="Time Remaining: 0:57",
            fg=strTextColor, bg=strBGColor, font=(self.strDefaultFont, strTextsizeTime))
        self.propagateWidget(self.labelTimeRemaining)
        
        
    def createFKeys(self):
        strFKTextColor = "#36B043" # Neon Green
        strFKBGColor = "#000000" # Black
        strFKBorderColor = "#FFFFFF" # White
        strFKFontStyle = self.strDefaultFont
        intFKFontSize = 12
    
        self.frameFKey = [None] * 8
        for i in range(8):
            self.frameFKey[i] = tk.Frame(self.mainFrame,bg=strFKBorderColor)
            self.propagateWidget(self.frameFKey[i])
    
        self.labelF1 = tk.Label(self.frameFKey[0], 
            text="F1 \nEdit \nGame", 
            fg=strFKTextColor, bg=strFKBGColor, font=(strFKFontStyle,intFKFontSize))
        self.labelF2 = tk.Label(self.frameFKey[1], 
            text="F2 \nGame \nParameters", 
            fg=strFKTextColor, bg=strFKBGColor, font=(strFKFontStyle,intFKFontSize))
        self.labelF3 = tk.Label(self.frameFKey[2], 
            text="F3 \nStart \nGame", 
            fg=strFKTextColor, bg=strFKBGColor, font=(strFKFontStyle,intFKFontSize))
        self.labelF5 = tk.Label(self.frameFKey[3], 
            text="F5 \nPre-\nEntered \nGame", 
            fg=strFKTextColor, bg=strFKBGColor, font=(strFKFontStyle,intFKFontSize))
        self.labelF7 = tk.Label(self.frameFKey[4], 
            text="F7", fg=strFKTextColor, 
            bg=strFKBGColor, font=(strFKFontStyle,intFKFontSize))
        self.labelF8 = tk.Label(self.frameFKey[5], 
            text="F8 \nView \nGame", 
            fg=strFKTextColor, bg=strFKBGColor, font=(strFKFontStyle,intFKFontSize))
        self.labelF10 = tk.Label(self.frameFKey[6], 
            text="F10 \nFlick \nSync", 
            fg=strFKTextColor, bg=strFKBGColor, font=(strFKFontStyle,intFKFontSize))
        self.labelF11 = tk.Label(self.frameFKey[7], 
            text="F11 \nClear \nGame", 
            fg=strFKTextColor, bg=strFKBGColor, font=(strFKFontStyle,intFKFontSize))
        
        self.propagateWidget(self.labelF1)
        self.propagateWidget(self.labelF2)
        self.propagateWidget(self.labelF3)
        self.propagateWidget(self.labelF5)
        self.propagateWidget(self.labelF7)
        self.propagateWidget(self.labelF8)
        self.propagateWidget(self.labelF10)
        self.propagateWidget(self.labelF11)