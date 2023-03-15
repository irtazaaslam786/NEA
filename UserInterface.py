import tkinter as tk
from datetime import date
import tksheet

from Scheduler import *
from AddWindow import *
from ViewWindow import *
from DeleteWindow import *

databaseAddress = "myDatabase.db"


def main_exit_handler():
    root.destroy()
    scheduler.closeDatabase()


def showWindow(oldWindow):
    root.deiconify()
    oldWindow.destroy()


def createAddWindow():
    addWindow = AddWindow(root, "500x300", scheduler)


def createViewWindow():
    viewWindow = ViewWindow(root, "500x300", scheduler)


def createDeleteWindow():
    deleteWindow = DeleteWindow(root, "500x300", scheduler)


def closeProgram():
    root.destroy()
    scheduler.closeDatabase()


root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", main_exit_handler)
root.title("M&S Scheduler")
root.geometry('800x600')
scheduler = Scheduler(databaseAddress)

addDataButton = tk.Button(root, text="Add Data", command=createAddWindow)
ViewButton = tk.Button(root, text="View", command=createViewWindow)
DeleteButton = tk.Button(root, text="Delete", command=createDeleteWindow)
QuitButton = tk.Button(root, text="Quit", command=closeProgram)

addDataButton.pack()
ViewButton.pack()
DeleteButton.pack()
QuitButton.pack()

root.mainloop()

