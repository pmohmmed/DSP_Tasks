import os
import tkinter as tk
from tkinter import ttk, filedialog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.fftpack import fft, ifft
import helper_functions as hf
from tkinter.ttk import *

x = None
y = None
def open_file(entry):

    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    file_name = os.path.basename(file_path)

    global x, y
    x, y = hf.read_signal_file(path=file_path)
    entry.delete(0, 'end')
    entry.insert(0, file_name)

def display_wave(dft_choice):
    global x, y
    apply_dft_idft(dft_choice)

    if(dft_choice.get() == "dft"):
        hf.draw(x1=x, y1=y,
                title="DFT Signal", type="both",label1="Phase", label2="Amplitude")
    else:
        hf.draw(x1=x, y1=y,
                title="Sampling Signal", type="both", label1="n", label2="x[n]")

def modified_wave():
    global x, y
    apply_modify_signal()
    hf.draw(x1=x, y1=y,
            title="DFT Signal", type="both", label1="Phase", label2="Amplitude")
def apply_dft_idft(dft_choice):
    # here to implement your function
    global x, y
    if(dft_choice == "dft"):
        hf.isPeriodic = 1
    else:
        hf.isPeriodic = 0
    # todo
def apply_modify_signal():
    # here to implement your function
    global x, y
    # todo


window = tk.Tk()
window.title("Frequency Domain Analysis")
window.geometry("490x460")
icon = tk.PhotoImage(
    file='signal.png')

window.iconphoto(True, icon)


# frame
dft_frame = tk.Frame(window,bg='lightblue')
# ================= DFT_Choice ==================
# choice
dft_choice = tk.StringVar()
dft_choice.set("dft")  # Default selection
# choice between DFT and IDFT
# choice1
option1_radio = tk.Radiobutton(
    dft_frame, text="DFT",
    variable=dft_choice, value="dft")
# choice 2
option2_radio = tk.Radiobutton(
    dft_frame, text="IDFT",
    variable=dft_choice, value="idft")
option1_radio.grid(row=0,columnspan=5)
option2_radio.grid(row=1,columnspan=5)

file_frame = tk.Frame(dft_frame)
dft_label = tk.Label(file_frame,
                 text="File:",
                 font=('Arial', 10))  # label
dft_entry = tk.Entry(file_frame,width=50)  # entry
dft_button = tk.Button(file_frame,
                   text="Browse",
                   command=lambda e=dft_entry: open_file(e))  # button
# display
dft_label.grid(row=0, column=0)
dft_entry.grid(row=0, column=1)
dft_button.grid(row=0, column=2)
file_frame.grid(row=2,pady=20)



display_button = tk.Button(dft_frame, text="Display",
                        command=lambda :display_wave(dft_choice), width=50)  # button
# display
display_button.grid(row=3)
dft_frame.grid(padx=50, pady=15)

# Create frames
modify_frame = ttk.LabelFrame(window, text="Modify Signal")

select_label = tk.Label(modify_frame, text="Select an fundamental frequency:",
                 font=('Arial', 13))  # label
select_label.grid(row=0,columnspan=4)

# choice
dropdown_var = tk.StringVar()

# drop down list
fundamental_frequancies = Combobox(modify_frame,
                    textvariable=dropdown_var,
                    justify='center',
                    font=('Arial', 10, 'bold'))
fundamental_frequancies.grid(row=1,columnspan=4)
# list
fundamental_frequancies['values'] = (1, 2, 3, 4, 5, 6)

# conf
fundamental_frequancies.configure(height=5, width=30)
# initinal
fundamental_frequancies.set("")

inside_frame = tk.Frame(modify_frame)

A_label = tk.Label(inside_frame,
                 text="A",
                 font=('Arial', 10))  # Amplitude label
Phase_label = tk.Label(inside_frame,
                 text="Phase",
                 font=('Arial', 10))  # Phase label
A_entry = tk.Entry(inside_frame)  # Amplitude entry
Phase_entry = tk.Entry(inside_frame)  # Phase entry
A_label.grid(row=2, column=0)
A_entry.grid(row=2, column=1)
Phase_label.grid(row=2, column=2)
Phase_entry.grid(row=2, column=3)
inside_frame.grid(pady=20)

modify_button = tk.Button(modify_frame, text="Modify Signal",
                        command=modified_wave, width=42)  # button

modify_button.grid(row=3)
modify_frame.grid(padx=50, pady=50)

back_main_button = tk.Button(window, text="Back",
                        command=lambda :hf.back_main_menu(window), width=50,bg="black",fg="white",font=('Arial',10, 'bold'))  # button

back_main_button.grid(row=4)




window.mainloop()
