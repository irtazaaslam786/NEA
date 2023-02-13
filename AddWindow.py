import tkinter as tk
from Window import *

class AddWindow(Window):
    def __init__(self, master, geometry):
        super().__init__(master, geometry)
        self.window.title("Add Data")

