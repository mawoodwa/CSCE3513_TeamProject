import tkinter as tk
from tkinter import ttk

class Screen_Splash(tk.Frame):
    def __init__(self, tkRoot):
        super().__init__(tkRoot)
        self.root = tkRoot
        
        self.createScreen()
        self.gridify()
        
        
    # Size control - prevent widget from over-expanding outside grid cell
    # This should be applied to most widgets
    def propagateWidget(self, widget):
        widget.pack_propagate(False)
        widget.grid_propagate(False)
        
    def destroyMain(self):
        '''Deletes main frame'''
        self.mainFrame.destroy()
        
    def hideSelf(self):
        '''Removes widgets from grid'''
        self.mainFrame.grid_remove()
        
    def showSelf(self):
        ''' organises widgets in a table-like structure'''
        self.mainFrame.grid()
        
    def createScreen(self):
        '''create splash screen'''
        strBGColor = "#000000"
    
        self.mainFrame = tk.Frame(self.root, 
            bg=strBGColor) 
        self.propagateWidget(self.mainFrame)
        self.imgSplash = tk.PhotoImage(file="./logo.png")
        self.labelSplash = tk.Label(self.mainFrame,
            image=self.imgSplash)
        
    def gridify(self):
        '''Expands image'''
        self.mainFrame.grid(column=0,row=0,sticky="NSEW")
        self.labelSplash.place(relx=0.5,rely=0.5,anchor=tk.CENTER) 
        
