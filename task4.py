import tkinter as tk

# Create the first GUI window
window1 = tk.Tk()
window1.title("Window 1")
label1 = tk.Label(window1, text="This is Window 1")
label1.pack()

# Create the second GUI window
window2 = tk.Tk()
window2.title("Window 2")
label2 = tk.Label(window2, text="This is Window 2")
label2.pack()

# Run the main loop for both windows
window1.mainloop()
window2.mainloop()