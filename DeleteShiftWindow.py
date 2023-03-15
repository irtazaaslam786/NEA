import tkinter as tk
from tkinter import messagebox
from Window import *


class DeleteShiftWindow(Window):
    def __init__(self, master, geometry, scheduler):
        super().__init__(master, geometry, scheduler)
        self.window.title("Delete Shift")

        self.DeleteFirstNameWidget()
        self.DeleteSurNameWidget()
        self.DeleteStartTimeWidget()
        self.DeleteEndTimeWidget()
        self.CreateSubmitDataButton()

        self.QuitButton.grid(row = 5, column = 0)

    def DeleteFirstNameWidget(self):
        self.FirstNameLabel = tk.Label(self.window, text="First Name :")
        self.FirstNameLabel.grid(row=0, column=0)
        self.FirstNameEntry = tk.Entry(self.window)
        self.FirstNameEntry.grid(row=0, column=1)

    def DeleteSurNameWidget(self):
        self.SurNameLabel = tk.Label(self.window, text="Surname:")
        self.SurNameLabel.grid(row=1, column=0)
        self.SurNameEntry = tk.Entry(self.window)
        self.SurNameEntry.grid(row=1, column=1)

    def DeleteStartTimeWidget(self):
        self.StartTimeLabel = tk.Label(self.window, text="StartTime:")
        self.StartTimeLabel.grid(row=2, column=0)
        self.StartTimeEntry = tk.Entry(self.window)
        self.StartTimeEntry.grid(row=2, column=1)

    def DeleteEndTimeWidget(self):
        self.EndTimeLabel = tk.Label(self.window, text="End Time:")
        self.EndTimeLabel.grid(row=3, column=0)
        self.EndTimeEntry = tk.Entry(self.window)
        self.EndTimeEntry.grid(row=3, column=1)

    def CreateSubmitDataButton(self):
        self.submitDataButton = tk.Button(self.window, text="Submit Data", command=self.getData)
        self.submitDataButton.grid(row=4, column=0)

    def getData(self):
        firstname = self.FirstNameEntry.get()
        surname = self.SurNameEntry.get()
        starttime = self.StartTimeEntry.get()
        endtime = self.EndTimeEntry.get()

        successfulDeletion = self.scheduler.deleteShift(firstname, surname, starttime, endtime)
        if not successfulDeletion:
            messagebox.showinfo("Invalid Data", "Please check your input, you have entered invalid data!")
        else:
            self.FirstNameEntry.delete(0, 'end')
            self.SurNameEntry.delete(0, 'end')
            self.StartTimeEntry.delete(0, 'end')
            self.EndTimeEntry.delete(0, 'end')
