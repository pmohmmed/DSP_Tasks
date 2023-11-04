import tkinter as tk
import importlib

def open_window(window_file):
    try:
        # Import the specific window file using importlib
        window_module = importlib.import_module(window_file)
        window_module.create_window(root)
    except ImportError:
        print(f"Failed to import {window_file}.")

root = tk.Tk()
root.title("Main Window")

# Button 1: Open window from window1.py
button1 = tk.Button(root, text="Open Window 1", command=lambda: open_window("task3"))
button1.pack()

# Button 2: Open window from window2.py
button2 = tk.Button(root, text="Open Window 2", command=lambda: open_window("window2"))
button2.pack()

# Button 3: Open window from window3.py
button3 = tk.Button(root, text="Open Window 3", command=lambda: open_window("window3"))
button3.pack()

root.mainloop()
