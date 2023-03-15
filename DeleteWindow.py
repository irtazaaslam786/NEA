import tkinter as tk
from Window import *
from DeleteShiftWindow import *
from DeleteEmployeeWindow import *
from DeleteHolidayWindow import *

class DeleteWindow(Window):
    def __init__(self, master, geometry, scheduler):
        super().__init__(master, geometry, scheduler)
        self.window.title("Delete Employees")

        self.createDeleteEmployeeButton()
        self.createDeleteShiftButton()
        self.createDeleteHolidayButton()

        self.QuitButton.pack()

    def createDeleteEmployeeButton(self):
        self.employeeButton = tk.Button(self.window, text="Delete Employee", command=self.createDeleteEmployeeWindow)
        self.employeeButton.pack()

    def createDeleteShiftButton(self):
        self.shiftButton = tk.Button(self.window, text="Delete Shift", command=self.createDeleteShiftWindow)
        self.shiftButton.pack()

    def createDeleteHolidayButton(self):
        self.holidayButton = tk.Button(self.window, text="Delete Holiday", command=self.createDeleteHolidayWindow)
        self.holidayButton.pack()

    def createDeleteEmployeeWindow(self):
        self.DeleteEmployeeWindow = DeleteEmployeeWindow(self.window, "500x300", self.scheduler)

    def createDeleteShiftWindow(self):
        self.DeleteShiftWindow = DeleteShiftWindow(self.window, "500x300", self.scheduler)

    def createDeleteHolidayWindow(self):
        self.DeleteHolidayWindow = DeleteHolidayWindow(self.window, "500x300", self.scheduler)
