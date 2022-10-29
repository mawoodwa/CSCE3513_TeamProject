import tkinter as tk
from tkinter import ttk
from lib.Menu import *

class Menu_ErrorNeedPlayers(Menu):
    def __init__(self, tkRoot, mSubmitOk):
        super().__init__(tkRoot)
        
        self.methodSubmitOk = mSubmitOk
        self.createSelf()
        self.gridify()

    def enableSelf(self):
        self.tkraise()
        self.buttonSubmitOk["state"]="normal"
        self.buttonSubmitOk.bind("<Return>",self.submitOk)
        
    def disableSelf(self):
        self.buttonSubmitOk["state"]="disabled"
        self.buttonSubmitOk.unbind("<Return>")
        
    def submitOk(self,event=None):
        self.methodSubmitOk()
            
    def createSelf(self):
        strBorderColor = "#5b5bc3"
        strBGColor = "#000000"
        strTextcolorError = "#FF0000" # True Red
        strTextcolorMain = "#FFFFFF" # Full White
        strFont = self.strDefaultFont
        intTextsizeHead = 24
        intTextsizeMain = 24
    
        self.propagateWidget(self)
        self.frameInterior = tk.Frame(self, bg=strBGColor)
        self.labelHead = tk.Label(self.frameInterior,
            text="Error: Not Enough Players!",
            fg = strTextcolorError, bg=strBGColor,font=(strFont,intTextsizeHead))
        self.labelHint = tk.Label(self.frameInterior,
            text="You need at least 1 player \non each team.",
            fg = strTextcolorMain, bg=strBGColor, font=(strFont,intTextsizeMain))
        self.buttonSubmitOk = tk.Button(self.frameInterior,
            text="Return to Edit Game",
            command=self.submitOk,
            state="disabled",
            fg=strTextcolorMain, bg=strBGColor, font=(strFont, intTextsizeMain))
        self.buttonSubmitOk.bind("<Return>",self.submitOk)
        
    def gridify(self):
        intBorderSize = 10
        self.frameInterior.pack(side="top", fill="both", expand=True, 
            padx=intBorderSize, pady=intBorderSize)
        
        intFrameInsPCols = 12
        intFrameInsPRows = 12
        
        for i in range(intFrameInsPCols):
            self.frameInterior.columnconfigure(i,weight=1,uniform="uniformIns")
        for i in range(intFrameInsPRows):
            self.frameInterior.rowconfigure(i,weight=1,uniform="uniformIns")
        self.labelHead.grid(column=0,row=0,columnspan=intFrameInsPCols,rowspan=2,sticky="NSEW")
        self.labelHint.grid(column=0,row=5,rowspan=2,columnspan=intFrameInsPCols,sticky="NSEW")
        self.buttonSubmitOk.grid(column=2,row=9,rowspan=2,columnspan=8,sticky="NSEW")