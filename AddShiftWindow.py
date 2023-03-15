import tkinter as tk
from tkinter import messagebox
from Window import *
from tkcalendar import Calendar
from tktimepicker import AnalogPicker, AnalogThemes


class AddShiftWindow(Window):
    def __init__(self, master, geometry, scheduler):
        super().__init__(master, geometry, scheduler)
        self.window.title("Add Schedule")

        self.addEmployeeIdWidget()
        self.addStartTimeWidget()
        self.addEndTimeWidget()
        self.addBreakTimeWidget()
        self.addDateWidget()
        self.CreateSubmitDataButton()

        self.QuitButton.grid(row=6, column=0)

    def addEmployeeIdWidget(self):
        self.EmployeeIdLabel = tk.Label(self.window, text="Employee Id:")
        self.EmployeeIdLabel.grid(row=0, column=0)
        self.EmployeeIdEntry = tk.Entry(self.window)
        self.EmployeeIdEntry.grid(row=0, column=1)

    def addStartTimeWidget(self):
        self.StartTimeLabel = tk.Label(self.window, text="Start Time:")
        self.StartTimeLabel.grid(row=1, column=0)
        self.StartTimePicker = AnalogPicker(self.window)
        theme = AnalogThemes(self.StartTimePicker)
        theme.setDracula()
        self.StartTimePicker.grid(row=1, column=1)

    def addEndTimeWidget(self):
        self.EndTimeLabel = tk.Label(self.window, text="End Time:")
        self.EndTimeLabel.grid(row=2, column=0)
        self.EndTimeEntry = tk.Entry(self.window)
        self.EndTimeEntry.grid(row=2, column=1)

    def addDateWidget(self):
        self.DateLabel = tk.Label(self.window, text="Date:")
        self.DateLabel.grid(row=3, column=0)
        self.DatePicker = Calendar(self.window, selectmode='day', year=2023, month=3, date_pattern="dd/mm/yyyy")
        self.DatePicker.grid(row=3, column=1)

    def addBreakTimeWidget(self):
        self.BreakTimeLabel = tk.Label(self.window, text="Break Time:")
        self.BreakTimeLabel.grid(row=4, column=0)
        self.BreakTimeEntry = tk.Entry(self.window)
        self.BreakTimeEntry.grid(row=4, column=1)

    def CreateSubmitDataButton(self):
        self.submitDataButton = tk.Button(self.window, text="Submit Data", command=self.getData)
        self.submitDataButton.grid(row=5, column=0)

    def formatTime(self, hours, minutes, period):
        if period == 'PM':
            hours += 12
        elif hours < 10:
            return '0' + str(hours) + ":" + str(minutes)
        return str(hours) + ":" + str(minutes)

    def getData(self):
        minutes = self.StartTimePicker.minutes()
        hours = self.StartTimePicker.hours()
        period = self.StartTimePicker.period()
        print(self.formatTime(hours, minutes, period))
        '''
        employeeID = self.EmployeeIdEntry.get()
        startTime = 0
        endTime = self.EndTimeEntry.get()
        date = self.DatePicker.get_date()
        breakTime = self.BreakTimeEntry.get()

        successfulEntry = self.scheduler.addShift(employeeID, startTime, endTime, date, breakTime)
        if not successfulEntry:
            messagebox.showinfo("Invalid Data", "Please check your input, you have entered invalid data!")
        else:
            self.EmployeeIdEntry.delete(0, 'end')
            self.StartTimeEntry.delete(0, 'end')
            self.EndTimeEntry.delete(0, 'end')
            self.BreakTimeEntry.delete(0, 'end')'''




