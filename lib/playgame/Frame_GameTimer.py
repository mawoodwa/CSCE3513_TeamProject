import tkinter as tk
from tkinter import ttk
from lib.AppObject import *

class Frame_GameTimer(AppObject):
    def __init__(self, tkRoot):
        super().__init__(tkRoot)
        
        self.createSelf()
        
    def createSelf(self):
        strBGColor = "#000000"
        strTextColor = "#FFFFFF"
        strFont = self.strDefaultFont
        strTextsizeTime = 24
    
        self["bg"] = strBGColor        
        
        self.labelTimeRemaining = tk.Label(self, 
            text="Time Remaining: 5:00",
            fg=strTextColor, bg=strBGColor, font=(self.strDefaultFont, strTextsizeTime))
        self.propagateWidget(self.labelTimeRemaining)
        
    def gridify(self):
        intCols = 1
        intRows = 1
        for i in range(intCols):
            self.columnconfigure(i,weight=1, uniform="gridUniform")
        for i in range(intRows):
            self.rowconfigure(0,weight=1, uniform="gridUniform")
        self.labelTimeRemaining.grid(column=0, row=0, sticky="E")
        
    def updateTimer(self, strTime):
        self.labelTimeRemaining["text"] = "Time Remaining: " + strTime