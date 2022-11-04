import tkinter as tk
from tkinter import ttk
from lib.Database import *
from lib.Frame_FKeys import *
from lib.AppObject import *
from lib.editgame.Frame_TeamBoxes import *
from lib.editgame.MenuManager_EditGame import *

class Controller_EditGame():
	def __init__(self, tkroot, editGame):
		editGame = None
		self.root = tkroot
		self.menuManager = None
		self.setEditGameUI(editGame)
		
	def setEditGameUI(self, editGame):
		self.editGame = editGame
		
	def isEditGameUISet(self):
		return self.editGame != None
		
	def createMenuManager(self, database, TeamBoxes):
		if self.isEditGameUISet():
			self.menuManager.setDatabase(database)
			self.menuManager.setTeamBoxes(TeamBoxes)
			self.menuManager.createSelf()
			self.menuManager = MenuManager_EditGame(self.editGame)
		else:
			raise Exception("Error: self.editGame is set to None!")
		
	def gridify(self):
		if self.isEditGameUISet():
			self.editGame.setMenuManagerOntoGrid(self.menuManager)

	#Get data
	def getMenuManager(self):
		return self.menuManager
		
	def getMenuState(self):
		return self.menuManager.getMenuState()
		
	def getPlayerList(self):
		return self.TeamBoxes.getPlayerList()
		
	def getPlayerAtArrow(self):
		return self.TeamBoxes.getPlayerAtArrow()


	# Returns reference to menu manager
	def moveArrow(self, offSetX, offSetY):
		if self.TeamBoxes.isValidArrowOffset(offSetX, offSetY):
			self.TeamBoxes.moveArrow(offSetX, offSetY)
			self.root.update()         
		
	def switchToMainMenu(self):
		self.menuManager.switchToMainMenu()

	def openMoveToPlayConfirm(self):
		self.menuManager.showSelf()
		self.menuManager.openMoveToPlayConfirm()	
		
	def bind_ChangeToPlay(self, mFunc):
		self.menuManager.bind_ChangeToPlay(mFunc)

			
	#Player Modification		
	def openAddPlayerName(self):
		self.menuManager.openAddPlayerName()

	def addPlayer(self, strPlayer, strCode):
		self.TeamBoxes.addPlayer(strPlayer, strCode)
		self.root.update()

	def openAddCodename(self):
		self.menuManager.openAddCodename()

	
	#Closures	
	def closeAllMenus(self):
		self.menuManager.closeAllMenus()
			
	def openDeleteDBConfirmMenu(self):
		self.menuManager.showSelf()
		self.menuManager.openDeleteDBConfirmMenu()	

		
	#Removal of players
	def deletePlayer(self, event):
		event = None
		self.TeamBoxes.deletePlayer()
		self.root.update()
		
	def clearAllPlayers(self):
		self.TeamBoxes.deleteAllPlayers()
		self.root.update()