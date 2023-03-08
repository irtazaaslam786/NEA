import tkinter as tk
from tkinter import messagebox
from Window import *

class DeleteHolidayWindow(Window):
    def __init__(self, master, geometry, scheduler):
        super().__init__(master, geometry, scheduler)
        self.window.title("Delete Holiday")

        self.DeleteHolidayIDWidgets()
        self.submitDataButton()

    def DeleteHolidayIDWidgets(self):
        self.holidayIDLabel = tk.Label(self.window, text="Holiday ID:")
        self.holidayIDLabel.grid(row = 0, column = 0)
        self.holidayIDEntry = tk.Entry(self.window)
        self.holidayIDEntry.grid(row = 0, column = 1)

    def submitDataButton(self):
        self.submitDataButton = tk.Button(self.window, text="Submit Data", command=self.getData)
        self.submitDataButton.grid(row = 1, column = 0)

    def getData(self):
        employeeID = self.employeeIDEntry.get()
        startDate = self.startDateEntry.get()
        endDate = self.endDateEntry.get()

        successful = self.scheduler.deleteHoliday()
        if not successful:
            messagebox.showinfo("Invalid Data", "Please check your input, you have entered invalid data")
        else:
            self.holidayIDEntry.delete(0, 'end')

