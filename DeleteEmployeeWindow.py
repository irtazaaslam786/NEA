import tkinter as tk
from tkinter import messagebox
from Window import *

class DeleteEmployeeWindow(Window):
    def __init__(self, master, geometry, scheduler):
        super().__init__(master, geometry, scheduler)
        self.window.title("Delete Shift")

        self.DeleteEmployeeWidget()
        self.submitDataButton()

    def DeleteEmployeeWidget(self):
        self.employeeIdLabel = tk.Label(self.window, text="Employee ID:")
        self.employeeIdLabel.grid(row = 0, column = 0)
        self.employeeIdEntry = tk.Entry(self.window)
        self.employeeIdEntry.grid(row = 0, column = 1)

    def submitDataButton(self):
        self.submitDataButton = tk.Button(self.window, text="Submit Data", command=self.getData)
        self.submitDataButton.grid(row = 1, column = 0)

    def getData(self):
        employeeID = self.employeeIdEntry.get()
        successful = self.scheduler.deleteEmployee(employeeID)
        if not successful:
            messagebox.showinfo("Invalid Data", "Please check your input, you have entered invalid data!")
        else:
            self.employeeIdEntry.delete(0, 'end')