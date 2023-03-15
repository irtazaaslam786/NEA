import tkinter as tk
import tksheet

from Window import *

class ViewEmployeesWindow(Window):
    def __init__(self, master, geometry, scheduler):
        super().__init__(master, geometry, scheduler)
        self.window.title("View Employees")

        self.createEmployeesTable()
        self.table.pack()

        self.QuitButton.pack()

    def createEmployeesTable(self):
        self.table = tksheet.Sheet(self.window, width = 300, height = 200)  #make dimensions dynamic
        employeeData, columns = self.scheduler.getEmployeeData()
        self.table.headers(columns)
        self.table.set_sheet_data(employeeData)
