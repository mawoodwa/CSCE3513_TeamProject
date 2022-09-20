import tkinter as tk
from tkinter import ttk

class Screen_EditGame(tk.Frame):
    PLAYERSELECT = 0
    PLAYERINS = 1
    def __init__(self, tkRoot):
        super().__init__(tkRoot)
        self.root = tkRoot
        
        self.strDefaultFont = "Arial"
        self.tupleArrowPos = (0,0)
        self.intMenu = self.PLAYERSELECT
        self.intPlayerEntries = 19
        
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
        
    def removeArrowAtPos(self):
        # Red
        if self.tupleArrowPos[0] < 1:
            self.rLabelArrow[self.tupleArrowPos[1]]["text"] = ""
        else: #Green
            self.gLabelArrow[self.tupleArrowPos[1]]["text"] = ""
            
    def placeArrowAtPos(self):
        # Red
        if self.tupleArrowPos[0] < 1:
            self.rLabelArrow[self.tupleArrowPos[1]]["text"] = ">>"
        else: #Green
            self.gLabelArrow[self.tupleArrowPos[1]]["text"] = ">>"
        
    def moveArrow(self, offsetX, offsetY):
        newPosX = offsetX + self.tupleArrowPos[0]
        newPosY = offsetY + self.tupleArrowPos[1]
        if newPosX >= 0 and newPosX <= 1 and newPosY >= 0 and newPosY < self.intPlayerEntries:
            self.removeArrowAtPos()
            self.tupleArrowPos = (newPosX, newPosY)
            self.placeArrowAtPos()
            self.root.update()
            
    def getPlayerAtArrow(self):
        if self.tupleArrowPos[0] < 1: #Red
            return (self.rLabelPlayerName[self.tupleArrowPos[1]]["text"], 
                self.rLabelCodeName[self.tupleArrowPos[1]]["text"])
        else: #Green
            return (self.gLabelPlayerName[self.tupleArrowPos[1]]["text"], 
                self.gLabelCodeName[self.tupleArrowPos[1]]["text"])
            
            
    def openInsPlayer(self):
        self.intMenu = self.PLAYERINS
        self.frameInsP.tkraise()
        self.entryPlayerName["state"]="normal"
        tuplePlayerAtArrow = self.getPlayerAtArrow()
        self.entryPlayerName.insert(0,tuplePlayerAtArrow[0])
        self.entryPlayerName.focus_set()
        self.entryPlayerCodeName["state"]="normal"
        self.entryPlayerCodeName.insert(0,tuplePlayerAtArrow[1])
        self.buttonSubmit["state"]="normal"
        self.root.update()
        
    def closeInsPlayer(self):
        self.intMenu = self.PLAYERSELECT
        self.entryPlayerName.delete(0,tk.END)
        self.entryPlayerName["state"]="disabled"
        self.entryPlayerCodeName.delete(0,tk.END)
        self.entryPlayerCodeName["state"]="disabled"
        self.buttonSubmit["state"]="disabled"
        self.frameTeamRed.tkraise()
        self.frameTeamGreen.tkraise()
        self.root.update()
        
    def addPlayer(self, strPlayer, strCode):
        if self.tupleArrowPos[0] == 0:
            self.rLabelPlayerName[self.tupleArrowPos[1]]["text"] = strPlayer
            self.rLabelCodeName[self.tupleArrowPos[1]]["text"] = strCode
            self.rCheckboxVar[self.tupleArrowPos[1]].set(True)
            self.rCheckboxC[self.tupleArrowPos[1]].select()
        else:
            self.gLabelPlayerName[self.tupleArrowPos[1]]["text"] = strPlayer
            self.gLabelCodeName[self.tupleArrowPos[1]]["text"] = strCode
            self.gCheckboxVar[self.tupleArrowPos[1]].set(True)
            self.gCheckboxC[self.tupleArrowPos[1]].select()
        self.root.update()
        
    def deletePlayer(self, event=None):
        if self.tupleArrowPos[0] == 0:
            self.rLabelPlayerName[self.tupleArrowPos[1]]["text"] = ""
            self.rLabelCodeName[self.tupleArrowPos[1]]["text"] = ""
            self.rCheckboxVar[self.tupleArrowPos[1]].set(False)
            self.rCheckboxC[self.tupleArrowPos[1]].deselect()
        else:
            self.gLabelPlayerName[self.tupleArrowPos[1]]["text"] = ""
            self.gLabelCodeName[self.tupleArrowPos[1]]["text"] = ""
            self.gCheckboxVar[self.tupleArrowPos[1]].set(False)
            self.gCheckboxC[self.tupleArrowPos[1]].deselect()
        self.root.update()
        
    def showInsertMenuError(self,text):
        if len(self.labelInsPError["text"]) > 0:
            self.labelInsPError["text"] = self.labelInsPError["text"] + "\nError: " + text
        else:
            self.labelInsPError["text"] = "Error: " + text

    def clearInsertMenuError(self):
        self.labelInsPError["text"] = ""
        
    def addPlayerFromMenu(self,event=None):
        intMinPNameLen = 2  # Player Name
        intMaxPNameLen = 30 # Player Name
        intMinCNameLen = 2  # Code Name
        intMaxCNameLen = 30 # Code Name
    
        self.clearInsertMenuError()
        intLenPlayerName = len(self.entryPlayerName.get())
        intLenCodeName = len(self.entryPlayerCodeName.get())
        boolPlayerNameInvalid = intLenPlayerName < intMinPNameLen or intLenPlayerName > intMaxPNameLen
        boolCodeNameInvalid = intLenCodeName < intMinCNameLen or intLenCodeName > intMaxCNameLen
        if boolPlayerNameInvalid:
            self.showInsertMenuError("Player name must be between 2 - 30 characters!")
        if boolCodeNameInvalid:
            self.showInsertMenuError("Code name must be between 2 - 30 characters!")
        if not boolPlayerNameInvalid and not boolCodeNameInvalid:
            self.clearInsertMenuError()
            self.addPlayer(self.entryPlayerName.get(), self.entryPlayerCodeName.get())
            self.closeInsPlayer()
            
    def createScreen(self):
        self.createMainFrame()
        self.createPageHeader()
        self.createTeamBoxes()
        self.createLabelGMode()
        self.createFKeys()
        self.createLabelFooter()
        self.createInsPMenu()
        
    def createInsPMenu(self):
        strBorderColor = "#5b5bc3"
        strBGColor = "#000000"
        strTextcolorError = "#FF0000" # True Red
        strTextcolorMain = "#FFFFFF" # Full White
        strFont = self.strDefaultFont
        intTextsizeHead = 20
        intTextsizeError = 14
        intTextsizeMain = 16
    
        self.frameInsP = tk.Frame(self.mainFrame, bg=strBorderColor)
        self.propagateWidget(self.frameInsP)
        self.frameInsPInterior = tk.Frame(self.frameInsP, bg=strBGColor)
        self.labelInsPHead = tk.Label(self.frameInsPInterior,
            text="Insert Player",
            fg = strTextcolorMain, bg=strBGColor,font=(strFont,intTextsizeHead))
        self.labelInsPError = tk.Label(self.frameInsPInterior,
            text="",
            fg= strTextcolorError,bg=strBGColor,font=(strFont,intTextsizeError))
        self.labelPlayerName = tk.Label(self.frameInsPInterior,
            text="Player Name:",
            fg = strTextcolorMain, bg=strBGColor,font=(strFont,intTextsizeMain))
        self.entryPlayerName = tk.Entry(self.frameInsPInterior,
            state="disabled",font=(strFont,intTextsizeMain))
        self.labelPlayerCodeName = tk.Label(self.frameInsPInterior,
            text="Player Code Name:",
            fg = strTextcolorMain, bg=strBGColor,font=(strFont,intTextsizeMain))
        self.entryPlayerCodeName = tk.Entry(self.frameInsPInterior,
            state="disabled",font=(strFont,intTextsizeMain))
        self.labelHint = tk.Label(self.frameInsPInterior,
            text="Tab or click to switch between boxes\nClick submit to insert player\nPress Esc to cancel",
            fg = strTextcolorMain, bg=strBGColor, font=(strFont,intTextsizeMain))
        self.buttonSubmit = tk.Button(self.frameInsPInterior,
            text="Submit",
            command=self.addPlayerFromMenu,
            state="disabled",
            fg=strTextcolorMain, bg=strBGColor, font=(strFont, intTextsizeMain))
        self.buttonSubmit.bind("<Return>",self.addPlayerFromMenu)
        
    def gridifyInsPMenu(self):
        intBorderSize = 10
        self.frameInsPInterior.pack(side="top", fill="both", expand=True, 
            padx=intBorderSize, pady=intBorderSize)
        
        intFrameInsPCols = 12
        intFrameInsPRows = 12
        
        for i in range(intFrameInsPCols):
            self.frameInsPInterior.columnconfigure(i,weight=1,uniform="uniformIns")
        for i in range(intFrameInsPRows):
            self.frameInsPInterior.rowconfigure(i,weight=1,uniform="uniformIns")
        self.labelInsPHead.grid(column=0,row=0,columnspan=10,rowspan=2,sticky="NSEW")
        self.labelInsPError.grid(column=0,row=2,columnspan=10,rowspan=2,sticky="NEW")
        self.labelPlayerName.grid(column=0,row=4,columnspan=4,rowspan=2,sticky="SEW")
        self.entryPlayerName.grid(column=4,row=4,columnspan=6,rowspan=2,sticky="SEW")
        self.labelPlayerCodeName.grid(column=0,row=6,columnspan=4,rowspan=2,sticky="SEW")
        self.entryPlayerCodeName.grid(column=4,row=6,columnspan=6,rowspan=2,sticky="SEW")
        self.labelHint.grid(column=0,row=9,rowspan=3,columnspan=8,padx=10,sticky="NSW")
        self.buttonSubmit.grid(column=7,row=9,rowspan=2,columnspan=2,sticky="NSEW")
        self.closeInsPlayer()
           
    def gridify(self):
        # If either of below are edited, all widgets will need to be repositioned
        # i.e: All calls to grid with row/column updated
        intMainFrameCols = 24
        intMainFrameRows = 40
        # Position F Key - Row
        intPosFKeyRow = 35
        intFKeyRowSpan = 5
        intFKeyColSpan = 2
        
        self.mainFrame.grid(column=0,row=0,sticky="NSEW")
        self.frameInsP.grid(column=6,row=8,columnspan=12,rowspan=20,sticky="NSEW")
        self.gridifyInsPMenu()
        #self.mainFrame.pack(side="top", fill="both", expand=True)
        
        for i in range(intMainFrameCols):
            self.mainFrame.columnconfigure(i,weight=1, uniform="gridUniform")
        for i in range(intMainFrameRows):
            self.mainFrame.rowconfigure(i,weight=1, uniform="gridUniform")
    
        self.labelEditGame.grid(column=0,row=0,columnspan=24,rowspan=2,sticky="SEW")
        
        self.frameTeamRed.grid(column=2,row=2,columnspan=10, rowspan=32,sticky="NSEW")
        self.gridifyRedTBox()
        
        self.frameTeamGreen.grid(column=12,row=2,columnspan=10, rowspan=32,sticky="NSEW")
        self.gridifyGreenTBox()
            
        self.labelGameMode.grid(column=9,row=34,columnspan=6,sticky="NSEW")
        
        self.frameFKey[0].grid(column=0, row=intPosFKeyRow, rowspan=intFKeyRowSpan, columnspan=intFKeyColSpan, sticky="NSEW") # F1
        self.frameFKey[1].grid(column=2, row=intPosFKeyRow, rowspan=intFKeyRowSpan, columnspan=intFKeyColSpan,sticky="NSEW") # F2
        self.frameFKey[2].grid(column=4, row=intPosFKeyRow, rowspan=intFKeyRowSpan, columnspan=intFKeyColSpan,sticky="NSEW") # F3
        self.frameFKey[3].grid(column=8, row=intPosFKeyRow, rowspan=intFKeyRowSpan, columnspan=intFKeyColSpan,sticky="NSEW") # F5
        self.frameFKey[4].grid(column=12, row=intPosFKeyRow, rowspan=intFKeyRowSpan, columnspan=intFKeyColSpan,sticky="NSEW") # F7
        self.frameFKey[5].grid(column=14, row=intPosFKeyRow, rowspan=intFKeyRowSpan, columnspan=intFKeyColSpan,sticky="NSEW") # F8
        self.frameFKey[6].grid(column=18, row=intPosFKeyRow, rowspan=intFKeyRowSpan, columnspan=intFKeyColSpan,sticky="NSEW") # F10
        self.frameFKey[7].grid(column=22, row=intPosFKeyRow, rowspan=intFKeyRowSpan, columnspan=intFKeyColSpan,sticky="NSEW") # F12
        self.gridifyFKeys()
        
        self.labelFooter.grid(column=0,row=40,columnspan=24,sticky="NSEW")
        
    def gridifyRedTBox(self):
        intRedTFrameCols = 10
        intRedTFrameRows = 20
        
        for i in range(intRedTFrameCols):
            self.frameTeamRed.columnconfigure(i,weight=1,uniform="uniformRed")
        for i in range(intRedTFrameRows):
            self.frameTeamRed.rowconfigure(i,weight=1,uniform="uniformRed")
            
        self.rLabelTeamName.grid(column=1, row=0, columnspan=11)
         
        for i in range(self.intPlayerEntries):
            self.rLabelArrow[i].grid(column=0, row=i+1,sticky="E")
            self.rCheckboxC[i].grid(column=1, row=i+1)
            self.rLabelPlayerName[i].grid(column=2, row=i+1,columnspan=4,padx=2,sticky="EW")
            self.rLabelCodeName[i].grid(column=6, row=i+1,columnspan=4,padx=(2,10),sticky="EW")
            
    def gridifyGreenTBox(self):
        intGreenTFrameCols = 10
        intGreenTFrameRows = 20
        
        for i in range(intGreenTFrameCols):
            self.frameTeamGreen.columnconfigure(i,weight=1,uniform="uniformGreen")
        for i in range(intGreenTFrameRows):
            self.frameTeamGreen.rowconfigure(i,weight=1,uniform="uniformGreen")
        
        self.gLabelTeamName.grid(column=1, row=0, columnspan=11)
            
        for i in range(self.intPlayerEntries):
            self.gLabelArrow[i].grid(column=0,row=i+1,sticky="E")
            self.gCheckboxC[i].grid(column=1, row=i+1)
            self.gLabelPlayerName[i].grid(column=2, row=i+1,columnspan=4,padx=2,sticky="EW")
            self.gLabelCodeName[i].grid(column=6, row=i+1,columnspan=4,padx=(2,10),sticky="EW")
    
    # Packed inside respective Function key frames
    def gridifyFKeys(self):
        self.labelF1.pack(padx=2,pady=(2,0),fill="both", expand=True)
        self.labelF2.pack(padx=2,pady=(2,0),fill="both", expand=True)
        self.labelF3.pack(padx=2,pady=(2,0),fill="both", expand=True)
        self.labelF5.pack(padx=2,pady=(2,0),fill="both", expand=True)
        self.labelF7.pack(padx=2,pady=(2,0),fill="both", expand=True)
        self.labelF8.pack(padx=2,pady=(2,0),fill="both", expand=True)
        self.labelF10.pack(padx=2,pady=(2,0),fill="both", expand=True)
        self.labelF11.pack(padx=2,pady=(2,0),fill="both", expand=True)
        
    def createMainFrame(self):
        self.mainFrame = tk.Frame(self.root, 
            bg="#000000")
        self.propagateWidget(self.mainFrame)
            
    def createPageHeader(self):
        strTextColor = "#5b5bc3" # Light, purplish blue
        strBGColor = "#000000" # Black
        strFontStyle = self.strDefaultFont
        intFontSize = 25
        
        self.labelEditGame = tk.Label(self.mainFrame, text="Edit Current Game", fg=strTextColor, bg=strBGColor, font=(strFontStyle,intFontSize))
        self.propagateWidget(self.labelEditGame)
        
    def createTeamBoxes(self):
        strRedTeamColor = "#330000" # Dark Red
        strGreenTeamColor = "#003300" # Dark green
    
        self.frameTeamRed = tk.Frame(self.mainFrame,bg=strRedTeamColor)
        self.frameTeamGreen = tk.Frame(self.mainFrame,bg=strGreenTeamColor)
        self.propagateWidget(self.frameTeamRed)
        self.propagateWidget(self.frameTeamGreen)
        
        self.createRedTeamBox()
        self.createGreenTeamBox()
        
    def createRedTeamBox(self):
        strTeamName = "TEAM RED"
        strTeamHeadBG = "#444444" # Mid gray
        intTeamHFontSize = 14
        strTeamColor = "#330000" # Dark red
        strTextColor = "#FFFFFF" # White
        strFontStyle = self.strDefaultFont
        intArrowFontSize = 18
        intCBoxFontSize = 14
        intEntryFontSize = 12
                        
        self.rLabelTeamName = tk.Label(self.frameTeamRed, text=strTeamName, fg=strTextColor, bg=strTeamHeadBG, font=(strFontStyle,intTeamHFontSize), borderwidth=2, relief="groove")
        self.propagateWidget(self.rLabelTeamName)

        self.rLabelPlayerName = [None] * self.intPlayerEntries
        self.rLabelCodeName = [None] * self.intPlayerEntries
        self.rCheckboxC = [None] * self.intPlayerEntries
        self.rCheckboxVar = [None] * self.intPlayerEntries
        self.rLabelArrow = [None] * self.intPlayerEntries
 
        for i in range(self.intPlayerEntries):
            self.rLabelArrow[i] = tk.Label(self.frameTeamRed, text="", fg=strTextColor, bg=strTeamColor,font=(strFontStyle,intArrowFontSize))
            self.rCheckboxVar[i] = tk.BooleanVar(value=False)
            self.rCheckboxC[i] = tk.Checkbutton(self.frameTeamRed, 
                text=str(i+1),
                fg=strTextColor, bg=strTeamColor,font=(strFontStyle,intCBoxFontSize),onvalue=1,offvalue=0,state="disabled",variable=self.rCheckboxVar[i]) 
            self.rLabelPlayerName[i] = tk.Label(self.frameTeamRed, bd=2,font=(strFontStyle,intEntryFontSize), anchor="w")
            self.rLabelCodeName[i] = tk.Label(self.frameTeamRed, bd=2,font=(strFontStyle,intEntryFontSize), anchor="w")
            
            self.propagateWidget(self.rCheckboxC[i])
            self.propagateWidget(self.rLabelPlayerName[i])
            self.propagateWidget(self.rLabelCodeName[i])
            self.propagateWidget(self.rLabelArrow[i])
        self.rLabelArrow[0]["text"] = ">>"
  
    def createGreenTeamBox(self):
        strTeamName = "TEAM GREEN"
        strTeamHeadBG = "#444444" # Mid gray
        intTeamHFontSize = 14
        strTeamColor = "#003300" # Dark green
        strTextColor = "#FFFFFF" # White
        strFontStyle = self.strDefaultFont
        intArrowFontSize = 18
        intCBoxFontSize = 14
        intEntryFontSize = 12
         
        self.gLabelTeamName = tk.Label(self.frameTeamGreen, text=strTeamName, fg=strTextColor, bg=strTeamHeadBG, font=(strFontStyle,intTeamHFontSize), borderwidth=2, relief="groove")
        self.propagateWidget(self.gLabelTeamName)

        self.gLabelPlayerName = [None] * self.intPlayerEntries
        self.gLabelCodeName = [None] * self.intPlayerEntries
        self.gCheckboxC = [None] * self.intPlayerEntries
        self.gCheckboxVar = [None] * self.intPlayerEntries
        self.gLabelArrow = [None] * self.intPlayerEntries
        
        for i in range(self.intPlayerEntries):
            self.gLabelArrow[i] = tk.Label(self.frameTeamGreen, text="", fg=strTextColor, bg=strTeamColor,font=(strFontStyle,intArrowFontSize))
            self.gCheckboxVar[i] = tk.BooleanVar(value=False)
            self.gCheckboxC[i] = tk.Checkbutton(self.frameTeamGreen, text=str(i+1),fg=strTextColor, bg=strTeamColor,font=(strFontStyle,intCBoxFontSize), onvalue=1,offvalue=0, state="disabled", variable=self.gCheckboxVar[i]) 
            self.gLabelPlayerName[i] = tk.Label(self.frameTeamGreen, bd=2,font=(strFontStyle,intEntryFontSize), anchor="w")
            self.gLabelCodeName[i] = tk.Label(self.frameTeamGreen, bd=2,font=(strFontStyle,intEntryFontSize), anchor="w")
            
            self.propagateWidget(self.gCheckboxC[i])
            self.propagateWidget(self.gLabelPlayerName[i])
            self.propagateWidget(self.gLabelCodeName[i])
            self.propagateWidget(self.gLabelArrow[i])
            
        
    def createLabelGMode(self):
        strTextColor = "#FFFFFF" # White
        strBGColor = "#444444" # Mid gray
        strFontStyle = self.strDefaultFont
        strFontSize = 14
    
        self.labelGameMode = tk.Label(self.mainFrame, text="Game Mode: Standard public mode", fg=strTextColor, bg=strBGColor, font=(strFontStyle,strFontSize))
        self.propagateWidget(self.labelGameMode)

        
    def createLabelFooter(self):
        strTextColor = "#000000" # Black
        strBGColor = "#d9d9d9" # Very light gray, almost white
        strFontStyle = self.strDefaultFont
        strFontSize = 14
    
        self.labelFooter = tk.Label(self.mainFrame, 
            text="<Del> to delete player, <Ins> to Manually Insert, or edit codename", 
            fg=strTextColor, bg=strBGColor, font=(strFontStyle,strFontSize))
        self.propagateWidget(self.labelFooter)

        
    def createFKeys(self):
        strTextColor = "#36B043" # Neon Green
        strBGColor = "#000000" # Black
        strBorderColor = "#FFFFFF" # White
        strFontStyle = self.strDefaultFont
        intFontSize = 12
        
        self.frameFKey = [None] * 8
        for i in range(8):
            self.frameFKey[i] = tk.Frame(self.mainFrame,bg=strBorderColor)
            self.propagateWidget(self.frameFKey[i])
    
        self.labelF1 = tk.Label(self.frameFKey[0], text="F1 \nEdit \nGame", fg=strTextColor, bg=strBGColor, font=(strFontStyle,intFontSize))
        self.labelF2 = tk.Label(self.frameFKey[1], text="F2 \nGame \nParameters", fg=strTextColor, bg=strBGColor, font=(strFontStyle,intFontSize))
        self.labelF3 = tk.Label(self.frameFKey[2], text="F3 \nStart \nGame", fg=strTextColor, bg=strBGColor, font=(strFontStyle,intFontSize))
        self.labelF5 = tk.Label(self.frameFKey[3], text="F5 \nPre-\nEntered \nGame", fg=strTextColor, bg=strBGColor, font=(strFontStyle,intFontSize))
        self.labelF7 = tk.Label(self.frameFKey[4], text="F7", fg=strTextColor, bg=strBGColor, font=(strFontStyle,intFontSize))
        self.labelF8 = tk.Label(self.frameFKey[5], text="F8 \nView \nGame", fg=strTextColor, bg=strBGColor, font=(strFontStyle,intFontSize))
        self.labelF10 = tk.Label(self.frameFKey[6], text="F10 \nFlick \nSync", fg=strTextColor, bg=strBGColor, font=(strFontStyle,intFontSize))
        self.labelF11 = tk.Label(self.frameFKey[7], text="F11 \nClear \nGame", fg=strTextColor, bg=strBGColor, font=(strFontStyle,intFontSize))
        
        self.propagateWidget(self.labelF1)
        self.propagateWidget(self.labelF2)
        self.propagateWidget(self.labelF3)
        self.propagateWidget(self.labelF5)
        self.propagateWidget(self.labelF7)
        self.propagateWidget(self.labelF8)
        self.propagateWidget(self.labelF10)
        self.propagateWidget(self.labelF11)

        