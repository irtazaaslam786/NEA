import tkinter as tk
from tkinter import messagebox
from Window import *

class DeleteShiftWindow(Window):
    def __init__(self, master, geometry, scheduler):
        super().__init__(master, geometry, scheduler)
        self.window.title("Delete Shift")

        self.DeleteShiftWidget()
        self.submitDataButton()

    def DeleteShiftWidget(self):
        self.ShiftIdLabel = tk.Label(self.window, text="Shift Id:")
        self.ShiftIdLabel.grid(row = 0, column = 0)
        self.ShiftIdEntry = tk.Entry(self.window)
        self.ShiftIdEntry.grid(row = 0, column = 1)

    def submitDataButton(self):
        self.submitDataButton = tk.Button(self.window, text="Submit Data", command=self.getData)
        self.submitDataButton.grid(row = 1, column = 0)

    def getData(self):
        shiftID = self.ShiftIdEntry.get()
        successfulDeletion = self.scheduler.deleteShift(shiftID)
        if not successfulDeletion:
            messagebox.showinfo("Invalid Data", "Please check your input, you have entered invalid data!")
        else:
            self.ShiftIdEntry.delete(0, 'end')
