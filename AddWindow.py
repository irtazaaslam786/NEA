import tkinter as tk

class AddWindow:
    def __init__(self, master, geometry):
        self.master = master
        self.master.withdraw()
        self.window = tk.Toplevel(self.master)
        self.window.title("Add Data")
        self.window.geometry(geometry)
        self.window.protocol("WM_DELETE_WINDOW", self.showWindow)
    def showWindow(self):
        self.master.deiconify()
        self.window.destroy()
