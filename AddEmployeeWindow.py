import tkinter as tk
from tkinter import messagebox
from Window import *

class AddEmployeeWindow(Window):
    def __init__(self, master, geometry, scheduler):
        super().__init__(master, geometry, scheduler)
        self.window.title("Add Employee")

        self.addFirstNameWidgets()
        self.addSurnameWidgets()
        self.addAgeWidgets()
        self.addDepartmentWidgets()
        self.submitDataButton()

    def addFirstNameWidgets(self):
        self.firstNameLabel = tk.Label(self.window, text="First name:")
        self.firstNameLabel.grid(row = 0, column = 0)
        self.firstNameEntry = tk.Entry(self.window)
        self.firstNameEntry.grid(row = 0, column = 1)

    def addSurnameWidgets(self):
        self.surNameLabel = tk.Label(self.window, text="Surname:")
        self.surNameLabel.grid(row = 1, column = 0)
        self.surNameEntry = tk.Entry(self.window)
        self.surNameEntry.grid(row = 1, column = 1)

    def addAgeWidgets(self):
        self.ageLabel = tk.Label(self.window, text="Age:")
        self.ageLabel.grid(row = 2, column = 0)
        self.ageEntry = tk.Entry(self.window)
        self.ageEntry.grid(row = 2, column = 1)

    def addDepartmentWidgets(self): #TODO: make dropdown box
        self.departmentLabel = tk.Label(self.window, text="Department:")
        self.departmentLabel.grid(row = 3, column = 0)
        self.departmentEntry = tk.Entry(self.window)
        self.departmentEntry.grid(row = 3, column = 1)

    def submitDataButton(self):
        self.submitDataButton = tk.Button(self.window, text="Submit Data", command=self.getData)
        self.submitDataButton.grid(row = 4, column = 0)

    def getData(self):
        try:
            age = int(self.ageEntry.get())
        except:
            messagebox.showinfo("Invalid Data", "Please check your input, you have entered invalid data!")
            return
        
        firstName = self.firstNameEntry.get()
        surName = self.surNameEntry.get()
        department = self.departmentEntry.get()
        
        successfulEntry = self.scheduler.addEmployee(firstName, surName, age, department)
        if not successfulEntry:
            messagebox.showinfo("Invalid Data", "Please check your input, you have entered invalid data!")
        else:
            self.firstNameEntry.delete(0, 'end')
            self.surNameEntry.delete(0, 'end')
            self.ageEntry.delete(0, 'end')
            self.departmentEntry.delete(0, 'end')
