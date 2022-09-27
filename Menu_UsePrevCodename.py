import tkinter as tk
from tkinter import ttk

class Menu_UsePrevCodename(tk.Frame):
    def __init__(self, tkRoot, mSubmitYes, mSubmitNo):
        super().__init__(tkRoot)
        self.root = tkRoot
        
        self.strDefaultFont = "Arial"
        self["bg"]="#000000"
        
        self.methodSubmitYes = mSubmitYes
        self.methodSubmitNo = mSubmitNo
        self.strPlayerCodename = ""
        self.create()
        self.gridify()
        
    # Size control - prevent widget from over-expanding outside grid cell
    # This should be applied to most widgets
    def propagateWidget(self, widget):
        widget.pack_propagate(False)
        widget.grid_propagate(False)
        
    def destroyMain(self):
        self.destroy()
        
    def hideSelf(self):
        self.grid_remove()
        
    def showSelf(self):
        self.grid()

    def openMenu(self):
        self.tkraise()
        self.buttonSubmitYes["state"]="normal"
        self.buttonSubmitNo["state"]="normal"
        self.root.update()
        
    def closeMenu(self):
        self.buttonSubmitYes["state"]="disabled"
        self.buttonSubmitNo["state"]="disabled"
        self.root.update()
        
    def submitNo(self,event=None):
        self.methodSubmitNo()
        
    def submitYes(self, event=None):
        self.methodSubmitYes()
        
    def setCodename(self, strCodename):
        self.strPlayerCodename = strCodename
        self.labelPlayerCodeName = "Player Code Name: " + self.strPlayerCodename
            
    def create(self):
        strBorderColor = "#5b5bc3"
        strBGColor = "#000000"
        strTextcolorError = "#FF0000" # True Red
        strTextcolorMain = "#FFFFFF" # Full White
        strFont = self.strDefaultFont
        intTextsizeHead = 20
        intTextsizeError = 14
        intTextsizeMain = 16
    
        #self.frameInsP = tk.Frame(self.root, bg=strBorderColor)
        self.propagateWidget(self)
        self.frameInterior = tk.Frame(self, bg=strBGColor)
        self.labelHead = tk.Label(self.frameInterior,
            text="Player Codename found!",
            fg = strTextcolorMain, bg=strBGColor,font=(strFont,intTextsizeHead))
        self.labelPlayerCodeName = tk.Label(self.frameInterior,
            text="Player Code Name: " + self.strPlayerCodename,
            fg = strTextcolorMain, bg=strBGColor,font=(strFont,intTextsizeMain))
        self.labelHint = tk.Label(self.frameInterior,
            text="Use previous Codename?\nIf No, you will be asked to enter a new codename.",
            fg = strTextcolorMain, bg=strBGColor, font=(strFont,intTextsizeMain))
        self.buttonSubmitYes = tk.Button(self.frameInterior,
            text="Yes",
            command=self.submitYes,
            state="disabled",
            fg=strTextcolorMain, bg=strBGColor, font=(strFont, intTextsizeMain))
        self.buttonSubmitYes.bind("<Return>",self.submitYes)
        self.buttonSubmitNo = tk.Button(self.frameInterior,
            text="No",
            command=self.submitNo,
            state="disabled",
            fg=strTextcolorMain, bg=strBGColor, font=(strFont, intTextsizeMain))
        self.buttonSubmitNo.bind("<Return>",self.submitNo)
        
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
        self.labelPlayerCodeName.grid(column=0,row=3,columnspan=intFrameInsPCols,rowspan=2,sticky="NSEW")
        self.labelHint.grid(column=0,row=5,rowspan=2,columnspan=intFrameInsPCols,sticky="NSEW")
        self.buttonSubmitYes.grid(column=3,row=9,rowspan=2,columnspan=2,sticky="NSEW")
        self.buttonSubmitNo.grid(column=7,row=9,rowspan=2,columnspan=2,sticky="NSEW")