
import tkinter as tk
from tkinter.ttk import *

# Now you can import the module or package
import task1
import task2
import task3
import task4
import task5

main_window = None


def open_task(i):
    global main_window
    # Hide the main window
    main_window.withdraw()
    # Create a new top-level window
    if(i == 1):
        task1.signal.open_gui(main_window)
    elif(i == 2):
        task2.open_gui(main_window)  
    elif(i == 3):
        task3.open_gui(main_window)     
    elif(i == 4):
        task4.open_gui(main_window)
    elif(i == 5):
        task5.open_gui(main_window)       
    
def create_task_button(N=1):
    for i in range(N):
        button = tk.Button(main_window,
                           text=f"Task{i+1}",
                           command=lambda e = i+1: open_task(e))  # button
        button.pack()
        
# Create the main main_window

def start_program(number_of_tasks=1):
    global main_window
    main_window = tk.Tk()
    main_window.title("Main Menu")
    main_window.geometry("500x500")
    # Program icon
    icon = tk.PhotoImage(
        file='signal.png')

    main_window.iconphoto(True, icon)

    create_task_button(number_of_tasks)
    main_window.mainloop()


start_program(5)