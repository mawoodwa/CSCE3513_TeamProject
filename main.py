# READ ME
# > Initial version of Team Project - Laser Tag program
# > Intended only for use in Team 8 of UArk CSCE 3513, Fall 2022
# > Program is incomplete. Major bugs are to be expected
# > Program has currently only been tested on Windows 10 and Linux Cinnamon Mint
# > Program requires latest pynput and tkinter modules to be installed
# > Program is NOT intended to work on Mac OS
# 
# DEPENDENCY INSTALLATION
# > Tkinter should be installed with python3 by default
# > If not installed in linux, use command: sudo apt-get install python-tk
# > For pynput, install via pip: pip install pynput
#
# HOW TO
# > Run program by typing in commandline (without quotations): "python main.py"
# > Use F7 to change between screens, including Splash
# > Only the Edit Game screen has functionality as of now
# > Edit Game functionality uses arrow keys, and Ins/Del
#       as seen on the bottom part of the window
#
# TESTING NEEDED
# > More systems (test with multiple Windows/Linux computers)
# > Ensure screen resolution is not an issue (current minimum: 1200x700)
# > ... (More to be added)

from sys import platform
import time
from pynput import keyboard
import tkinter as tk
from tkinter import ttk
from lib.editgame.Screen_EditGame import *
from lib.playgame.Screen_PlayGame import *
from lib.splash.Screen_Splash import *

class App(tk.Frame):
    S_SPLASH = 0
    S_EDITGAME = 1
    S_PLAYGAME = 2
    def __init__(self, tkRoot):
        super().__init__(tkRoot)
        self.root = tkRoot
        self.root.configure(background="#000000")
    
        # Root Window
        self.root.title("Entry Terminal")
        self.root.geometry("1200x800+0+0") # Originally tested on 1200x800
        self.root.minsize(1000,700) # Minimum size of window is 1200x700 before scrunching
        #self.root.resizable(False, False)
        
        print("Running for platform: {}".format(platform))
        if platform == "win32" or platform == "win64" or platform == "win82":
            self.root.state("zoomed")
        else:
            self.root.wm_attributes('-zoomed',1)
        self.propagateWidget(self.root)
        
        # Using grid instead of pack to allow frame-on-frame for
        #    inserting player menu, and other similar menus
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0,weight=1)
        self["bg"] = "#000000"
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.grid(column=0, row=0,sticky="NSEW")
        
        # Needed for bug with F10 key.
        self.inputSim = keyboard.Controller()
        
        # App members
        self.screen_Splash = Screen_Splash(self)
        self.screen_Splash.grid(column=0, row=0,sticky="NSEW")
        self.screen_EditGame = Screen_EditGame(self)
        self.screen_EditGame.bind_ChangeToPlay(self.changeToPlay)
        self.screen_EditGame.grid(column=0, row=0,sticky="NSEW")
        self.screen_PlayGame = Screen_PlayGame(self)
        self.screen_PlayGame.bind_MoveToEdit(self.changeToEdit)
        self.screen_PlayGame.grid(column=0, row=0,sticky="NSEW")
        
        self.currentScreen = self.S_SPLASH
        self.screen = self.screen_Splash
        self.changeScreens(self.S_SPLASH)
        self.startInputListener()
        self.root.update()
        print("Waiting 3 seconds...")
        self.idRootAfter = self.root.after(3000, self.showSplashFor3Sec)
    
    # Size control - prevent widget from over-expanding outside grid cell
    # This should be applied to most widgets
    def propagateWidget(self, widget):
        widget.pack_propagate(0)
        widget.grid_propagate(0)
        
    def changeScreens(self, nextScreen):
        self.unloadCurrentScreen()
        self.loadScreen(nextScreen)
        self.root.update()
        
    # Used to bind in Screen_EditGame
    def changeToPlay(self):
        self.screen_EditGame.closeAllMenus()
        self.changeScreens(self.S_PLAYGAME)
        self.screen_PlayGame.startWaitTimer()
        
    # Used to bind in Screen_PlayGame
    def changeToEdit(self):
        self.screen_PlayGame.closeAllMenus()
        self.changeScreens(self.S_EDITGAME)
            
    def unloadCurrentScreen(self):
        if self.currentScreen == self.S_SPLASH:
            self.unloadScreen_Splash()
        elif self.currentScreen == self.S_EDITGAME:
            self.unloadScreen_EditGame()
        elif self.currentScreen == self.S_PLAYGAME:
            self.unloadScreen_PlayGame()
        else:
            print("Changing from unknown screen")
            
    def loadScreen(self, nextScreen):
        if nextScreen == self.S_SPLASH:
            print("Loading Splash...")
            self.currentScreen = self.S_SPLASH
            self.loadScreen_Splash()
        elif nextScreen == self.S_EDITGAME:
            print("Loading Edit Game...")
            self.currentScreen = self.S_EDITGAME
            self.loadScreen_EditGame()
        elif nextScreen == self.S_PLAYGAME:
            print("Loading Play Game...")
            self.currentScreen = self.S_PLAYGAME
            self.loadScreen_PlayGame()
        else:
            print("Not a valid screen!")
    
    def loadScreen_Splash(self):
        self.screen = self.screen_Splash
        self.screen.showSelf()
        
    def unloadScreen_Splash(self):
        self.screen.hideSelf()
            
    def loadScreen_EditGame(self):
        self.screen = self.screen_EditGame
        self.screen.showSelf()
        self.screen.tkraise()
        
    def unloadScreen_EditGame(self):
        self.screen.hideSelf()
        
    def loadScreen_PlayGame(self):
        self.screen = self.screen_PlayGame
        listPlayers = self.screen_EditGame.getPlayerList()
        self.screen.setPlayersUsingList(listPlayers)
        self.screen.showSelf()
        
    def unloadScreen_PlayGame(self):
        self.screen.hideSelf()
        
    def showSplashFor3Sec(self):
        print("3 seconds finished.")
        self.root.after_cancel(self.idRootAfter)
        self.changeScreens(self.S_EDITGAME)
        
    # Used for debugging
    def any_SwitchScreen(self, key):
        if key == keyboard.Key.f1:
            currentScreen = self.currentScreen
            if currentScreen == self.S_SPLASH:
                self.changeScreens(self.S_EDITGAME)
            elif currentScreen == self.S_EDITGAME:
                self.changeScreens(self.S_PLAYGAME)
            elif currentScreen == self.S_PLAYGAME:
                self.changeScreens(self.S_SPLASH)
                
    def any_InputListen(self, key):
        if key == keyboard.Key.f10:
            self.inputSim.press(keyboard.Key.f10)
        
    def editgame_PlayerSelect(self, key):
        if key == keyboard.Key.up:
            self.screen.moveArrow(0,-1)
        elif key == keyboard.Key.down:
            self.screen.moveArrow(0,1)
        if key == keyboard.Key.left:
            self.screen.moveArrow(-1,0)
        elif key == keyboard.Key.right:
            self.screen.moveArrow(1,0)
            
        if key == keyboard.Key.insert:
            self.screen.openAddPlayerName()
        if key == keyboard.Key.delete:
            self.screen.deletePlayer()
            
        if key == keyboard.Key.f5:
            self.screen.openMoveToPlayConfirm()
            
        if key == keyboard.Key.f7:
            self.screen.openDeleteDBConfirmMenu()
            
    def editgame_PlayerIns(self, key):
        if key == keyboard.Key.esc:
            self.screen.closeAllMenus()
            
    def playgame_Listen(self, key):
        if key == keyboard.Key.f5:
            if self.screen.getMenuState() == self.screen.MENU_MAIN or self.screen.getMenuState() == self.screen.MENU_WAITSTART:
                self.screen.openMoveToEditMenu()
        if key == keyboard.Key.esc:
            self.screen.closeAllMenus()
        
    def on_press(self, key):
        if self.currentScreen == self.S_EDITGAME:
            if self.screen.getMenuState() == self.screen.PLAYERSELECT:
                self.editgame_PlayerSelect(key)
            elif self.screen.getMenuState() != self.screen.PLAYERSELECT:
                self.editgame_PlayerIns(key)
        elif self.currentScreen == self.S_PLAYGAME:
            self.playgame_Listen(key)
        elif self.currentScreen == self.S_SPLASH:
            pass
        self.any_InputListen(key)
            
    def closeDB(self):
        if self.screen_EditGame == None:
            print("Closing DB...")
            self.database.closeDB_NoCommit()
        else:
            self.screen_EditGame.closeDB()
        
    def on_release(self, key):
        True==True
        
    def startInputListener(self):
        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        self.listener.start()
        
def driver_TK():
    tkRoot = tk.Tk()
    app = App(tkRoot)
    app.mainloop()
    app.closeDB()

if __name__ == "__main__":
    driver_TK()