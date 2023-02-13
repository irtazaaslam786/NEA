import tkinter as tk
from Window import *

class DeleteWindow(Window):
    def __init__(self, master, geometry, scheduler):
        super().__init__(master, geometry, scheduler)
        self.window.title("Delete Employees")
