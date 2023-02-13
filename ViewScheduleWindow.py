import tkinter as tk
import tksheet
from datetime import datetime

from Window import *

class ViewScheduleWindow(Window):
    def __init__(self, master, geometry, scheduler):
        super().__init(master, geometry)
        self.window.title("View Schedule")
        self.scheduler = scheduler

        self.createScheduleTable()
        self.table.pack()

    def getDate(self):
        return datetime.today().strftime('%d:%m:%Y')

    def createScheduleTable(self):
        self.table = tksheet.sheet(self.window, width = 300, height = 200)  #make size dynamic
        shiftData, columns = scheduler.getShiftsForDay(self.getDate)
        table.headers = columns
        table.set_sheet_data(shiftData)

