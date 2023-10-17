import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt


def plot_waves():
    # Get the user's choice of waves
    wave_choice = wave_var.get()

    # Get the user's input values
    amplitude = float(amplitude_entry.get())
    frequency = float(frequency_entry.get())
    phase_shift = float(phase_shift_entry.get())

    # Clear the plot
    plt.clf()

    # Generate x values
    x = np.linspace(0, 2 * np.pi, 100)

    # Calculate the y values based on the user's input
    if wave_choice == 'sin':
        y = amplitude * np.sin(2 * np.pi * frequency * x + phase_shift)
        plt.plot(x, y, label='Sin Wave')
    elif wave_choice == 'cos':
        y = amplitude * np.cos(2 * np.pi * frequency * x + phase_shift)
        plt.plot(x, y, label='Cos Wave')
    elif wave_choice == 'both':
        y_sin = amplitude * np.sin(2 * np.pi * frequency * x + phase_shift)
        y_cos = amplitude * np.cos(2 * np.pi * frequency * x + phase_shift)
        plt.plot(x, y_sin, label='Sin Wave')
        plt.plot(x, y_cos, label='Cos Wave')

    # Add legend and show the plot
    plt.legend()
    plt.show()


def toggle_entry():
    if data_var.get() == 'input':
        amplitude_label.grid()
        amplitude_entry.grid()
        frequency_label.grid()
        frequency_entry.grid()
        phase_shift_label.grid()
        phase_shift_entry.grid()
    else:
        amplitude_label.grid_remove()
        amplitude_entry.grid_remove()
        frequency_label.grid_remove()
        frequency_entry.grid_remove()
        phase_shift_label.grid_remove()
        phase_shift_entry.grid_remove()


# Create the main window
window = tk.Tk()
window.title("Wave Plotter")

# Wave selection
wave_var = tk.StringVar()
wave_var.set('sin')  # Default selection

wave_label = tk.Label(window, text="Select Waves:")
wave_label.grid(row=0, column=0, columnspan=3)

sin_button = tk.Radiobutton(
    window, text="Sine", variable=wave_var, value='sin')
sin_button.grid(row=1, column=0)

cos_button = tk.Radiobutton(window, text="Cosine",
                            variable=wave_var, value='cos')
cos_button.grid(row=1, column=1)

both_button = tk.Radiobutton(
    window, text="Both", variable=wave_var, value='both')
both_button.grid(row=1, column=2)

# Data source selection
data_var = tk.StringVar()
data_var.set('default')  # Default selection

data_label = tk.Label(window, text="Select Data Source:")
data_label.grid(row=2, column=0, columnspan=3)

input_button = tk.Radiobutton(
    window, text="Enter Own Data", variable=data_var, value='input', command=toggle_entry)
input_button.grid(row=3, column=0)

default_button = tk.Radiobutton(
    window, text="Default Data", variable=data_var, value='default', command=toggle_entry)
default_button.grid(row=3, column=1)

# Amplitude input
amplitude_label = tk.Label(window, text="Enter Amplitude:")
amplitude_entry = tk.Entry(window)

# Frequency input
frequency_label = tk.Label(window, text="Enter Frequency:")
frequency_entry = tk.Entry(window)

# Phase shift input
phase_shift_label = tk.Label(window, text="Enter Phase Shift:")
phase_shift_entry = tk.Entry(window)

# Plot button
plot_button = tk.Button(window, text="Plot Waves", command=plot_waves)
plot_button.grid(row=4, column=0, columnspan=3)

# Start the main event loop
window.mainloop()
