import tkinter as tk
from Window import *

class AddEmployeeWindow(Window):
    def __init__(self, master, geometry, scheduler):
        super().__init__(master, geometry, scheduler)
        self.window.title("Add Employee")

        self.addFirstNameWidgets()
        self.addSurnameWidgets()
        self.addAgeWidgets()
        self.addDepartmentWidgets()

    def addFirstNameWidgets(self):
        self.firstNameLabel = tk.Label(self.window, text="First name:").grid(row = 0, column = 0)
        self.firstNameEntry = tk.Entry(self.window).grid(row = 0, column = 1)

    def addSurnameWidgets(self):
        self.surNameLabel = tk.Label(self.window, text="Surname:").grid(row = 1, column = 0)
        self.surNameEntry = tk.Entry(self.window).grid(row = 1, column = 1)

    def addAgeWidgets(self):
        self.ageLabel = tk.Label(self.window, text="Age:").grid(row = 2, column = 0)
        self.ageEntry = tk.Entry(self.window).grid(row = 2, column = 1)

    def addDepartmentWidgets(self): #make dropdown box
        self.departmentLabel = tk.Label(self.window, text="Department:").grid(row = 3, column = 0)
        self.departmentEntry = tk.Entry(self.window).grid(row = 3, column = 1)
