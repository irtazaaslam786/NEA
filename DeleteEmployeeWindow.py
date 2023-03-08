import tkinter as tk
from tkinter import messagebox
from Window import *

class DeleteEmployeeWindow(Window):
    def __init__(self, master, geometry, scheduler):
        super().__init__(master, geometry, scheduler)
        self.window.title("Delete Employee")

        self.DeleteFirstNameWidget()
        self.DeleteSurNameWidget()
        self.DeleteDepartmentWidget()
        self.submitDataButton()

    def DeleteFirstNameWidget(self):
        self.FirstNameLabel = tk.Label(self.window, text="Firstname:")
        self.FirstNameLabel.grid(row = 0, column = 0)
        self.FirstNameEntry = tk.Entry(self.window)
        self.FirstNameEntry.grid(row = 0, column = 1)

    def DeleteSurNameWidget(self):
        self.SurNameLabel = tk.Label(self.window, text="Surname:")
        self.SurNameLabel.grid(row = 1, column = 0)
        self.SurNameEntry = tk.Entry(self.window)
        self.SurNameEntry.grid(row = 1, column = 1)

    def DeleteDepartmentWidget(self):
        self.DepartmentLabel = tk.Label(self.window, text="Department:")
        self.DepartmentLabel.grid(row = 2, column = 0)
        self.DepartmentEntry = tk.Entry(self.window)
        self.DepartmentEntry.grid(row = 2, column = 1)

    def submitDataButton(self):
        self.submitDataButton = tk.Button(self.window, text="Submit Data", command=self.getData)
        self.submitDataButton.grid(row = 3, column = 1)

    def getData(self):
        firstname = self.FirstNameEntry.get()
        surname = self.SurNameEntry.get()
        department = self.DepartmentEntry.get()
        successful = self.scheduler.deleteEmployee(firstname, surname, department)
        if not successful:
            messagebox.showinfo("Invalid Data", "Please check your input, you have entered invalid data!")
        else:
            self.FirstNameEntry.delete(0, 'end')
            self.SurNameEntry.delete(0, 'end')
            self.DepartmentEntry.delete(0, 'end')

