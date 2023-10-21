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

    hf.draw(x1=x, y1=y, title=f"{selected_item} Signal", type="continuous")


def open_file(signal_number=1):

    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    file_name = os.path.basename(file_path)

    global x1, x2, y1, y2

    if(signal_number == 1):
        file_entry.delete(0, 'end')
        file_entry.insert(0, file_name)
        x1, y1 = signal.read_signal_file(path=file_path)
    #
    else:
        print("Invalid signal number")

# num_signals = int(cast_to_float(signal_num_entry.get()))


def create_signal_inputs(N=1):

    # Clear existing signal frames and widgets
    for widget in signal_frame.winfo_children():
        widget.destroy()

    # Generate signal input fields
    for i in range(N):
        file_frame = tk.Frame(signal_frame)

        label = tk.Label(file_frame, text=f"File {i+1}:", font=('Arial', 10))
        entry = tk.Entry(file_frame)
        button = tk.Button(file_frame, text="Browse",
                           command=lambda i=i: open_file(i+1))

        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        button.grid(row=0, column=2)

        file_frame.pack()
    signal_frame.pack()


def clear_widgets():
    constant_frame.forget()
    file_frame.forget()
    normalization_frame.forget()
    signal_frame.forget()
    num_frame.forget()


def normalization_rad_frame():
    normalization_frame.pack()
    file_frame.pack()


def constant_file_frame():
    constant_frame.pack()
    file_frame.pack()


def onefile_frame():
    file_frame.pack()


def files_frame(N=1):
    file1_frame.pack()
    file2_frame.pack()

    # signal_frame.pack()

    # for i in range(N):
    #     file1_frame.pack()


def cast_to_float(value):
    try:
        float(value)
        return float(value)
    except ValueError:
        return 0


def Addition():
    y = None
    if (y1 is not None) and (y2 is not None):
        y = y1 + y2
    hf.write_file(
        "output.txt", signal.signalType,
        signal.isPeriodic,
        signal.N, x1.astype(int), y.astype(int)
    )
    return x1, y


def Subtraction():
    y = None
    if (y1 is not None) and (y2 is not None):
        y = y1 - y2

    hf.write_file(
        "output.txt", signal.signalType,
        signal.isPeriodic,
        signal.N, x1.astype(int), y.astype(int)
    )
    return x1, y


def Multiplication():
    constant = cast_to_float(constant_entry.get())
    y = None
    if (y1 is not None) and constant:
        y = y1 * constant

    hf.write_file(
        "output.txt", signal.signalType,
        signal.isPeriodic,
        signal.N, x1.astype(int), y.astype(int)
    )

    return x1, y


def Squaring():
    y = None
    if (y1 is not None):
        y = np.power(y1, 2)

    hf.write_file(
        "output.txt", signal.signalType,
        signal.isPeriodic,
        signal.N, x1.astype(int), y.astype(int)
    )
    return x1, y


def Shifting():

    x = None
    constant = cast_to_float(constant_entry.get()) * -1

    if (x1 is not None):
        x = x1 + constant

    hf.write_file(
        "output.txt", signal.signalType,
        signal.isPeriodic,
        signal.N, x.astype(int), y1.astype(int)
    )

    return x, y1


def Normalization():

    y = None

    if (y1 is not None):
        ymin = np.min(y1)
        ymax = np.max(y1)

        # 0 to 1
        if(normalization_choice.get() == 'option1'):
            y = (y1 - ymin) / (ymax - ymin)
        # -1 to 1
        else:
            y = 2 * ((y1 - ymin) / (ymax - ymin)) - 1
    hf.write_file(
        "output.txt", signal.signalType,
        signal.isPeriodic,
        signal.N, x1.astype(int), y
    )
    return x1, y


def Accumulation():

    y = np.add.accumulate(y1).astype(int)

    hf.write_file(
        "output.txt", signal.signalType,
        signal.isPeriodic,
        signal.N, x1.astype(int), y.astype(int)
    )
    return x1, y


# Create the main window
window = tk.Tk()
window.title("Dropdown List Example")
window.geometry("500x500")

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

display_button = Button(window, text="Display",
                        command=display_wave, width=36, padding=5)  # button
# display
display_button.pack()

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

# ======one signal (Squaring, Mulitiplication, Shifitig, Accumulation, Normalization)=====
# frame
file_frame = tk.Frame(window)

file_label = Label(file_frame, text="File:", font=('Arial', 10))  # label
file_entry = tk.Entry(file_frame)  # entry
file_button = Button(file_frame, text="Browse",
                     command=lambda: open_file(1))  # button

# display
file_label.grid(row=1, column=0)
file_entry.grid(row=1, column=1)
file_button.grid(row=1, column=2)


# =========== addition and subtraction frames ============

num_frame = tk.Frame(window)
# number of signals
signal_num_label = Label(
    num_frame, text="# Signals:", font=('Arial', 10))  # label
signal_num_entry = Entry(num_frame)  # entry

# button
signal_num_button = Button(num_frame, text="Apply", command=lambda: create_signal_inputs(
    int(cast_to_float(signal_num_entry.get()))))

# display
signal_num_label.grid(row=0, column=0)
signal_num_entry.grid(row=0, column=1)
signal_num_button.grid(row=0, column=2)

# signal frames
signal_frame = tk.Frame(window)


# Run the main loop
window.mainloop()
