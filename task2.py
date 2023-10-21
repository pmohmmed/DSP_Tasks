import os
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import *
import helper_functions as hf
import task1 as t1
import numpy as np


signal = t1.SignalProcessing()
x1 = y1 = x2 = y2 = None


def on_select(event):
    selected_item = dropdown_var.get()
    label.config(text=f"You selected: {selected_item}")

    # clear
    clear_widgets()
    if(selected_item == "Addition" or selected_item == "Subtraction"):
        twofiles_frame()
    elif(selected_item == "Multiplication" or selected_item == "Shifting"):
        constant_file_frame()
    else:
        onefile_frame()

    # call Arithmatic function


def display_wave():
    selected_item = dropdown_var.get()
    # if(selected_item == 'Norma')

    x = []
    y = []
    x, y = Addition()
    x, y = Normalization()
    x, y = Subtraction()
    x, y = Multiplication()

    hf.draw(x1=x, y1=y, title=f"{selected_item} Signal", type="continuous")


def open_file(signal_number=1):

    file_path = filedialog.askopenfilename()
    if file_path:
        file_name = os.path.basename(file_path)
        file1_entry.delete(0, 'end')
        file1_entry.insert(0, file_name)
    global x1, x2, y1, y2

    if(signal_number == 1):
        x1, y1 = signal.read_signal_file(path=file_path)
    elif(signal_number == 2):
        x2, y2 = signal.read_signal_file(path=file_path)
    else:
        print("Invalid signal number")


def clear_widgets():
    constant_frame.forget()
    file1_frame.forget()
    file2_frame.forget()


def constant_file_frame():
    constant_frame.pack()
    file1_frame.pack()


def onefile_frame():
    file1_frame.pack()


def twofiles_frame():
    file1_frame.pack()
    file2_frame.pack()


def Addition():

    if (y1 is not None) and (y2 is not None):
        return x1, y1 + y2

    return None, None


def Subtraction():
    if (y1 is not None) and (y2 is not None):
        return x1, y1 - y2

    return None, None


def Multiplication():
    if (y1 is not None) and (y2 is not None):
        return x1, y1 * float(constant_entry.get())

    return None, None


def Squaring():
    # note: delete print('plapla) and return x , y
    # todo
    print('plapla')


def Shifting():
    # note: delete print('plapla) and return x , y
    # todo
    print('plapla')


def Normalization():
    choice = 0
    y = None

    if (y1 is not None):
        ymin = np.min(y1)
        ymax = np.max(y1)

        # 0 to 1
        if(choice):
            y = (y1 - ymin) / (ymax - ymin)
        # -1 to 1
        else:
            y = 2 * ((y1 - ymin) / (ymax - ymin)) - 1

    return x1, y


def Accumulation():
    # note: delete print('plapla) and return x , y
    # todo
    print('plapla')


# Create the main window
window = tk.Tk()
window.title("Dropdown List Example")
window.geometry("500x500")
# Create a label
label = tk.Label(window, text="Select an operation:", font=('Arial', 14))

label.pack(pady=10)

# Create a variable to store the selected item
dropdown_var = tk.StringVar()

# Create a dropdown list
dropdown = Combobox(window, textvariable=dropdown_var,
                    justify='center', font=('Arial', 10, 'bold'))
dropdown['values'] = ("Addition", "Subtraction", "Multiplication",
                      "Squaring", "Shifting", "Normalization", "Accumulation")
# Set the number of visible items (size)
dropdown.configure(height=5, width=30)
dropdown.pack()

# Set the initial selection
dropdown.set("")
# Bind the event to the selection
dropdown.bind("<<ComboboxSelected>>", on_select)

display_button = Button(window, text="Display",
                        command=display_wave, width=36, padding=5)
display_button.pack()

constant_frame = tk.Frame(window)
constant_label = Label(constant_frame, text="Constant:", font=('Arial', 10))
constant_entry = Entry(constant_frame, width=39)
constant_label = Label(constant_frame, text="Constant:", font=('Arial', 10))
constant_entry = Entry(constant_frame, width=39)
constant_label.pack()
constant_entry.pack()

file1_frame = tk.Frame(window)
file1_label = Label(file1_frame, text="File 1:", font=('Arial', 10))
file1_entry = tk.Entry(file1_frame)
file1_button = Button(file1_frame, text="Browse", command=lambda: open_file(1))
file1_label.grid(row=0, column=0)
file1_entry.grid(row=0, column=1)
file1_button.grid(row=0, column=2)


file2_frame = tk.Frame(window)
file2_label = Label(file2_frame, text="File 2:", font=('Arial', 10))
file2_entry = tk.Entry(file2_frame)
file2_button = Button(file2_frame, text="Browse", command=lambda: open_file(2))
file2_label.grid(row=0, column=0)
file2_entry.grid(row=0, column=1)
file2_button.grid(row=0, column=2)

# Run the main loop
window.mainloop()
