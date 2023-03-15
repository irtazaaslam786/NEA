import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry

from Window import *

class AddHolidayWindow(Window):
    def __init__(self, master, geometry, scheduler):
        super().__init__(master, geometry, scheduler)
        self.window.title("Add Holiday")

        self.addEmployeeIDWidgets()
        self.addStartDateWidgets()
        self.addEndDateWidgets()
        self.submitDataButton()

        self.QuitButton.grid(row = 4, column = 0)

    def addEmployeeIDWidgets(self):
        self.employeeIDLabel = tk.Label(self.window, text="Employee ID:")
        self.employeeIDLabel.grid(row = 0, column = 0)
        self.employeeIDEntry = tk.Entry(self.window)
        self.employeeIDEntry.grid(row = 0, column = 1)

    def addStartDateWidgets(self):
        self.startDateLabel = tk.Label(self.window, text="Start date:")
        self.startDateLabel.grid(row = 1, column = 0)
        self.startDatePicker = Calendar(self.window, selectmode = 'day', year = 2023, month = 3)
        self.startDatePicker.grid(row = 1, column = 1)

    def addEndDateWidgets(self):
        self.endDateLabel = tk.Label(self.window, text="End date:")
        self.endDateLabel.grid(row = 2, column = 0)
        self.endDateEntry = tk.Entry(self.window)
        self.endDateEntry.grid(row = 2, column = 1)

    def submitDataButton(self):
        self.submitDataButton = tk.Button(self.window, text="Submit Data", command=self.getData)
        self.submitDataButton.grid(row = 3, column = 0)

    def getData(self):
        employeeID = self.employeeIDEntry.get()
        startDate = self.startDateEntry.get()
        endDate = self.endDateEntry.get()

        successfulEntry = self.scheduler.addHoliday(employeeID, startDate, endDate)
        if not successfulEntry:
            messagebox.showinfo("Invalid Data", "Please check your input, you have entered invalid data")
        else:
            self.employeeIDEntry.delete(0, 'end')
            self.startDateEntry.delete(0, 'end')
            self.endDateEntry.delete(0, 'end')
