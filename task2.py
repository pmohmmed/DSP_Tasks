import os
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import *
import helper_functions as hf

# Initialize variables
signalType = 0
isPeriodic = 0
N = 0
values = []
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
def display_wave():
    file_content = ""
    selected_item = dropdown_var.get()
    x = []
    y = []
    file_content = perform_operation(selected_item=selected_item)
    # hf.draw(x1=x,y1=y,title=f"{selected_item} Signal",type="both")

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_name = os.path.basename(file_path)
        file1_entry.delete(0, 'end')
        file1_entry.insert(0, file_name)

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
    # note: delete print('plapla) and return x , y
    # todo
    print('plapla')
def Subtraction():
    # note: delete print('plapla) and return x , y
    # todo
    print('plapla')
def Multiplication():
    signalType, isPeriodic, N, values = hf.read_file(f"task2_data\\input\\{file1_entry.get()}")

    # Define the constant for Multiplicated the second number
    constant = int(constant_entry.get())  # You can replace this with your desired constant value

    # Multiply the second number in each pair in samples
    multiplicated_samples = []
    for pair in values:
        multiplicated_pair = [pair[0], pair[1] * constant]
        multiplicated_samples.append(multiplicated_pair)

    file_content = hf.write_file("output.txt", signalType, isPeriodic, N, multiplicated_samples)
    return file_content
def Squaring():
    signalType, isPeriodic, N, values = hf.read_file(f"task2_data\\input\\{file1_entry.get()}")

    # Square the first number in each pair in samples
    square_samples = []
    for pair in values:
        square_pair = [pair[0], pow(pair[1], 2)]
        square_samples.append(square_pair)

    file_content = hf.write_file("output.txt", signalType, isPeriodic, N, square_samples)
    return file_content
def Shifting():
    signalType, isPeriodic, N, values = hf.read_file(f"task2_data\\input\\{file1_entry.get()}")

    # Define the constant for shifting the first number
    constant = int(constant_entry.get()) * -1  # You can replace this with your desired constant value

    # Shift the first number in each pair in samples
    shifted_samples = []
    for pair in values:
        shifted_pair = [pair[0] + constant, pair[1]]
        shifted_samples.append(shifted_pair)

    file_content = hf.write_file("output.txt", signalType, isPeriodic, N, shifted_samples)
    return file_content
def Normalization():
    # note: delete print('plapla) and return x , y
    # todo
    print('plapla')
def Accumulation():
    signalType, isPeriodic, N, values = hf.read_file(f"task2_data\\input\\{file1_entry.get()}")

    # Accumulate the second number in each pair in samples
    accumulate_samples = []
    accumulator = 0  # Initialize the accumulator to 0

    for pair in values:
        accumulator += pair[1]  # Accumulate the current element
        accumulate_pair = [pair[0], accumulator]
        accumulate_samples.append(accumulate_pair)

    file_content = hf.write_file("output.txt", signalType, isPeriodic, N, accumulate_samples)
    return file_content

def perform_operation(selected_item):
    operations = {
        "Addition": Addition,
        "Subtraction": Subtraction,
        "Multiplication": Multiplication,
        "Squaring": Squaring,
        "Shifting": Shifting,
        "Normalization": Normalization,
        "Accumulation": Accumulation,
    }

    if selected_item in operations:
        return operations[selected_item]()
    else:
        print("Invalid operation")

# Create the main window
window = tk.Tk()
window.title("Dropdown List Example")
window.geometry("500x500")
# Create a label
label = tk.Label(window, text="Select an operation:",font=('Arial',14))

label.pack(pady=10)

# Create a variable to store the selected item
dropdown_var = tk.StringVar()

# Create a dropdown list
dropdown = Combobox(window, textvariable=dropdown_var,justify='center',font=('Arial',10,'bold'))
dropdown['values'] = ("Addition", "Subtraction", "Multiplication", "Squaring","Shifting","Normalization","Accumulation")
# Set the number of visible items (size)
dropdown.configure(height=5,width=30)
dropdown.pack()

# Set the initial selection
dropdown.set("")
# Bind the event to the selection
dropdown.bind("<<ComboboxSelected>>", on_select)

display_button = Button(window,text="Display",command=display_wave,width=36,padding=5)
display_button.pack()

constant_frame = tk.Frame(window)
constant_label = Label(constant_frame,text="Constant:",font=('Arial',10))
constant_entry = Entry(constant_frame,width=28)
constant_label.grid(row=0,column=0)
constant_entry.grid(row=0, column=1,padx=5)

file1_frame = tk.Frame(window)
file1_label = Label(file1_frame,text="File 1:",font=('Arial',10))
file1_entry = tk.Entry(file1_frame)
file1_button = Button(file1_frame, text="Browse", command=open_file)
file1_label.grid(row=0,column=0)
file1_entry.grid(row=0, column=1)
file1_button.grid(row=0, column=2)


file2_frame = tk.Frame(window)
file2_label = Label(file2_frame,text="File 2:",font=('Arial',10))
file2_entry = tk.Entry(file2_frame)
file2_button = Button(file2_frame, text="Browse", command=open_file)
file2_label.grid(row=0,column=0)
file2_entry.grid(row=0, column=1)
file2_button.grid(row=0, column=2)

# Run the main loop
window.mainloop()