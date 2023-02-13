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

#add widget functionality here
def createAddWindow():
    addWindow = AddWindow(root, "500x300", scheduler)

def createViewWindow():
    viewWindow = ViewWindow(root, "500x300", scheduler)

def createDeleteWindow():
    deleteWindow = DeleteWindow(root, "500x300", scheduler)

root = tk.Tk() #root window
root.protocol("WM_DELETE_WINDOW", main_exit_handler)
root.title("M&S Scheduler") #window title
root.geometry('800x600')    #window dimensions
scheduler = Scheduler(databaseAddress)  #create scheduler instance

'''
table = tksheet.Sheet(root, width = 750, height = 550) #creating table
shiftData, columns = scheduler.getEmployeeData()
table.headers(columns)
table.set_sheet_data(shiftData) '''

addDataButton = tk.Button(root, text="Add Data", command=createAddWindow)
ViewButton = tk.Button(root, text="View", command=createViewWindow)
DeleteButton = tk.Button(root, text="Delete", command=createDeleteWindow)


#add widgets here
addDataButton.pack()
ViewButton.pack()
DeleteButton.pack()

#table.grid()    #snap table to grid
root.mainloop()



