import tkinter as tk
import tksheet
from Window import *

class ViewHolidaysWindow(Window):
    def __init__(self, master, geometry, scheduler):
        super().__init__(master, geometry, scheduler)
        self.window.title("View Holidays")

        self.createHolidaysTable()
        self.table.pack()

        self.QuitButton.pack()

    def createHolidaysTable(self):
        self.table = tksheet.Sheet(self.window, width = 300, height = 200)  #make dimensions dynamic
        holidayData, columns = self.scheduler.getHolidays()
        self.table.headers(columns)
        self.table.set_sheet_data(holidayData)
