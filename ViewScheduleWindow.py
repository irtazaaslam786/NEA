import tkinter as tk
import tksheet

from Window import *

class ViewScheduleWindow(Window):
    def __init__(self, master, geometry, scheduler):
        super().__init__(master, geometry, scheduler)
        self.window.title("View Schedule")

        self.createScheduleTable()
        self.table.pack()
        print(self.getDate())

    def createScheduleTable(self):
        self.table = tksheet.Sheet(self.window, width = 300, height = 200)  #make size dynamic
        shiftData, columns = self.scheduler.getShiftsForDay(self.getDate())
        self.table.headers = columns
        self.table.set_sheet_data(shiftData)

