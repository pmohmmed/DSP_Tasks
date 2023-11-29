import os
from tkinter import *
from tkinter import filedialog
import numpy as np
import helper_functions as hf
from task4 import *
from tkinter.ttk import *
import task5_data.comparesignal2 as compare
from task6_data.TestCases.Derivative_Updated.DerivativeSignal import DerivativeSignal
from task6_data.TestCases.Shifting_and_Folding.Shift_Fold_Signal import Shift_Fold_Signal

dropdown_var = num_entry = num_label =signal_f_entry=x_values=y_values=file_name=  None
def open_file():
    global signal_f_entry, x_values, y_values,file_name
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    file_name = os.path.basename(file_path)
    
    signal_f_entry.delete(0, 'end')
    signal_f_entry.insert(0, file_name)
    x_values, y_values = hf.read_signal_file(path=file_path)
  

def on_select(e):
    global dropdown_var
    selected_item = dropdown_var.get()


    # clear
    clear_widgets()
    if(selected_item == "Smoothing"):
        window_size_display()
    elif(selected_item == "Shifted Folded Signal"):
        k_display()

    apply_button.pack()
    

def clear_widgets():
    num_label.forget()
    num_entry.forget()
    apply_button.forget()
def window_size_display():
    num_label.pack()
    num_entry.pack()
    num_label.config(text="Window size")
def k_display():
    num_label.pack()
    num_entry.pack()
    num_label.config(text="k")
    
def apply_feature():
    global dropdown_var, x_values, y_values
    selected_item = dropdown_var.get()
    if(selected_item == "Smoothing"):
        window_size =hf.cast_to_(num_entry.get(),'int')
        x_values_smooth, y_values_smooth = Smoothing(n=x_values, x_n=y_values, window_size=window_size)
        # hf.draw(x1=list(x_values),y1=y_values,label1="n",label2='y[n]',type='discrete',title='Smoothing Signals')
        if(file_name == 'Signal2.txt'):
            print('Test on Smoothing on Signal2 ...')
            compare.SignalSamplesAreEqual(file_name='task6_data/TestCases/Moving_Average/OutMovAvgTest2.txt', samples=y_values_smooth)
        else:
            print('Test on Smoothing on Signal1 ...')
            compare.SignalSamplesAreEqual(file_name='task6_data/TestCases/Moving_Average/OutMovAvgTest1.txt', samples=y_values_smooth)
    elif(selected_item == "Sharpening"):
        print('Test Sharpening ...')
        DerivativeSignal()

    elif(selected_item == "Folding"):
        x_values_fold, y_values_fold = Folding(n=x_values, x_n=y_values)
        print('Test on Folding ...')
        Shift_Fold_Signal(file_name='task6_data/TestCases/Shifting_and_Folding/Output_fold.txt', Your_indices=x_values_fold, Your_samples=y_values_fold)
        
    elif(selected_item == "Shifted Folded Signal"):
        k = hf.cast_to_(num_entry.get(), 'int')
        x_values_fold_shif, y_values_fold_shift = Folding_with_Shifting(n=x_values, x_n=y_values, k=k)
        if(k < 0):
            print('Test on Folding with Shifting when k = -500 ...')
            Shift_Fold_Signal(file_name='task6_data/TestCases/Shifting_and_Folding/Output_ShiftFoldedby-500.txt', Your_indices=x_values_fold_shif, Your_samples=y_values_fold_shift)
        else:
            print('Test on Folding with Shifting when k = 500 ...')
            Shift_Fold_Signal(file_name='task6_data/TestCases/Shifting_and_Folding/Output_ShifFoldedby500.txt', Your_indices=x_values_fold_shif,Your_samples=y_values_fold_shift)
    elif(selected_item == "Remove Dc"):
        x_values_remove_ds, y_values_remove_ds = Remove_DC(n=x_values, x_n=y_values)
        print('Test on Remove_DC ...')
        compare.SignalSamplesAreEqual(file_name='task5_data/RM_DC/DC_component_output.txt', samples=y_values_remove_ds)

def Smoothing(n, x_n, window_size):
    y_n = []
    for i in range(len(x_n) - window_size + 1):
        sum = 0
        for j in range(window_size):
            sum += x_n[i + j]
        y_n.append(round(float(sum / window_size), 6))
    return n, y_n

def Shifting(n, x_n, k):
    new_x = [a + k for a in n]
    return new_x, x_n
def Folding(n, x_n):
    output_signals = {}
    signal_map = {}
    for i in range(len(n)):
        signal_map[n[i]] = x_n[i]
    for i, j in signal_map.items():
        output_signals[int(i)] = int(signal_map[-int(i)])
    return list(output_signals.keys()), list(output_signals.values())

def Folding_with_Shifting (n, x_n, k):
    x_folded, y_folded = Folding(n, x_n)
    output_signals_x, output_signals_y = Shifting(x_folded,y_folded,k)
    return output_signals_x, output_signals_y
def Remove_DC(n, x_n):
    amplitude, phase = dft(x_n, len(n))
    amplitude[0] = np.abs(complex(0, 0))
    phase[0] = np.angle(complex(0, 0))
    final_output = idft(amplitude, phase, len(n))
    final_output = [np.round(z, 3) for z in final_output]
    final_output = [value.real for value in final_output]
    return n, final_output
        
        
        
    
def open_gui(root):
    global window, dropdown_var,num_label ,num_entry,apply_button,signal_f_entry
    
    window = Toplevel(root)
    window.title("Task 6")
    window.geometry("800x500")
    icon = PhotoImage(
        file='signal.png')
        
    # ============ Back to main =============
    back_button = Button(window, text='Back', command=lambda:hf.switch_to_main(root,window), width=50)
    back_button.pack()
    
    # ============ Drop down list ============

    
    
    # choice
    dropdown_var = StringVar()

    # drop down list
    dropdown = Combobox(window,
                        textvariable=dropdown_var,
                        justify='center',
                        font=('Arial', 10, 'bold'))
    # list
    dropdown['values'] = ("Smoothing", "Sharpening",
               "Folding", "Shifted Folded Signal", "Remove Dc")
    
  # conf
    dropdown.configure(height=5, width=30)
    # initinal
    dropdown.set("")

    dropdown.pack()

    # Bind the event to the selection
    dropdown.bind("<<ComboboxSelected>>", on_select)

    file_frame = Frame(window)
    signal_f_label = Label(file_frame,
                    text="File:",
                    font=('Arial', 10))  # label
    signal_f_entry = Entry(file_frame,width=50)  # entry
    
    signal_f_button = Button(file_frame,
                    text="Browse",
                    command=open_file)  # button
    signal_f_label.grid(row=0, column=0)
    signal_f_entry.grid(row=0, column=1)
    signal_f_button.grid(row=0, column=2)
    file_frame.pack()
    
    num_label = Label(window, text="Constant:",
                        font=('Arial', 10))  # label
    
    num_entry = Entry(window, width=39)  # entry
    apply_button = Button(window,text = 'Apply', width=39, command=apply_feature)  # entry

    

    window.mainloop()