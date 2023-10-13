import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Function to display sine or cosine wave
def display_wave(wave_type):
    x = np.linspace(0, 2 * np.pi, 1000)
    if wave_type == "Sine":
        y = np.sin(x)
        title = "Sine Wave"
    elif wave_type == "Cosine":
        y = np.cos(x)
        title = "Cosine Wave"


    # Create a new figure for the plot
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(title)

    # Embed the plot in the Tkinter window
    display_wave.canvas = FigureCanvasTkAgg(fig, master=window)
    display_wave.canvas.get_tk_widget().pack()
    display_wave.canvas.draw()


# Create the main window
window = tk.Tk()
window.title("Sine/Cosine Wave Viewer")

# Create a label
label = tk.Label(window, text="Select a wave to view:")
label.pack()

# Create radio buttons for selecting the wave type
wave_var = tk.StringVar()
wave_var.set("Sine")  # Default selection
sine_radio = tk.Radiobutton(window, text="Sine", variable=wave_var, value="Sine")
cosine_radio = tk.Radiobutton(window, text="Cosine", variable=wave_var, value="Cosine")
sine_radio.pack()
cosine_radio.pack()

# Create a button to display the selected wave
display_button = tk.Button(window, text="Display", command=lambda: display_wave(wave_var.get()))
display_button.pack()

# Run the main loop
window.mainloop()