import os
import tkinter as tk
import random
from tkinter import filedialog
from tkinter.ttk import *
import helper_functions as hf
import task1 as t1
import numpy as np

signal = t1.SignalProcessing()


def open_file():
    print("not completed")


window = tk.Tk()
window.title("Quntization")
window.geometry("500x500")
# Program icon
icon = tk.PhotoImage(
    file='signal.png')

window.iconphoto(True, icon)


# choice
# 0 : bits
# 1 : levels

normalization_choice = tk.IntVar()
normalization_choice.set(0)  # Default selection

bit_radio = tk.Radiobutton(
    window, text="Bits",
    variable=normalization_choice, value=0, padx=9)
# choice 2
level_radio = tk.Radiobutton(
    window, text="Levels",
    variable=normalization_choice, value=1)

# display
bit_radio.pack()
level_radio.pack()

num_frame = tk.Frame(window)
# number of levels/bits
num_label = tk.Label(num_frame, text="#:", font=('Arial', 15))
num_entry = tk.Entry(num_frame, width=36)


label = tk.Label(num_frame,
                 text=f"File:",
                 font=('Arial', 15))  # label
entry = tk.Entry(num_frame, width=36)  # entry
button = tk.Button(num_frame,
                   text="Browse",
                   command=open_file)  # button

# display
num_label.grid(row=0, column=0)
num_entry.grid(row=0, column=1)


label.grid(row=1, column=0, padx=5)
entry.grid(row=1, column=1, padx=5)
button.grid(row=1, column=2)

# display frame
num_frame.pack()


# ================= Display Button ==================

display_button = Button(window, text="Display",
                        command=window, width=36, padding=5)  # button
# display
display_button.pack()


# Run the main loop
window.mainloop()
