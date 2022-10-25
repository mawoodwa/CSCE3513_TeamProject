import tkinter as tk
from tkinter import ttk
from lib.AppObject import *

class Menu(AppObject):
    def __init__(self, tkRoot):
        super().__init__(tkRoot) 
        
    def destroyMain(self):
        self.destroy()
        
    def openSelf(self):
        self.showSelf()
        self.enableSelf()
        
    def closeSelf(self):
        self.hideSelf()
        self.disableSelf()

    def enableSelf(self):
        pass
        
    def disableSelf(self):
        pass
            
    def createSelf(self):
        pass
        
    def gridify(self):
        pass