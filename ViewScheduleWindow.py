import tkinter as tk
import tksheet

from Window import *

class ViewScheduleWindow(Window):
    def __init__(self, master, geometry, scheduler):
        super().__init(master, geometry, scheduler)
        self.window.title("View Schedule")

        self.createScheduleTable()
        self.table.pack()

    def createScheduleTable(self):
        self.table = tksheet.sheet(self.window, width = 300, height = 200)  #make size dynamic
        shiftData, columns = scheduler.getShiftsForDay(self.getDate)
        table.headers = columns
        table.set_sheet_data(shiftData)

