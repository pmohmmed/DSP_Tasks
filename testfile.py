import tkinter as tk
from tkinter import filedialog

def open_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_entry.delete(0, 'end')
        folder_entry.insert(0, folder_path)

# Create the main window
window = tk.Tk()
window.title("Folder Selector")

# Create a custom frame to contain the folder selection entry
folder_frame = tk.Frame(window)
folder_frame.pack()

# Create an entry widget for the folder path
folder_entry = tk.Entry(folder_frame, width=30)
folder_entry.grid(row=0, column=0)

# Create a button for opening the folder selection dialog
folder_button = tk.Button(folder_frame, text="Browse", command=open_folder)
folder_button.grid(row=0, column=1)

# Run the main loop
window.mainloop()
