import os
import tkinter as tk
from tkinter import ttk, filedialog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.fftpack import fft, ifft
import helper_functions as hf
from tkinter.ttk import *
import task4_data.signalcompare as sc
import task4_data
windwo = dft_frame = dft_choice = option1_radio = option2_radio = option1_radio = option2_radio = file_frame = dft_label = dft_entry = dft_button = display_button = modify_frame = select_label = dropdown_var = fundamental_frequancies = inside_frame = A_label = Phase_label = A_entry = Phase_entry = modify_button = None
x_phase= y_phase=x_amplitude= y_amblitude=None
x = y = None
Amplitude = Phase = Frequences = None

def open_file(entry,dft_choice):

    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    file_name = os.path.basename(file_path)

    global Amplitude, Phase, Frequences, x, y
    if(dft_choice.get() == "DFT"):
        x, y = hf.read_signal_file(path=file_path)
        print("x = ", x)
        print("y = ", y)
    else:
        Amplitude, Phase = hf.read_amplitude_phase_file(file_path=file_path)
        print("(A) = ", Amplitude)
        print("Phase = ", Phase)
    entry.delete(0, 'end')
    entry.insert(0, file_name)

def display_wave(dft_choice,Fs):
    global Amplitude, Phase, Frequences, x, y
    
    apply_dft_idft(dft_choice,Fs)

    if(dft_choice.get() == "DFT"):
        hf.isPeriodic = 1
        hf.draw(x1=Frequences, y1=Amplitude,
                title="DFT Signal", type="discrete",label1="frequency", label2="amplitude")
        hf.draw(x1=Frequences, y1=Phase,
                title="DFT Signal", type="discrete", label1="frequency", label2="phase")
        amp_test, phase_test = hf.read_amplitude_phase_file('task4_data/IDFT/Input_Signal_IDFT_A,Phase.txt')
        s1 = sc.SignalComapreAmplitude(np.round(amp_test,decimals=6),np.round(Amplitude,decimals=6))
        s2= sc.SignalComaprePhaseShift(np.round(phase_test, decimals=6),np.round(Phase, decimals=6))
        if(s1 == True):
            print("pass 1")
        if(s2 == True):
            print("pass2")
        
        
        # Format the numbers
        Amplitude_ = [f'{i:.13f}f' for i in Amplitude]
        Phase_ = [f'{i:.13f}f' for i in Phase]
        
        hf.write_file('output.txt', signalType=hf.signalType, isPeriodic=hf.isPeriodic, N=hf.N, x=Amplitude_, y=Phase_)
    else:
        hf.isPeriodic = 0
        hf.draw(x1=x, y1=y,
                title="Sampling Signal", type="both", label1="n", label2="x[n]")
        hf.write_file('output.txt', signalType=hf.signalType, isPeriodic=hf.isPeriodic, N=hf.N, x=x, y=y)
    fundamental_frequancies['values'] = Frequences
    
    
def modified_wave():
    global x, y, x_amplitude, y_amblitude, Amplitude, Phase, Frequences

    apply_modification()
    # print(f'Modify wave (amplit):{Amplitude}\after: {Phase}')
    # print(f'Freq: {Frequences}')
    
    hf.draw(x1=Frequences, y1=Amplitude,
                title="DFT Signal", type="discrete",label1="frequency", label2="amplitude")
    hf.draw(x1=Frequences, y1=Phase,
                title="DFT Signal", type="discrete", label1="frequency", label2="phase")
    # hf.draw(x1=x_phase, y1=y_phase,x2=x_amplitude, y2=y_amblitude,
    #         title="DFT Signal", type="discrete", label1="Phase", label2="Amplitude")
    # hf.draw(x1= Frequences, y1= Amplitude, title='Amblitude', type='discrete')
    # hf.draw(x1= Frequences, y1= Phase, title='phase', type='discrete')

def apply_dft_idft(dft_choice,Fs):
    # here to implement your function
    global Amplitude, Phase, Frequences, x, y
    if (dft_choice.get() == "DFT"):
        Frequences = calculate_frequences(sampling_frequency=float(Fs),N=hf.N)
        Amplitude, Phase = dft(x_n=y, N=hf.N)
        # # Format the numbers
        # x = [f'{i:.13f}f' for i in x]
        # y = [f'{i:.13f}f' for i in y]
        # Print the results
        print("Frequences = ", Frequences)
        print("(A) = ", Amplitude)
        print("Phase = ", Phase)
    else:
        X_n = idft(amplitudes=Amplitude, phases=Phase, N=hf.N)
        x = np.array(range(hf.N))
        # Extract the real parts and store them in a list
        y = [round(xn.real) for xn in X_n]
        print("x = ", x)
        print("y = ", y)

def calculate_frequences(sampling_frequency, N):
    omega = (2 * np.pi) / (N * (1 / sampling_frequency)) # calculate fundamental frequency
    frequencies = [omega * k for k in range(N)]
    return frequencies
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
    global x,y, A_entry, Phase_entry, fundamental_frequancies, Amplitude, Phase


    if((x is not None) and (y is not None)):
        a = hf.cast_to_(A_entry.get())
        p = hf.cast_to_(Phase_entry.get())

        
        # git index of the selected fond
        i = fundamental_frequancies.current()

        f = 0
        if (i!=0):
            print(3)
            f = fundamental_frequancies.get()

        diff = p - Phase[i]
        Amplitude[i] = a
        Phase[i] = p
       
        Phase[(-i -1)] = Phase[(-i -1)] - diff
     
        
        return
    print('X(k) signal is missing')
    
        

    

    



def open_gui(root):
    global window, dft_frame , dft_choice , option1_radio , option2_radio , option1_radio , option2_radio, frequancy_frame, frequancy_label, frequancy_entry, file_frame , dft_label , dft_entry , dft_button , display_button , modify_frame , select_label , dropdown_var , fundamental_frequancies , inside_frame , A_label , Phase_label , A_entry , Phase_entry , modify_button
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
    
    s_frequency_label = tk.Label(dft_frame,
                    text="Fs",
                    font=('Arial', 10))  # label
    s_frequency_entry = tk.Entry(dft_frame,width=50)  # entry
    
    option1_radio.grid(row=0,columnspan=5)
    option2_radio.grid(row=1,columnspan=5)

    frequancy_frame = tk.Frame(dft_frame)
    frequancy_label = tk.Label(frequancy_frame,
                    text="Fs(kHz)",
                    font=('Arial', 10))  # label
    frequancy_entry = tk.Entry(frequancy_frame,width=50)  # entry
    frequancy_label.grid(row=0,column=0)
    frequancy_entry.grid(row=0,column=1)
    frequancy_frame.grid(row=2,pady=7)

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
    file_frame.grid(row=3,pady=20)



    display_button = tk.Button(dft_frame, text="Display",
                            command=lambda :display_wave(dft_choice,frequancy_entry.get()), width=50)  # button
    # display
    display_button.grid(row=4)
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




