import os
from tkinter import *
from tkinter import filedialog
import numpy as np
import helper_functions as hf
from tkinter.ttk import *
import task5_data.comparesignal2 as compare
dropdown_var = num_entry = num_label =signal_f_entry= None
def open_file():
    global signal_f_entry
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    file_name = os.path.basename(file_path)
    
    signal_f_entry.delete(0, 'end')
    signal_f_entry.insert(0, file_name)
  

def on_select(e):
    global dropdown_var
    selected_item = dropdown_var.get()


    # clear
    clear_widgets()
    if(selected_item == "Smoothing"):
        smothing_display()

    elif(selected_item == "Delaying signal" or selected_item ==  "Advancing signal"):
        del_adv_signal_display()
    apply_button.pack()
    

def clear_widgets():
    num_label.forget()
    num_entry.forget()
    apply_button.forget()
def smothing_display():
    num_label.pack()
    num_entry.pack()
    num_label.config(text="Window size")
def del_adv_signal_display():
    num_label.pack()
    num_entry.pack()
    num_label.config(text="K")
    
def apply_feature():
    global dropdown_var
    selected_item = dropdown_var.get()
    if(selected_item == "Smoothing"):
        window_size =hf.cast_to_(num_entry.get(),'int') 
        print("call your function here")
        print(window_size)
    elif(selected_item == "Sharpening"):
        print("call your function here")
    elif(selected_item == "Delaying signal"):
        k =hf.cast_to_(num_entry.get(),'int') 
        print("call your function here")
        print(k)
        
    elif(selected_item == "Advancing signal"):
        k =hf.cast_to_(num_entry.get(),'int') 
        print("call your function here")
        print(k)
        
    elif(selected_item == "Folding"):
        print("call your function here")
        
    elif(selected_item == "Delaying folded signal"):
        print("call your function here")
        
    elif(selected_item == "Advanced folded signal"):
        print("call your function here")
        
    elif(selected_item == "Remove Dc"):
        print("call your function here")
        
        
        
        
    
def open_gui(root):
    global window, dropdown_var,num_label ,num_entry,apply_button,signal_f_entry
    
    window = Toplevel(root)
    window.title("Task 5")
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
    dropdown['values'] = ("Smoothing", "Sharpening", "Delaying signal", "Advancing signal",
               "Folding", "Delaying folded signal","Advanced folded signal", "Remove Dc")
    
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