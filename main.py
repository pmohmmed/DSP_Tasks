import os
import tkinter as tk
import random
from tkinter import filedialog
from tkinter.ttk import *
import helper_functions as hf
import numpy as np
import importlib
import task2

def open_task(i=1):
    main_window.destroy()

    
    if(i == 1):
        task2.start_gui()
    elif(i == 2):
        task2.start_gui()
    


def create_task_button(N=1):
    for i in range(N):
        button = tk.Button(main_window,
                           text=f"Task{i+1}",
                           command=lambda e = i+1: open_task(e))  # button
        button.pack()
        
# Create the main main_window
main_window = None

def start_gui():
    global main_window
    main_window = tk.Tk()
    main_window.title("Main Menu")
    main_window.geometry("500x500")
    # Program icon
    icon = tk.PhotoImage(
        file='signal.png')

    main_window.iconphoto(True, icon)

    number_of_tasks = 2
    create_task_button(number_of_tasks)
    main_window.mainloop()

