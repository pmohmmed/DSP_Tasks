import os
import tkinter as tk
import random
from tkinter import filedialog
from tkinter.ttk import *
import helper_functions as hf
import numpy as np

import main

# total files
# list of lists ex: x[[file1], [file2], [file3]]
x = None
y = None


def on_select(event):
    selected_item = dropdown_var.get()
    label.config(text=f"You selected: {selected_item}")

    # clear
    clear_widgets()
    if(selected_item == "Addition" or selected_item == "Subtraction"):
        num_frame.pack()
    elif(selected_item == "Multiplication" or selected_item == "Shifting"):
        constant_file_frame()
    elif(selected_item == "Normalization"):
        normalization_rad_frame()
    else:
        onefile_frame()

    # call Arithmatic function


def display_wave():

    selected_item = dropdown_var.get()

    x = []
    y = []

    if selected_item in globals() and callable(globals()[selected_item]):
        # Call the function using the string name
        x, y = globals()[selected_item]()
    else:
        print("Function not found or not callable")

    num_samples = 10
    # Sample 10 random values from x and y
    if ((x is None and y is None) or (len(x) == 0 and len(y) == 0) or selected_item == "Squaring" or selected_item == "Accumulation"):
        x_samples = x
        y_samples = y
    else:
        sample_indices = random.sample(range(len(x)), num_samples)
        x_samples = [x[i] for i in sample_indices]
        y_samples = [y[i] for i in sample_indices]

    hf.draw(x1=x_samples, y1=y_samples,
            title=f"{selected_item} Signal", type="both")


def open_file(entry):

    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    file_name = os.path.basename(file_path)

    global x, y
    xi, yi = hf.read_signal_file(path=file_path)
    x.append(xi)
    y.append(yi)
    entry.delete(0, 'end')
    entry.insert(0, file_name)


def create_signal_inputs(N=1):
    # clear x and y
    global x, y
    x = []
    y = []

    # Clear existing signal frames and widgets
    for widget in signal_files_frame.winfo_children():
        widget.destroy()

    # Generate signal input fields

    for i in range(N):

        label = tk.Label(signal_files_frame,
                         text=f"File {i+1}:",
                         font=('Arial', 10))  # label
        entry = tk.Entry(signal_files_frame)  # entry
        button = tk.Button(signal_files_frame,
                           text="Browse",
                           command=lambda e=entry: open_file(e))  # button

        # display
        label.grid(row=i, column=0)
        entry.grid(row=i, column=1)
        button.grid(row=i, column=2)

    # display frame
    signal_files_frame.pack()


def clear_widgets():
    constant_frame.forget()
    normalization_frame.forget()
    signal_files_frame.forget()
    num_frame.forget()


def normalization_rad_frame():
    normalization_frame.pack()
    create_signal_inputs(1)


def constant_file_frame():
    constant_frame.pack()
    create_signal_inputs(1)


def onefile_frame():
    create_signal_inputs(1)


def cast_to_float(value):
    try:
        float(value)
        return float(value)
    except ValueError:
        return 0


def Addition():

    y_ = None
    flag = True
    length = 0

    if (y is None) or (y == []):
        return None, None

    length = len(y)
    for i in range(length):

        if (y[i] is not None):
            if(flag):
                # initialize the y_ with first signal
                y_ = y[i]
                flag = False
                continue

            y_ += y[i]

    hf.write_file(
        file_name="output.txt",
        N=hf.N, x=x[0].astype(int), y=y_.astype(int)
    )

    return x[0], y_


def Subtraction():

    y_ = None
    flag = True
    length = 0
    if (y is None) or (y == []):
        return None, None

    length = len(y)

    for i in range(length):

        if (y[i] is not None):
            if(flag):
                # initialize the y_ with first signal
                y_ = y[i]
                flag = False
                continue

            y_ -= y[i]

    hf.write_file(
        file_name="output.txt",
        N=hf.N, x=x[0].astype(int), y=y_.astype(int)
    )
    return x[0], y_


def Multiplication():
    constant = cast_to_float(constant_entry.get())
    y_ = None
    if (y is None) or (y == []):
        return None, None

    y_ = y[0] * constant

    hf.write_file(
        "output.txt", hf.signalType,
        hf.isPeriodic,
        hf.N, x[0].astype(int), y_.astype(int)
    )

    return x[0], y_


def Squaring():
    y_ = None
    if (y is None) or (y == []):
        return None, None

    y_ = np.power(y[0], 2)

    hf.write_file(
        "output.txt", hf.signalType,
        hf.isPeriodic,
        hf.N, x[0].astype(int), y_.astype(int)
    )

    return x[0], y_


def Shifting():

    x_ = None
    constant = cast_to_float(constant_entry.get()) * -1

    if (y is None) or (y == []):
        return None, None

    x_ = x[0] + constant

    hf.write_file(
        "output.txt", hf.signalType,
        hf.isPeriodic,
        hf.N, x_.astype(int), y[0].astype(int)
    )
    return x_, y[0]


def Normalization():

    y_ = None

    if (x is None) or (x == []):
        return None, None

    ymin = np.min(y[0])
    ymax = np.max(y[0])

    # 0 to 1
    if(normalization_choice.get() == 'option1'):
        y_ = (y[0] - ymin) / (ymax - ymin)
    # -1 to 1
    else:
        y_ = 2 * ((y[0] - ymin) / (ymax - ymin)) - 1
    hf.write_file(
        "output.txt", hf.signalType,
        hf.isPeriodic,
        hf.N, x[0].astype(int), y_
    )
    return x[0], y_


def Accumulation():
    if (y is None) or (y == []):
        return None, None
    y_ = np.add.accumulate(y[0]).astype(int)

    hf.write_file(
        "output.txt", hf.signalType,
        hf.isPeriodic,
        hf.N, x[0].astype(int), y_.astype(int)
    )
    return x[0], y_


# Create the main window
window = tk.Tk()
window.title("Calculating by operations")
window.geometry("500x500")
# Program icon
icon = tk.PhotoImage(
    file='signal.png')

window.iconphoto(True, icon)

# ============= Signal file ============
# frame contain : label, entry, button
# signal frames
signal_files_frame = tk.Frame(window)


# ============================= Start the selection ======================
label = tk.Label(window, text="Select an operation:",
                 font=('Arial', 14))  # label


# choice
dropdown_var = tk.StringVar()

# drop down list
dropdown = Combobox(window,
                    textvariable=dropdown_var,
                    justify='center',
                    font=('Arial', 10, 'bold'))
# list
dropdown['values'] = ("Addition",
                      "Subtraction",
                      "Multiplication",
                      "Squaring",
                      "Shifting",
                      "Normalization",
                      "Accumulation")


# conf
dropdown.configure(height=5, width=30)
# initinal
dropdown.set("")

# display
label.pack(pady=10)
dropdown.pack()

# Bind the event to the selection
dropdown.bind("<<ComboboxSelected>>", on_select)

# ================= Display Button ==================

buttons_frame = tk.Frame(window)
display_button = Button(buttons_frame, text="Display",
                        command=display_wave, width=36, padding=5)  # button
# display
display_button.grid(row=0)

back_main_button = Button(buttons_frame, text="Back",
                        command=lambda :hf.back_main_menu(window), width=36, padding=5)  # button
# display
back_main_button.grid(row=1)
buttons_frame.pack()


# ================= Constant ==================
# frame
constant_frame = tk.Frame(window)

constant_label = Label(constant_frame, text="Constant:",
                       font=('Arial', 10))  # label
constant_entry = Entry(constant_frame, width=39)  # entry

# ================= Normalization ==================
# frame
normalization_frame = tk.Frame(window)

# choice
normalization_choice = tk.StringVar()
normalization_choice.set("option1")  # Default selection

# choice between 0 to 1 and -1 to 1
# choice1
option1_radio = tk.Radiobutton(
    normalization_frame, text="0 to 1",
    variable=normalization_choice, value="option1")
# choice 2
option2_radio = tk.Radiobutton(
    normalization_frame, text="-1 to 1",
    variable=normalization_choice, value="option2")

# display
option1_radio.pack()
option2_radio.pack()
constant_label.pack()
constant_entry.pack()

# =========== Addition and subtraction frames ============

num_frame = tk.Frame(window)
# number of signals
signal_num_label = Label(
    num_frame, text="# Files:", font=('Arial', 10))  # label
signal_num_entry = Entry(num_frame)  # entry

# button
signal_num_button = Button(num_frame, text="Apply", command=lambda: create_signal_inputs(
    int(cast_to_float(signal_num_entry.get()))))

# display
signal_num_label.grid(row=0, column=0)
signal_num_entry.grid(row=0, column=1)
signal_num_button.grid(row=0, column=2)


 
    
    
def close_gui():
    window.destroy()
    main.start_gui()

back_button = Button(window, text="Back", command=close_gui)
back_button.pack()
def start_gui():
    window.mainloop()
    
start_gui()

# Run the main loop

