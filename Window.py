import tkinter as tk
from datetime import datetime

class Window:
    def __init__(self, master, geometry, scheduler):
        self.master = master
        self.scheduler = scheduler
        self.master.withdraw()
        self.window = tk.Toplevel(self.master)
        self.window.geometry(geometry)
        self.window.protocol("WM_DELETE_WINDOW", self.closeWindow)
        self.QuitButton = tk.Button(self.window, text="Quit", command=self.closeWindow)

    def closeWindow(self):
        self.master.deiconify()
        self.window.destroy()

    def getDate(self):
        return datetime.today().strftime('%d/%m/%Y')
