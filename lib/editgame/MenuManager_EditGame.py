import tkinter as tk
from tkinter import ttk
from lib.AppObject import *
from lib.Database import *
from lib.Frame_FKeys import *
from lib.AppObject import *
from lib.editgame.Menu_AddPlayerName import *
from lib.editgame.Menu_AddCodename import *
from lib.editgame.Menu_UsePrevCodename import *
from lib.editgame.Menu_DeleteDBConfirm import *
from lib.editgame.Menu_MoveToPlayConfirm import *
from lib.editgame.Menu_ErrorNeedPlayers import *
from lib.editgame.Menu_DebugFillPlayers import *
from lib.editgame.Frame_TeamBoxes import *

class MenuManager_EditGame(AppObject):
    INDEX_PINFO_ID = 0
    INDEX_PINFO_FNAME = 1
    INDEX_PINFO_LNAME = 2
    INDEX_PINFO_CODE = 3
    PLAYERSELECT = 0
    PLAYERNAME = 1
    ASKUSEPREVCODE = 2
    PLAYERCODENAME = 3
    DELETEDBCONFIRM = 4
    MOVETOPLAYCONFIRM = 5
    ERRORNEEDPLAYERS = 6
    DEBUGFILLPLAYERS = 7
    def __init__(self, tkRoot):
        super().__init__(tkRoot)
        
        self.intMenu = self.PLAYERSELECT
        self.listPlayerInfo = [0,"","",""]
        
    def setDatabase(self, db):
        self.database = db
        
    def setTeamBoxes(self, frameTeamBoxes):
        self.frameTeamBoxes = frameTeamBoxes
        
    def createSelf(self):
        self.createAddPlayerMenu()
        self.createAddCodenameMenu()
        self.createUsePrevCodenameMenu()
        self.createDeleteDBConfirmMenu()
        self.createMoveToPlayConfirmMenu()
        self.createErrorNeedPlayersMenu()
        self.createDebugFillPlayersMenu()
         
    def createAddPlayerMenu(self):
        self.menuAddPlayerName = Menu_AddPlayerName(self, self.submitPlayerName)
        self.menuAddPlayerName.closeSelf()
        
    def createAddCodenameMenu(self):
        self.menuAddCodename = Menu_AddCodename(self, self.submitCodeName)
        self.menuAddCodename.closeSelf()
    
    def createUsePrevCodenameMenu(self):
        self.menuUsePrevCodename = Menu_UsePrevCodename(self, self.submitYes_UsePrevCodename, self.submitNo_UsePrevCodename)
        self.menuUsePrevCodename.closeSelf()
        
    def createDeleteDBConfirmMenu(self):
        self.menuDeleteDBConfirm = Menu_DeleteDBConfirm(self, self.submitYes_DeleteDB, self.submitNo_DeleteDB)
        self.menuDeleteDBConfirm.closeSelf()
        
    def createMoveToPlayConfirmMenu(self):
        self.menuMoveToPlayConfirm = Menu_MoveToPlayConfirm(self, self.submitYes_MoveToPlay, self.submitNo_MoveToPlay)
        
    def createErrorNeedPlayersMenu(self):
        self.menuErrorNeedPlayers = Menu_ErrorNeedPlayers(self, self.submitOk_NeedPlayers)
        
    def createDebugFillPlayersMenu(self):
        self.menuDebugFillPlayers = Menu_DebugFillPlayers(self, self.submitYes_FillPlayers,
                                                                self.submitNo_FillPlayers)
        
    def gridify(self):
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.menuAddPlayerName.grid(column=0,row=0,sticky="NSEW")
        self.menuAddPlayerName.gridify()
        self.menuAddCodename.grid(column=0,row=0,sticky="NSEW")
        self.menuAddCodename.gridify()
        self.menuUsePrevCodename.grid(column=0,row=0,sticky="NSEW")
        self.menuUsePrevCodename.gridify()
        self.menuDeleteDBConfirm.grid(column=0,row=0,sticky="NSEW")
        self.menuDeleteDBConfirm.gridify()
        self.menuMoveToPlayConfirm.grid(column=0,row=0,sticky="NSEW")
        self.menuMoveToPlayConfirm.gridify()
        self.menuErrorNeedPlayers.grid(column=0,row=0,sticky="NSEW")
        self.menuErrorNeedPlayers.gridify()
        self.menuDebugFillPlayers.grid(column=0,row=0,sticky="NSEW")
        self.menuDebugFillPlayers.gridify()
        
    def openDeleteDBConfirmMenu(self):
        self.intMenu = self.DELETEDBCONFIRM
        self.menuDeleteDBConfirm.openSelf()
            
    def openAddPlayerName(self):
        self.showSelf()
        self.intMenu = self.PLAYERNAME# keep
        listPlayerAtArrow = self.getPlayerAtArrow()# keep
        self.menuAddPlayerName.setPlayerName(listPlayerAtArrow[0],
                                            listPlayerAtArrow[1])
        self.menuAddPlayerName.openSelf()
        self.root.update()# keep

    def openAddCodename(self):
        self.intMenu = self.PLAYERCODENAME # keep
        self.menuAddCodename.openSelf()
        self.root.update()# keep
        
    def openMoveToPlayConfirm(self):
        self.showSelf()
        self.intMenu = self.MOVETOPLAYCONFIRM
        self.menuMoveToPlayConfirm.openSelf()
        self.root.update()
        
    def openErrorNeedPlayers(self):
        self.intMenu = self.ERRORNEEDPLAYERS
        self.menuErrorNeedPlayers.openSelf()
        self.root.update()
        
    def openDebugFillPlayers(self):
        self.intMenu = self.DEBUGFILLPLAYERS
        self.menuDebugFillPlayers.openSelf()
        self.root.update()
        
    def switchToMainMenu(self):
        self.intMenu = self.PLAYERSELECT# keep
        self.frameTeamBoxes.tkraise()
        self.root.update()# keep
         
    def closeAllMenus(self):
        self.menuAddPlayerName.closeSelf()
        self.menuAddCodename.closeSelf()
        self.menuUsePrevCodename.closeSelf()
        self.menuDeleteDBConfirm.closeSelf()
        self.menuMoveToPlayConfirm.closeSelf()
        self.menuErrorNeedPlayers.closeSelf()
        self.switchToMainMenu()
        
    def closeAddCodename(self):
        self.menuAddCodename.closeSelf()
        self.switchToMainMenu()
        
    def closeUsePrevCodename(self):
        self.menuUsePrevCodename.closeSelf()
        self.switchToMainMenu()
        
    def closeAddPlayerName(self):
        self.menuAddPlayerName.closeSelf()
        self.switchToMainMenu()
        
    def closeInsPlayerWithoutSave(self):
        self.menuAddPlayerName.closeSelf()
        self.menuAddCodename.closeSelf()
        self.switchToMainMenu()
        
    def closeDebugFillPlayers(self):
        self.menuDebugFillPlayers.closeSelf()
        self.switchToMainMenu()
        
    def getMenuState(self):
        return self.intMenu
        
    def bind_ChangeToPlay(self, mFunc):
        self.methodChangeToPlay = mFunc
        
    def submitYes_UsePrevCodename(self):
        self.menuUsePrevCodename.closeSelf()
        self.addPlayer(self.listPlayerInfo[self.INDEX_PINFO_FNAME] + " " 
                        + self.listPlayerInfo[self.INDEX_PINFO_LNAME], 
                        self.listPlayerInfo[self.INDEX_PINFO_CODE])
        self.switchToMainMenu()
        
    def submitNo_UsePrevCodename(self):
        self.intMenu = self.PLAYERCODENAME
        self.menuUsePrevCodename.closeSelf()
        self.menuAddCodename.openSelf()

    def submitYes_DeleteDB(self):
        self.menuDeleteDBConfirm.closeSelf()
        print("Deleting all rows in DB...")
        self.database.deleteAllRows()
        self.database.commit()
        rows = self.database.getAllRows()
        print(rows)
        self.clearAllPlayers()
        self.switchToMainMenu()
        
    def submitNo_DeleteDB(self):
        self.menuDeleteDBConfirm.closeSelf()
        self.switchToMainMenu()
        
    def submitYes_MoveToPlay(self):
        listPlayerCount = self.frameTeamBoxes.getPlayerCount()
        if listPlayerCount[0] >= 1 and listPlayerCount[1] >= 1:
            self.intMenu = self.PLAYERSELECT
            self.menuMoveToPlayConfirm.closeSelf()
            self.methodChangeToPlay()
        else:
            self.menuMoveToPlayConfirm.closeSelf()
            self.openErrorNeedPlayers()
        
    def submitNo_MoveToPlay(self):
        self.menuMoveToPlayConfirm.closeSelf()
        self.switchToMainMenu()
        
    def submitOk_NeedPlayers(self):
        self.menuErrorNeedPlayers.closeSelf()
        self.switchToMainMenu()
        
    def submitYes_FillPlayers(self):
        self.closeDebugFillPlayers()
        self.debug_FillAllPlayers()
        
    def submitNo_FillPlayers(self):
        self.closeDebugFillPlayers()
        
    def submitPlayerName(self, strFirstName, strLastName):
        self.menuAddPlayerName.closeSelf()
        self.listPlayerInfo[self.INDEX_PINFO_FNAME] = strFirstName
        self.listPlayerInfo[self.INDEX_PINFO_LNAME] = strLastName
        # Check DB for name
        playerRow = self.database.findPlayerByName(strFirstName,strLastName)
        if len(playerRow) < 1:
            print("Player not found")
            self.intMenu = self.PLAYERCODENAME
            self.menuAddCodename.openSelf()
        else:
            player = playerRow[0] # First occurrence, if somehow multiple entries
            print(player)
            self.intMenu = self.ASKUSEPREVCODE
            self.menuUsePrevCodename.setCodename(player[self.INDEX_PINFO_CODE])
            self.menuUsePrevCodename.openSelf()
            self.listPlayerInfo[self.INDEX_PINFO_ID] = player[self.INDEX_PINFO_ID]
            self.listPlayerInfo[self.INDEX_PINFO_CODE] = player[self.INDEX_PINFO_CODE]
        
    def submitCodeName(self, strCodeName):
        self.listPlayerInfo[3] = strCodeName
        self.menuAddCodename.closeSelf()
        print(self.listPlayerInfo)
        if self.listPlayerInfo[self.INDEX_PINFO_ID] == 0:
            row = self.database.getLastId()
            id = 0
            if len(row) == 0:
                id = 1
            else:
                id = row[0][self.INDEX_PINFO_ID] + 1
            self.listPlayerInfo[self.INDEX_PINFO_ID] = id
            if self.database.findId(id) == []:
                self.database.insertPlayer(self.listPlayerInfo)
                self.database.commit()
        else:
            id = self.listPlayerInfo[self.INDEX_PINFO_ID]
            if self.database.findId(id) != []:
                self.database.updateUsingId(self.listPlayerInfo)
                self.database.commit()
        rows = self.database.getAllRows()
        print(rows)
        self.addPlayer(self.listPlayerInfo[self.INDEX_PINFO_FNAME] + " " 
                        + self.listPlayerInfo[self.INDEX_PINFO_LNAME],
                        self.listPlayerInfo[self.INDEX_PINFO_CODE])
        self.switchToMainMenu()
            
    def getPlayerAtArrow(self):
        return self.frameTeamBoxes.getPlayerAtArrow()
        
    def addPlayer(self, strPlayer, strCode):
        self.frameTeamBoxes.addPlayer(strPlayer, strCode)
        self.listPlayerInfo = [0,"","",""]
        self.root.update()
        
    def deletePlayer(self, event=None):
        self.frameTeamBoxes.deletePlayer()
        self.root.update()
        
    def clearAllPlayers(self):
        self.frameTeamBoxes.deleteAllPlayers()
        self.root.update()
             
    def debug_AddOrUpdatePlayer(self, strPlayerFirstName, strPlayerLastName, strPlayerCodename):
        tupleDBEntry = self.database.findPlayerByName(strPlayerFirstName, strPlayerLastName)
        if tupleDBEntry is None or len(tupleDBEntry) == 0:
            tupleLastEntry = self.database.getLastId()
            intNextID = 0
            if len(tupleLastEntry) > 0:
                intNextID = int(tupleLastEntry[0][0])+1
            listNewPlayerEntry = [intNextID, str(strPlayerFirstName), str(strPlayerLastName), str(strPlayerCodename)]
            self.database.insertPlayer(listNewPlayerEntry)
        else:
            listUpdatedEntry = [tupleDBEntry[0][0], tupleDBEntry[0][1], tupleDBEntry[0][2], tupleDBEntry[0][3]]
            listUpdatedEntry[3] = strPlayerCodename
            self.database.updateUsingId(listUpdatedEntry)
        self.database.commit()
        
    def debug_FillAllPlayers(self):
        listRedPlayerNames = ["Janice Evans", "Raymond Griffin", "Patrick Hill", "Matthew Bryant",
                            "Jason Martin", "Catherine Carter", "Kevin Sanders", "Gary Young",
                            "Anthony Russel", "Pamela Hart", "Leonardo Harris", "Nick Wells",
                            "Simon Mitchell", "Paul Willis", "Paula Reyes"]
        listGreenPlayerNames = ["Steven Perez", "Gary Patterson", "Janice Hall", "Kenneth Edwards",
                                "Walter Howard", "Norman Hughes", "Lewis Hayes", "Angela Shaw",
                                "Burt Davis", "Kevin Simpson", "Carlene Brown", "Frederick Baker",
                                "Derick Smith", "Stephen Morris", "Max Reed"]
        listRedCodenames = ["ProudPancake","ExcitingEgg","SmoggyGhost","HollowHorse",
                            "BarbaricMouse","GracefulTiger","BusyBear","BrawnyBee",
                            "DullBell","CharmingJellyfish", "GentleCow", "CleverPotato",
                            "SpitefulArmadillo","DapperVelociraptor","MeekMouse"]
        listGreenCodenames = ["PhantomFairy","GrumpyCat","ChiefRat","RaggedRabbit",
                            "SpikyWorm","DecisiveDuck","LoudCloud","GraySnail",
                            "SaltyPig","JollySponge","SpicySugar","DraconianDeer",
                            "SoftTomato","IcyIgloo","MoldyApple"]
        for j in range(0, 2):
            for i in range(0, 15):
                if j == 0:
                    self.frameTeamBoxes.setArrowPos(Frame_TeamBoxes.REDARROWPOS, i)
                    self.frameTeamBoxes.addPlayer(listRedPlayerNames[i],
                                                    listRedCodenames[i])
                    listPlayerNameSplit = listRedPlayerNames[i].split(" ")
                    self.debug_AddOrUpdatePlayer(listPlayerNameSplit[0], listPlayerNameSplit[1],                        listRedCodenames[i])
                else:
                    self.frameTeamBoxes.setArrowPos(Frame_TeamBoxes.GREENARROWPOS, i)
                    self.frameTeamBoxes.addPlayer(listGreenPlayerNames[i],
                                                    listGreenCodenames[i])
                    listPlayerNameSplit = listGreenPlayerNames[i].split(" ")
                    self.debug_AddOrUpdatePlayer(listPlayerNameSplit[0], listPlayerNameSplit[1],                        listRedCodenames[i])
                self.root.update()
        self.frameTeamBoxes.setArrowPos(Frame_TeamBoxes.REDARROWPOS, 0)