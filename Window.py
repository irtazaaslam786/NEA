import tkinter as tk

class Window:
    def __init__(self, master, geometry):
        self.master = master
        self.master.withdraw()
        self.window = tk.Toplevel(self.master)
        self.window.geometry(geometry)
        self.window.protocol("WM_DELETE_WINDOW", self.closeWindow)

    def closeWindow(self):
        self.master.deiconify()
        self.window.destroy()
