import tkinter as tk
from Window import *
from ViewScheduleWindow import *

class ViewWindow(Window):
    def __init__(self, master, geometry, scheduler):
        super().__init__(master, geometry, scheduler)
        self.window.title("View Data")
        
        self.createSchedulerButton()

    def createSchedulerButton(self):
        self.scheduleButton = tk.Button(self.window, text="View Schedule", command=self.createViewScheduleWindow)
        self.scheduleButton.pack()

    def createViewScheduleWindow(self):
        viewScheduleWindow = ViewScheduleWindow(self.window, "500x300", self.scheduler)

