import tkinter as tk

from Window import *
from ViewScheduleWindow import *
from ViewEmployeesWindow import *
from ViewHolidaysWindow import *

class ViewWindow(Window):
    def __init__(self, master, geometry, scheduler):
        super().__init__(master, geometry, scheduler)
        self.window.title("View Data")
        
        self.createSchedulerButton()
        self.createEmployeesButton()
        self.createHolidayButton()

        self.QuitButton.pack()

    def createSchedulerButton(self):
        self.scheduleButton = tk.Button(self.window, text="View Schedule", command=self.createViewScheduleWindow)
        self.scheduleButton.pack()

    def createViewScheduleWindow(self):
        viewScheduleWindow = ViewScheduleWindow(self.window, self.geometry, self.scheduler)

    def createEmployeesButton(self):
        self.employeesButton = tk.Button(self.window, text="View Employees", command=self.createViewEmployeesWindow)
        self.employeesButton.pack()

    def createHolidayButton(self):
        self.holidayButton = tk.Button(self.window, text="View Holidays", command=self.createViewHolidayWindow)
        self.holidayButton.pack()

    def createViewHolidayWindow(self):
        viewHolidayWindow = ViewHolidaysWindow(self.window, self.geometry, self.scheduler)

    def createViewEmployeesWindow(self):
        viewEmployeesWindow = ViewEmployeesWindow(self.window, self.geometry, self.scheduler)
