import os
import tkinter as tk
import random
from tkinter import filedialog
from tkinter.ttk import *
import helper_functions as hf
import numpy as np

def import_file(n=1):
    import importlib
    package_name = f"task{n}"
    try:
        # Use import_module to import the package specified by the string
        imported_package = importlib.import_module(package_name)

        # Now, you can use the package as you would with a regular import statement
        # print(imported_package._version_)  # Access an attribute of the package (e.g., version)
    except ImportError:
        print(f"Failed to import the package '{package_name}'.")

def create_task_button(N=1):
    for i in range(N):
        button = tk.Button(main_window,
                           text=f"Task{i+1}",
                           command=lambda e=i+1: import_file(e))  # button
        button.grid(row=i, column=0)



# Create the main main_window
main_window = tk.Tk()
main_window.title("Main Menu")
main_window.geometry("500x500")
# Program icon
icon = tk.PhotoImage(
    file='signal.png')

main_window.iconphoto(True, icon)

number_of_tasks = 3
create_task_button(number_of_tasks)
main_window.mainloop()


