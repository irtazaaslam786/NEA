import tkinter as tk

class DeleteWindow:
    def __init__(self, master, geometry):
        self.master = master
        self.master.withdraw()
        self.window = tk.Toplevel(self.master)
        self.window.title("Delete Employees")
        self.window.geometry(geometry)
        self.window.protocol("WM_DELETE_WINDOW", self.showWindow)
    def showWindow(self):
        self.master.deiconify()
        self.window.destroy()
