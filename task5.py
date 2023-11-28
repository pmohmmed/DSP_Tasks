import os
from tkinter import *
from tkinter import filedialog
import numpy as np
import helper_functions as hf
from tkinter.ttk import *
import task5_data.comparesignal2 as compare

window = None
function_type = None
m_entry = 0
m = 0
Xn = X = Y = None
def open_file(entry):
    global Xn, X
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    file_name = os.path.basename(file_path)
    X, Xn = hf.read_signal_file(path=file_path)
    entry.delete(0, 'end')
    entry.insert(0, file_name)
  

def operation():
    global Xn, X, Y
    if(Xn is None or X is None):
        return
    if function_type.get() == 'dct':
        Y = DCT(Xn)
        compare.SignalSamplesAreEqual('task5_data/DCT/DCT_output.txt', Y)
    else:
        Y = remove_DC(Xn)
        compare.SignalSamplesAreEqual('task5_data/RM_DC/DC_component_output.txt', Y)
    hf.draw(x1 = X, y1 = Y, label1='DCT')
        

def apply_save():
    if(Xn is None or X is None):
        return
    operation()
    m = hf.cast_to_(m_entry.get(), type = 'int')
    y_ = Y[:m, 0]
    ispriodic = 0
    if function_type.get() == 'dct':
        ispriodic = 1
    hf.write_file('Output.txt', isPeriodic=ispriodic, N = m, x= np.arange(m), y = y_)
  
def DCT(Xn):
    global Y
    Xn= np.array(Xn)
    N = Xn.size
    Yk = np.zeros(N)
    n = np.arange(N)
    for k in range(N):
        Yk[k] = np.sqrt(2/N) * np.sum(Xn * np.cos(np.pi/(4*N)*(2*n-1)*(2*k - 1)))
    return Yk.reshape(N,1)


def remove_DC(Xn):
    global Y
    Xn = np.array(Xn)
    mean = Xn.mean()
    Y = Xn - mean
    return Y.reshape(Xn.size,1)

dct_x, dct_y = hf.read_signal_file(path='task5_data/DCT/DCT_input.txt')
dc_x, dc_y = hf.read_signal_file(path='task5_data/RM_DC/DC_component_input.txt')



def open_gui(root):
    global window, function_type,m_entry, m
    
    window = Toplevel(root)
    window.title("Task 5")
    window.geometry("800x500")
    icon = PhotoImage(
        file='signal.png')
    function_type = StringVar()
    m = IntVar()

    user_input_frame = Frame(window)
    # ================= Function_Choice ==================
    # choice
    function_type.set("dct")  # Default selection
    # choice between DCT and RemoveDC
    # choice1
    option1_radio = Radiobutton(user_input_frame, text="DCT", variable=function_type, value="dct")
    # choice 2
    option2_radio = Radiobutton(user_input_frame, text="RemoveDC", variable=function_type, value="remove_dc")
    # read file
    dct_label = Label(user_input_frame, text="File:", font=('Arial', 10))
    dct_entry = Entry(user_input_frame,width=50)
    dct_button = Button(user_input_frame, text="Browse", command= lambda entry=dct_entry: open_file(entry))

    # m coefficients
    m_label = Label(user_input_frame, text="m", font=('Arial', 10))
    m_entry = Entry(user_input_frame, textvariable=m, width=50)

    # apply the operations and display it
    apply_button = Button(user_input_frame, text='Apply', command=operation, width=30)
    # apply and save the m coefficients in txt file
    save_button = Button(user_input_frame, text='Apply And Save', command=apply_save, width=30)

    option1_radio.grid(row=0, columnspan=5)
    option2_radio.grid(row=1, columnspan=5)
    dct_label.grid(row=2, column=0)
    dct_entry.grid(row=2, column=1)
    dct_button.grid(row=2, column=2)
    m_label.grid(row=3, column=0)
    m_entry.grid(row=3, column=1)
    apply_button.grid(row=4, column=0, columnspan=3)
    save_button.grid(row=5, column=0, columnspan=3)

    # back to main
    back_button = Button(window, text='Back', command=lambda:hf.switch_to_main(root,window), width=50)

    user_input_frame.grid(row=0, padx=90, pady=20)
    back_button.grid(row=1)
    apply_button.grid(row=4, columnspan = 3)
    save_button.grid(row=5, columnspan= 3)

    # back to main
    back_button = Button(window, text='Back', command=lambda:hf.switch_to_main(root,window))

    user_input_frame.grid(row=0, padx=90, pady=20)


    window.mainloop()