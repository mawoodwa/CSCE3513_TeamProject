import tkinter as tk
from tkinter import ttk
import time
from lib.Menu import *

class Frame_WaitUntilPlay(Menu):
    def __init__(self, tkRoot):
        super().__init__(tkRoot)
        
        self.boolIsCountActive = False
        self.boolIsPaused = False
        self.intTimeRemaining = 0.0
        
        self.createSelf()
        self.gridify()
        
            
    def createSelf(self):
        strBorderColor = "#FFFFFF" #old color - light blue "#5b5bc3"
        strBGColor = "#000000"
        strTextcolorError = "#FF0000" # True Red
        strTextcolorMain = "#FFFFFF" # Full White
        strFont = self.strDefaultFont
        intTextsizeHead = 32
        intTextsizeError = 14
        intTextsizeMain = 32
    
        self["bg"] = strBorderColor
        self.propagateWidget(self)
        self.frameInterior = tk.Frame(self, bg=strBGColor)
        self.labelHead = tk.Label(self.frameInterior,
            text="Game beginning in...",
            fg = strTextcolorMain, bg=strBGColor,font=(strFont,intTextsizeHead))
        self.labelTimer = tk.Label(self.frameInterior,
            text="30:00",
            fg = strTextcolorMain, bg=strBGColor, font=(strFont,intTextsizeMain))
            
    def resetToDefault(self):
        self.labelHead["text"] = "Game beginning in..."
        self.labelHead["fg"] = "#FFFFFF"
        self.labelTimer["fg"] = "#FFFFFF"
        self.labelTimer["font"] = (self.strDefaultFont, 32)
        
    def gridify(self):
        intBorderSize = 10
        self.frameInterior.pack(side="top", fill="both", expand=True, 
            padx=intBorderSize, pady=intBorderSize)
        
        intFrameInsPCols = 1
        intFrameInsPRows = 3
        
        for i in range(intFrameInsPCols):
            self.frameInterior.columnconfigure(i,weight=1,uniform="uniformIns")
        for i in range(intFrameInsPRows):
            self.frameInterior.rowconfigure(i,weight=1,uniform="uniformIns")
        self.labelHead.grid(column=0,row=0,sticky="SEW")
        self.labelTimer.grid(column=0,row=1,sticky="NEW")
        
    def enableSelf(self):
        pass
        
    def disableSelf(self):
        pass
        
    def isPaused(self):
        return self.boolIsPaused
        
    def isCountActive(self):
        return self.boolIsCountActive
        
    def getTimeRemaining(self):
        return self.intTimeRemaining
        
    def beginCount(self, counttime=30.0):
        print("Beginning count with counttime: {}".format(counttime))
        self.timeUntil = time.time() + counttime
        self.resetToDefault()
        self.idRootAfter = self.root.after(1, self.updateCount)
        self.boolIsCountActive = True
        
    def pauseCount(self):
        self.intTimeRemaining = self.timeUntil - time.time()
        boolIsCountActive = self.boolIsCountActive
        self.endCount()
        self.boolIsCountActive = boolIsCountActive
        self.boolIsPaused = True
        
    def unpauseCount(self):
        self.beginCount(self.intTimeRemaining)
        self.boolIsPaused = False
        
    def updateCount(self):
        intTimeRemaining = self.timeUntil - time.time()
        if intTimeRemaining < 10.0 and self.labelTimer["bg"] != "#ff6666":
            self.labelHead["fg"] = "#ff6666"
            self.labelHead["text"] = "Game imminent! \nStarting in..."
            self.labelTimer["fg"] = "#ff6666"
        if not self.boolIsPaused:
            if intTimeRemaining > 0.0:
                self.root.after_cancel(self.idRootAfter)
                self.labelTimer["text"] = str(self.timeUntil - time.time())[:5]
                self.root.update()
                self.idRootAfter = self.root.after(1, self.updateCount)
            else:
                self.root.after_cancel(self.idRootAfter)
                self.labelHead["text"] = ""
                self.labelTimer["font"] = (self.strDefaultFont, 72)
                self.labelTimer["text"] = "BEGIN!"
                print("BEGIN!")
                self.root.update()
                self.idRootAfter = self.root.after(1000, self.endCountInternal)
                
    def endCountInternal(self):
        self.endCount(True)
        
    def endCount(self, boolCalledInternally=False):
        self.root.after_cancel(self.idRootAfter)
        self.resetToDefault()
        self.hideSelf()
        self.boolIsCountActive = False
        self.boolIsPaused = False
        if boolCalledInternally:
            self.methodAfterFinished()
        
    def bindMethodAfterFinished(self, methodAfterFinished):
        self.methodAfterFinished = methodAfterFinished