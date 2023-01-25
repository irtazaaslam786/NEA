import tkinter as tk
from datetime import date
import tksheet

from Scheduler import *

databaseAddress = "myDatabase.db"

def exit_handler():
    root.destroy()
    scheduler.closeDatabase()

root = tk.Tk() #root window
root.protocol("WM_DELETE_WINDOW", exit_handler)
root.title("M&S Scheduler") #window title
root.geometry('1200x6000')    #window dimensions

table = tksheet.Sheet(root) #creating table
table.grid()    #snap table to grid

scheduler = Scheduler(databaseAddress)
scheduler.DBcontroller.createEmployeeTable()
scheduler.DBcontroller.createShiftsTable()
scheduler.DBcontroller.createEmployee("fname", "sname", 24, "Stock")
scheduler.DBcontroller.createShift("1", "11:00", "20:00", "11:01:2023", "14:30")
shiftData = scheduler.getShiftsForDay("11:01:2023")


table.headers(["Column 1", "Column 2", "Column 3", "Column 4", "Column 5"])
table.set_sheet_data(shiftData)

#add widget functionality here

#add widgets here

root.mainloop()


