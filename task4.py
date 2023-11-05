import os
import tkinter as tk
from tkinter import ttk, filedialog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.fftpack import fft, ifft
import helper_functions as hf
from tkinter.ttk import *
windwo = dft_frame = dft_choice = option1_radio = option2_radio = option1_radio = option2_radio = file_frame = dft_label = dft_entry = dft_button = display_button = modify_frame = select_label = dropdown_var = fundamental_frequancies = inside_frame = A_label = Phase_label = A_entry = Phase_entry = modify_button = None
x_phase= y_phase=x_amplitude= y_amblitude=None
x = y = None
def open_file(entry,dft_choice):

    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    file_name = os.path.basename(file_path)

    global x, y
    if(dft_choice.get() == "DFT"):
        x, y = hf.read_signal_file(path=file_path)
        print("x = ", x)
        print("y = ", y)
    else:
        x, y = hf.read_amplitude_phase_file(file_path=file_path)
        print("(A) = ", x)
        print("Phase = ", y)
    entry.delete(0, 'end')
    entry.insert(0, file_name)

def display_wave(dft_choice):
    global x, y
    apply_dft_idft(dft_choice)

    if(dft_choice.get() == "DFT"):
        hf.isPeriodic = 1
        hf.draw(x1=x, y1=y,
                title="DFT Signal", type="both",label1="Phase", label2="Amplitude")
        # Format the numbers
        x = [f'{i:.13f}f' for i in x]
        y = [f'{i:.13f}f' for i in y]
        hf.write_file('output.txt', signalType=hf.signalType, isPeriodic=hf.isPeriodic, N=hf.N, x=x, y=y)
    else:
        hf.isPeriodic = 0
        hf.draw(x1=x, y1=y,
                title="Sampling Signal", type="both", label1="n", label2="x[n]")
        hf.write_file('output.txt', signalType=hf.signalType, isPeriodic=hf.isPeriodic, N=hf.N, x=x, y=y)

def modified_wave():
    global x_phase, y_phase,x_amplitude, y_amblitude

    apply_modification()
    hf.draw(x1=x_phase, y1=y_phase,x2=x_amplitude, y2=y_amblitude,
            title="DFT Signal", type="discrete", label1="Phase", label2="Amplitude")
def apply_dft_idft(dft_choice):
    # here to implement your function
    global x, y
    if (dft_choice.get() == "DFT"):
        x, y = dft(x_n=y, N=hf.N)
        # # Format the numbers
        # x = [f'{i:.13f}f' for i in x]
        # y = [f'{i:.13f}f' for i in y]
        # Print the results
        print("(A) = ", x)
        print("Phase = ", y)
    else:
        X_n = idft(amplitudes=x, phases=y, N=hf.N)
        x = np.array(range(hf.N))
        # Extract the real parts and store them in a list
        y = [round(xn.real) for xn in X_n]
        print("x = ", x)
        print("y = ", y)
def dft(x_n, N):
    x_k = np.zeros(N, dtype=np.complex128)
    for k in range(N):
        x_k[k] = np.sum(x_n * np.exp(-1j * 2 * np.pi * k * np.arange(N) / N))
    # Calculate amplitude and phase
    amplitude = np.abs(x_k)
    phase = np.angle(x_k)

    return amplitude, phase

# Function to calculate IDFT
def idft(amplitudes, phases, N):
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(1j * 2 * np.pi * k * n / N)
    X_n = np.dot(e, amplitudes * np.exp(1j * phases))
    return X_n / N
def apply_modification():
    # here to implement your function
    global x_phase, y_phase,x_amplitude, y_amblitude, A_entry, Phase_entry, fundamental_frequancies
    # #tmp
    # ff = 6.28
    # x_ = [0, 1 * ff, 2*ff, 3 *ff]
    # x_phase = x_amplitude = x_
    # y_phase = [0, -45, 0, 45]
    # y_amblitude = [6, 2.8,  2, 2.8]
    #end of tmp
    if((x_phase is not None) and (x_amplitude is not None)):
        a = hf.cast_to_(A_entry.get())
        p = hf.cast_to_(Phase_entry.get())
        
        # git index of the selected fond
        i = fundamental_frequancies.current()
        f = 0
        if (i!=0):
            f = fundamental_frequancies.get()
        y_phase[i] = p
        y_amblitude[i] = a
        return
    print('X(k) signal is missing')
    
        

    

    



def open_gui(root):
    global window, dft_frame , dft_choice , option1_radio , option2_radio , option1_radio , option2_radio , file_frame , dft_label , dft_entry , dft_button , display_button , modify_frame , select_label , dropdown_var , fundamental_frequancies , inside_frame , A_label , Phase_label , A_entry , Phase_entry , modify_button
    
    window =  tk.Toplevel(root)
    window.title("Frequency Domain Analysis")
    window.geometry("600x500")
    icon = tk.PhotoImage(
        file='signal.png')

    window.iconphoto(True, icon)


    # frame
    dft_frame = tk.Frame(window,bg='lightblue')
    # ================= DFT_Choice ==================
    # choice
    dft_choice = tk.StringVar()
    dft_choice.set("DFT")  # Default selection
    # choice between DFT and IDFT
    # choice1
    option1_radio = tk.Radiobutton(
        dft_frame, text="DFT",
        variable=dft_choice, value="DFT")
    # choice 2
    option2_radio = tk.Radiobutton(
        dft_frame, text="IDFT",
        variable=dft_choice, value="IDFT")
    option1_radio.grid(row=0,columnspan=5)
    option2_radio.grid(row=1,columnspan=5)

    file_frame = tk.Frame(dft_frame)
    dft_label = tk.Label(file_frame,
                    text="File:",
                    font=('Arial', 10))  # label
    dft_entry = tk.Entry(file_frame,width=50)  # entry
    dft_button = tk.Button(file_frame,
                    text="Browse",
                    command=lambda e=dft_entry: open_file(e,dft_choice=dft_choice))  # button
    # display
    dft_label.grid(row=0, column=0)
    dft_entry.grid(row=0, column=1)
    dft_button.grid(row=0, column=2)
    file_frame.grid(row=2,pady=20)



    display_button = tk.Button(dft_frame, text="Display",
                            command=lambda :display_wave(dft_choice), width=50)  # button
    # display
    display_button.grid(row=3)
    # dft_frame.grid(padx=50, pady=15)
    dft_frame.pack()
    
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
    # modify_frame.grid(padx=50, pady=50)
    modify_frame.pack()

    back_button = Button(window,text="back",command=lambda:hf.switch_to_main(root,window))
    back_button.pack()




