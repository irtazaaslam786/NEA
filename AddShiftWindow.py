import tkinter as tk
from tkinter import messagebox
from Window import *

class AddShiftWindow(Window):
    def __init__(self, master, geometry, scheduler):
        super().__init__(master, geometry, scheduler)
        self.window.title("Add Schedule")

        self.addEmployeeIdWidget()
        self.addStartTimeWidget()
        self.addEndTimeWidget()
        self.addDateWidget()
        self.addBreakTimeWidget()
        self.submitDataButton()

        self.QuitButton.grid(row = 6, column = 0)
        
    def addEmployeeIdWidget(self):
        self.EmployeeIdLabel = tk.Label(self.window, text="Employee Id:")
        self.EmployeeIdLabel.grid(row = 0, column = 0)
        self.EmployeeIdEntry = tk.Entry(self.window)
        self.EmployeeIdEntry.grid(row = 0, column = 1)

    def addStartTimeWidget(self):
        self.StartTimeLabel = tk.Label(self.window, text="Start Time:")
        self.StartTimeLabel.grid(row = 1, column = 0)
        self.StartTimeEntry = tk.Entry(self.window)
        self.StartTimeEntry.grid(row = 1, column = 1)

    def addEndTimeWidget(self):
        self.EndTimeLabel = tk.Label(self.window, text="End Time:")
        self.EndTimeLabel.grid(row = 2, column = 0)
        self.EndTimeEntry = tk.Entry(self.window)
        self.EndTimeEntry.grid(row = 2, column = 1)

    def addDateWidget(self):
        self.DateLabel = tk.Label(self.window, text="Date:")
        self.DateLabel.grid(row = 3, column = 0)
        self.DateEntry = tk.Entry(self.window)
        self.DateEntry.grid(row = 3, column = 1)

    def addBreakTimeWidget(self):
        self.BreakTimeLabel = tk.Label(self.window, text="Break Time:")
        self.BreakTimeLabel.grid(row = 4, column = 0)
        self.BreakTimeEntry = tk.Entry(self.window)
        self.BreakTimeEntry.grid(row = 4, column = 1)

    def submitDataButton(self):
        self.submitDataButton = tk.Button(self.window, text="Submit Data", command=self.getData)
        self.submitDataButton.grid(row = 5, column = 0)

    def getData(self):
        employeeID = self.EmployeeIdEntry.get()
        startTime = self.StartTimeEntry.get()
        endTime = self.EndTimeEntry.get()
        date = self.DateEntry.get()
        breakTime = self.BreakTimeEntry.get()
        
        successfulEntry = self.scheduler.addShift(employeeID, startTime, endTime, date, breakTime)
        if not successfulEntry:
            messagebox.showinfo("Invalid Data", "Please check your input, you have entered invalid data!")
        else:
            self.EmployeeIdEntry.delete(0, 'end')
            self.StartTimeEntry.delete(0, 'end')
            self.EndTimeEntry.delete(0, 'end')
            self.DateEntry.delete(0, 'end')
            self.BreakTimeEntry.delete(0, 'end')




