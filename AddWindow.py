import tkinter as tk
from Window import *
from AddEmployeeWindow import *
from AddShiftWindow import *
from AddHolidayWindow import *

class AddWindow(Window):
    def __init__(self, master, geometry, scheduler):
        super().__init__(master, geometry, scheduler)
        self.window.title("Add Data")

        self.createAddEmployeeButton()
        self.createAddShiftButton()
        self.createAddHolidayButton()

    def createAddEmployeeButton(self):
        self.employeeButton = tk.Button(self.window, text="Add Employee", command=self.createAddEmployeeWindow)
        self.employeeButton.pack()

    def createAddShiftButton(self):
        self.shiftButton = tk.Button(self.window, text="Add Shift", command=self.createAddShiftWindow)
        self.shiftButton.pack()

    def createAddHolidayButton(self):
        self.holidayButton = tk.Button(self.window, text="Add Holiday", command=self.createAddHolidayWindow)
        self.holidayButton.pack()

    def createAddEmployeeWindow(self):
        self.addEmployeeWindow = AddEmployeeWindow(self.window, "500x300", self.scheduler)

    def createAddShiftWindow(self):
        self.addShiftWindow = AddShiftWindow(self.window, "500x300", self.scheduler)

    def createAddHolidayWindow(self):
        self.addHolidayWindow = AddHolidayWindow(self.window, "500x300", self.scheduler)
