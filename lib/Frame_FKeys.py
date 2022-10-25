import tkinter as tk
from tkinter import ttk
from lib.AppObject import *

class Frame_FKeys(AppObject):
    def __init__(self, tkRoot):
        super().__init__(tkRoot)
        self.intDefaultTextsize = 12
        self.intFKeyAmount = 12
        # Initialized in createFKeys
        self.labelFKey = [None] * self.intFKeyAmount
        self.frameFKey = [None] * self.intFKeyAmount
        
        self.createSelf()
        
    def setKeyText(self, intFKey, strText, intTextSize=0):
        if intTextSize==0:
            intTextSize=self.intDefaultTextsize
        if intFKey < 1 or intFKey > 12:
            raise Exception("Frame_FKeys: Invalid F Key passed to setKeyText!")
        else:
            intFKeyArrayPos = intFKey - 1
            self.labelFKey[intFKeyArrayPos].config(font=(self.strDefaultFont, intTextSize))
            self.labelFKey[intFKeyArrayPos]["text"] = strText

    def clearAllKeyText(self):
        for i in range(1,self.intFKeyAmount):
            self.setKeyText(i,"")
        
    def createSelf(self):
        self["bg"]="#000000"
        self.propagateWidget(self)
        self.createFKeys()     
            
    def createFKeys(self):
        strTextColor = "#36B043" # Neon Green
        strBGColor = "#000000" # Black
        strBorderColor = "#FFFFFF" # White
        strFontStyle = self.strDefaultFont
        intFontSize = self.intDefaultTextsize
    
        for i in range(0,self.intFKeyAmount):
            self.frameFKey[i] = tk.Frame(self,bg=strBorderColor)
            self.labelFKey[i] = tk.Label(self.frameFKey[i], 
                text="",
                fg=strTextColor, bg=strBGColor, 
                font=(strFontStyle,intFontSize))
            self.propagateWidget(self.frameFKey[i])
            self.propagateWidget(self.labelFKey[i])
            
        self.labelFKey[0]["text"]="F1 \nEdit \nGame"
        self.labelFKey[1]["text"]="F2 \nGame \nParameters"
        self.labelFKey[2]["text"]="F3 \nStart \nGame"
        self.labelFKey[4]["text"]="F5 \nPre-\nEntered \nGame"
        self.labelFKey[6]["text"]=""
        self.labelFKey[7]["text"]="F8 \nView \nGame"
        self.labelFKey[9]["text"]="F10 \nFlick \nSync"
        self.labelFKey[10]["text"]="F11 \nClear \nGame"
        
    def gridify(self):
        intFrameCols = 24
        intFrameRows = 1
        # FKey attributes
        intPosRow = 0
        intRowSpan = 1
        intColSpan = 2
        
        for i in range(intFrameCols):
            self.columnconfigure(i,weight=1, uniform="gridUniform")
        for i in range(intFrameRows):
            self.rowconfigure(i,weight=1, uniform="gridUniform")
            
        for i in range(0, self.intFKeyAmount):
            self.frameFKey[i].grid(column=i*2, row=intPosRow, 
                rowspan=intRowSpan, columnspan=intColSpan, 
                sticky="NSEW")
        
        self.gridifyFKeys()
    
    def gridifyFKeys(self):
        intPadX = 2
        tuplePadY = (2,0)
        
        for i in range(0,self.intFKeyAmount):
            self.labelFKey[i].pack(padx=intPadX,pady=tuplePadY,fill="both", expand=True)