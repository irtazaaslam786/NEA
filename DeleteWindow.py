import tkinter as tk
from Window import *

class DeleteWindow(Window):
    def __init__(self, master, geometry):
        super().__init__(master, geometry)
        self.window.title("Delete Employees")
