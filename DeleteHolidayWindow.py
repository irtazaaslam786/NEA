import tkinter as tk
from tkinter import messagebox
from DeleteWindow import *

class DeleteHolidayWindow(Window):
    def __init__(self, master, geometry, scheduler):
        super().__init__(master, geometry, scheduler)
        self.window.title("Delete Holiday")

        self.DeleteFirstNameWidget()
        self.DeleteSurNameWidget()
        self.DeleteStartDateWidget()
        self.CreateSubmitDataButton()

        self.QuitButton.grid(row = 4, column = 0)

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

    def DeleteStartDateWidget(self):
        self.StartDateLabel = tk.Label(self.window, text="StartDate:")
        self.StartDateLabel.grid(row = 2, column = 0)
        self.StartDateEntry = tk.Entry(self.window)
        self.StartDateEntry.grid(row = 2, column = 1)

    def CreateSubmitDataButton(self):
        self.submitDataButton = tk.Button(self.window, text="Submit Data", command=self.getData)
        self.submitDataButton.grid(row = 3, column = 0)

    def getData(self):
        firstname = self.FirstNameEntry.get()
        surname = self.SurNameEntry.get()
        startdate = self.StartDateEntry.get()
        successful = self.scheduler.deleteEmployee(firstname, surname, startdate)
        if not successful:
            messagebox.showinfo("Invalid Data", "Please check your input, you have entered invalid data!")
        else:
            self.FirstNameEntry.delete(0, 'end')
            self.SurNameEntry.delete(0, 'end')
            self.StartDateEntry.delete(0, 'end')