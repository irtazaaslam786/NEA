import tkinter as tk
from Window import *

class ViewWindow(Window):
    def __init__(self, master, geometry, scheduler):
        super().__init__(master, geometry, scheduler)
        self.window.title("View Data")

    def createSchedulerButton(self):
        createScheduleButton = tk.Button(text="View Schedule", command=self.createViewScheduleWindow)

    def createViewScheduleWindow(self):
        viewScheduleWindow = ViewScheduleWindow(self.window, "500x300")


