import tkinter as tk
from tkinter import ttk
from Menu_AddPlayerName import *
from Menu_AddCodename import *
from Menu_UsePrevCodename import *
from Menu_DeleteDBConfirm import *
from Database import *

class Screen_EditGame(tk.Frame):
    PLAYERSELECT = 0
    PLAYERNAME = 1
    ASKUSEPREVCODE = 2
    PLAYERCODENAME = 3
    DELETEDBCONFIRM = 4

    def __init__(self, tkRoot):
        super().__init__(tkRoot)
        self.root = tkRoot
        
        self.database = Database()
        self.database.openConnection()
        self.strDefaultFont = "Arial"
        self.tupleArrowPos = (0,0)
        self.intMenu = self.PLAYERSELECT
        self.intPlayerEntries = 15
        self.listPlayerInfo = [0,"","",""]
        
        self.createScreen()
        self.gridify()
        self.showMainMenu()
    
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
        
    def closeDB(self):
        print("Closing DB...")
        self.database.closeDB_NoCommit()
        
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
            listStrPlayerName = self.rLabelPlayerName[self.tupleArrowPos[1]]["text"].split()
            if listStrPlayerName == [] or listStrPlayerName == None:
                listStrPlayerName = ["",""]
            return (listStrPlayerName[0], 
                listStrPlayerName[1])
                #self.rLabelCodeName[self.tupleArrowPos[1]]["text"]
        else: #Green
            listStrPlayerName = self.gLabelPlayerName[self.tupleArrowPos[1]]["text"].split()
            if listStrPlayerName == [] or listStrPlayerName == None:
                listStrPlayerName = ["",""]
            return (listStrPlayerName[0], 
                listStrPlayerName[1])
                
    def changeMenu(self, newMenu):
        print("Not implemented!")
        
    def submitYes_UsePrevCodename(self):
        self.intMenu = self.PLAYERSELECT
        self.menuUsePrevCodename.closeMenu()
        self.menuUsePrevCodename.hideSelf()
        self.addPlayer(self.listPlayerInfo[1] + " " + self.listPlayerInfo[2], self.listPlayerInfo[3])
        self.frameTeamRed.tkraise()# keep
        self.frameTeamGreen.tkraise()# keep
        self.root.update()# keep
        
    def submitNo_UsePrevCodename(self):
        self.intMenu = self.PLAYERCODENAME
        self.menuUsePrevCodename.closeMenu()
        self.menuUsePrevCodename.hideSelf()
        self.menuAddCodename.openMenu()
        self.menuAddCodename.showSelf()
        
    def openDeleteDBConfirmMenu(self):
        self.intMenu = self.DELETEDBCONFIRM
        self.menuDeleteDBConfirm.showSelf()
        self.menuDeleteDBConfirm.openMenu()
        
    def submitYes_DeleteDB(self):
        self.intMenu = self.PLAYERSELECT
        self.menuDeleteDBConfirm.closeMenu()
        self.menuDeleteDBConfirm.hideSelf()
        print("Deleting all rows in DB...")
        self.database.deleteAllRows()
        self.database.commit()
        rows = self.database.getAllRows()
        print(rows)
        self.clearAllPlayers()
        self.frameTeamRed.tkraise()# keep
        self.frameTeamGreen.tkraise()# keep
        self.root.update()# keep
        
    def submitNo_DeleteDB(self):
        self.intMenu = self.PLAYERSELECT
        self.menuDeleteDBConfirm.closeMenu()
        self.menuDeleteDBConfirm.hideSelf()
        self.frameTeamRed.tkraise()# keep
        self.frameTeamGreen.tkraise()# keep
        self.root.update()# keep
        
    def submitPlayerName(self, strFirstName, strLastName):
        self.menuAddPlayerName.closeMenu()
        self.menuAddPlayerName.hideSelf()
        self.listPlayerInfo[1] = strFirstName
        self.listPlayerInfo[2] = strLastName
        # Check DB for name
        playerRow = self.database.findPlayerByName(strFirstName,strLastName)
        if len(playerRow) < 1:
            print("Player not found")
            self.intMenu = self.PLAYERCODENAME
            self.menuAddCodename.openMenu()
            self.menuAddCodename.showSelf()
        else:
            print(playerRow[0])
            self.intMenu = self.ASKUSEPREVCODE
            self.menuUsePrevCodename.openMenu()
            self.menuUsePrevCodename.showSelf()
            self.listPlayerInfo[0] = playerRow[0][0]
            self.listPlayerInfo[3] = playerRow[0][3]
        
    def submitCodeName(self, strCodeName):
        self.listPlayerInfo[3] = strCodeName
        self.menuAddCodename.closeMenu()
        self.menuAddCodename.hideSelf()
        print(self.listPlayerInfo)
        if self.listPlayerInfo[0] == 0:
            row = self.database.getLastId()
            id = 0
            if len(row) == 0:
                id = 1
            else:
                id = row[0][0] + 1
            self.listPlayerInfo[0] = id
            if self.database.findId(id) == []:
                self.database.insertPlayer(self.listPlayerInfo)
                self.database.commit()
        else:
            id = self.listPlayerInfo[0]
            if self.database.findId(id) != []:
                self.database.updateUsingId(self.listPlayerInfo)
                self.database.commit()
        rows = self.database.getAllRows()
        print(rows)
        self.addPlayer(self.listPlayerInfo[1] + " " + self.listPlayerInfo[2],
                        self.listPlayerInfo[3])
        self.intMenu = self.PLAYERSELECT
        self.frameTeamRed.tkraise()# keep
        self.frameTeamGreen.tkraise()# keep
        self.root.update()# keep
            
    def openAddPlayerName(self):
        self.intMenu = self.PLAYERNAME# keep
        tuplePlayerAtArrow = self.getPlayerAtArrow()# keep
        self.menuAddPlayerName.openMenu(tuplePlayerAtArrow)
        self.menuAddPlayerName.showSelf()
        self.root.update()# keep
        
    def closeAddPlayerName(self):
        self.menuAddPlayerName.closeMenu()
        self.menuAddPlayerName.hideSelf()
        
    def closeInsPlayerWithoutSave(self):
        self.intMenu = self.PLAYERSELECT# keep
        self.menuAddPlayerName.closeMenu()
        self.menuAddPlayerName.hideSelf()
        self.menuAddCodename.closeMenu()
        self.menuAddCodename.hideSelf()
        self.root.update()# keep
        
    def openAddCodename(self):
        self.intMenu = self.PLAYERCODENAME # keep
        self.menuAddCodename.openMenu()
        self.root.update()# keep
        
    def closeAddCodename(self):
        self.intMenu = self.PLAYERSELECT# keep
        self.menuAddCodename.closeMenu()
        self.frameTeamRed.tkraise()# keep
        self.frameTeamGreen.tkraise()# keep
        self.root.update()# keep
        
    def showMainMenu(self):
        self.intMenu = self.PLAYERSELECT# keep
        self.frameTeamRed.tkraise()# keep
        self.frameTeamGreen.tkraise()# keep
        self.root.update()# keep
        
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
        self.listPlayerInfo = [0,"","",""]
        self.root.update()
        
    def switchToCodenameCheck(self):
        print("codenamecheck")
        
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
        
    def clearAllPlayers(self):
        for i in range(self.intPlayerEntries):
            self.gLabelPlayerName[i]["text"] = ""
            self.gLabelCodeName[i]["text"] = ""
            self.gCheckboxVar[i].set(False)
            self.gCheckboxC[i].deselect()
            self.rLabelPlayerName[i]["text"] = ""
            self.rLabelCodeName[i]["text"] = ""
            self.rCheckboxVar[i].set(False)
            self.rCheckboxC[i].deselect()
            
    def createScreen(self):
        self.createMainFrame()
        self.createPageHeader()
        self.createTeamBoxes()
        self.createLabelGMode()
        self.createFKeys()
        self.createLabelFooter()
        self.createAddPlayerMenu()
        self.createAddCodenameMenu()
        self.createUsePrevCodenameMenu()
        self.createDeleteDBConfirmMenu()
        
    def createDeleteDBConfirmMenu(self):
        self.menuDeleteDBConfirm = Menu_DeleteDBConfirm(self.mainFrame, self.submitYes_DeleteDB, self.submitNo_DeleteDB)
        self.menuDeleteDBConfirm.closeMenu()
        self.menuDeleteDBConfirm.hideSelf()
        
    def createAddPlayerMenu(self):
        self.menuAddPlayerName = Menu_AddPlayerName(self.mainFrame, self.submitPlayerName)
        self.menuAddPlayerName.closeMenu()
        self.menuAddPlayerName.hideSelf()
        
    def createAddCodenameMenu(self):
        self.menuAddCodename = Menu_AddCodename(self.mainFrame, self.submitCodeName)
        self.menuAddCodename.closeMenu()
        self.menuAddCodename.hideSelf()
        
    def createUsePrevCodenameMenu(self):
        self.menuUsePrevCodename = Menu_UsePrevCodename(self.mainFrame, self.submitYes_UsePrevCodename, self.submitNo_UsePrevCodename)
        self.menuUsePrevCodename.closeMenu()
        self.menuUsePrevCodename.hideSelf()
           
    def gridify(self):
        # If either of below are edited, all widgets will need to be repositioned
        # i.e: All calls to grid with row/column updated
        intMainFrameCols = 24
        intMainFrameRows = 42
        # Position F Key - Row
        intPosFKeyRow = 35
        intFKeyRowSpan = 5
        intFKeyColSpan = 2
        
        self.mainFrame.grid(column=0,row=0,sticky="NSEW")
        self.menuAddPlayerName.grid(column=6,row=8,columnspan=12,rowspan=20,sticky="NSEW")
        self.menuAddPlayerName.gridify()
        self.menuAddCodename.grid(column=6,row=8,columnspan=12,rowspan=20,sticky="NSEW")
        self.menuAddCodename.gridify()
        self.menuUsePrevCodename.grid(column=6,row=8,columnspan=12,rowspan=20,sticky="NSEW")
        self.menuUsePrevCodename.gridify()
        self.menuDeleteDBConfirm.grid(column=6,row=8,columnspan=12,rowspan=20,sticky="NSEW")
        self.menuDeleteDBConfirm.gridify()
        #self.mainFrame.pack(side="top", fill="both", expand=True)
        
        for i in range(intMainFrameCols):
            self.mainFrame.columnconfigure(i,weight=1, uniform="gridUniform")
        for i in range(intMainFrameRows):
            self.mainFrame.rowconfigure(i,weight=1, uniform="gridUniform")
    
        self.labelEditGame.grid(column=0,row=0,columnspan=24,rowspan=2,sticky="SEW")
        
        self.frameTeamRed.grid(column=2,row=2,columnspan=10, rowspan=31,sticky="NSEW")
        self.gridifyRedTBox()
        
        self.frameTeamGreen.grid(column=12,row=2,columnspan=10, rowspan=31,sticky="NSEW")
        self.gridifyGreenTBox()
            
        self.labelGameMode.grid(column=7,row=33,columnspan=9,rowspan=2,sticky="NSEW")
        
        self.frameFKey[0].grid(column=0, row=intPosFKeyRow, rowspan=intFKeyRowSpan, columnspan=intFKeyColSpan, sticky="NSEW") # F1
        self.frameFKey[1].grid(column=2, row=intPosFKeyRow, rowspan=intFKeyRowSpan, columnspan=intFKeyColSpan,sticky="NSEW") # F2
        self.frameFKey[2].grid(column=4, row=intPosFKeyRow, rowspan=intFKeyRowSpan, columnspan=intFKeyColSpan,sticky="NSEW") # F3
        self.frameFKey[3].grid(column=8, row=intPosFKeyRow, rowspan=intFKeyRowSpan, columnspan=intFKeyColSpan,sticky="NSEW") # F5
        self.frameFKey[4].grid(column=12, row=intPosFKeyRow, rowspan=intFKeyRowSpan, columnspan=intFKeyColSpan,sticky="NSEW") # F7
        self.frameFKey[5].grid(column=14, row=intPosFKeyRow, rowspan=intFKeyRowSpan, columnspan=intFKeyColSpan,sticky="NSEW") # F8
        self.frameFKey[6].grid(column=18, row=intPosFKeyRow, rowspan=intFKeyRowSpan, columnspan=intFKeyColSpan,sticky="NSEW") # F10
        self.frameFKey[7].grid(column=22, row=intPosFKeyRow, rowspan=intFKeyRowSpan, columnspan=intFKeyColSpan,sticky="NSEW") # F12
        self.gridifyFKeys()
        
        self.labelFooter.grid(column=0,row=40,columnspan=24,rowspan=2,sticky="NSEW")
        
    def gridifyRedTBox(self):
        intRedTFrameCols = 10
        intRedTFrameRows = 15
        
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
        intGreenTFrameRows = 15
        
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
    
        self.labelF1 = tk.Label(self.frameFKey[0], text="F1", fg=strTextColor, bg=strBGColor, font=(strFontStyle,intFontSize))
        self.labelF2 = tk.Label(self.frameFKey[1], text="F2", fg=strTextColor, bg=strBGColor, font=(strFontStyle,intFontSize))
        self.labelF3 = tk.Label(self.frameFKey[2], text="F3", fg=strTextColor, bg=strBGColor, font=(strFontStyle,intFontSize))
        self.labelF5 = tk.Label(self.frameFKey[3], text="F5 \nChange \nScreens", fg=strTextColor, bg=strBGColor, font=(strFontStyle,intFontSize))
        self.labelF7 = tk.Label(self.frameFKey[4], text="F7 \nDelete DB \nEntries", fg=strTextColor, bg=strBGColor, font=(strFontStyle,intFontSize))
        self.labelF8 = tk.Label(self.frameFKey[5], text="F8", fg=strTextColor, bg=strBGColor, font=(strFontStyle,intFontSize))
        self.labelF10 = tk.Label(self.frameFKey[6], text="F10", fg=strTextColor, bg=strBGColor, font=(strFontStyle,intFontSize))
        self.labelF11 = tk.Label(self.frameFKey[7], text="F11", fg=strTextColor, bg=strBGColor, font=(strFontStyle,intFontSize))
        
        self.propagateWidget(self.labelF1)
        self.propagateWidget(self.labelF2)
        self.propagateWidget(self.labelF3)
        self.propagateWidget(self.labelF5)
        self.propagateWidget(self.labelF7)
        self.propagateWidget(self.labelF8)
        self.propagateWidget(self.labelF10)
        self.propagateWidget(self.labelF11)

        