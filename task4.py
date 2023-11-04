import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.fftpack import fft, ifft


def apply_fft():
    global signal, fs
    fs = float(sampling_frequency_entry.get())
    N = len(signal)
    freq = np.fft.fftfreq(N, 1 / fs)
    amplitude = np.abs(fft(signal))
    phase = np.angle(fft(signal))

    amplitude_entry.delete(0, 'end')
    amplitude_entry.insert(0, amplitude)
    phase_entry.delete(0, 'end')
    phase_entry.insert(0, phase)

    plot_fft(freq, amplitude, phase)


def plot_fft(freq, amplitude, phase):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 4))
    ax1.plot(freq, amplitude)
    ax1.set_ylabel('Amplitude')
    ax2.plot(freq, phase)
    ax2.set_ylabel('Phase')
    ax2.set_xlabel('Frequency (Hz)')

    canvas = FigureCanvasTkAgg(fig, master=fft_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0)


def modify_signal():
    new_amplitude = eval(amplitude_entry.get())
    new_phase = eval(phase_entry.get())

    global signal
    signal = new_amplitude * np.exp(1j * new_phase)
    plot_signal()


def plot_signal():
    fig, ax = plt.subplots(figsize=(6, 4))
    t = np.arange(0, len(signal)) / fs
    ax.plot(t, np.real(signal))
    ax.set_ylabel('Amplitude')
    ax.set_xlabel('Time (s)')

    canvas = FigureCanvasTkAgg(fig, master=signal_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0)


def reconstruct_signal():
    global signal, fs
    N = len(signal)
    time_values = np.arange(N) / fs
    reconstructed_signal = ifft(signal)
    signal = reconstructed_signal
    plot_signal()


app = tk.Tk()
app.title("Frequency Domain Analysis")
app.geometry("800x600")

# Create frames
input_frame = ttk.LabelFrame(app, text="Input Signal")
input_frame.pack(pady=10)

fft_frame = ttk.LabelFrame(app, text="FFT")
fft_frame.pack(pady=10)

signal_frame = ttk.LabelFrame(app, text="Modified Signal")
signal_frame.pack(pady=10)

# Sampling frequency input
sampling_frequency_label = ttk.Label(input_frame, text="Sampling Frequency (Hz):")
sampling_frequency_label.grid(row=0, column=0)
sampling_frequency_entry = ttk.Entry(input_frame)
sampling_frequency_entry.grid(row=0, column=1)

# Signal modification inputs
amplitude_label = ttk.Label(input_frame, text="Amplitude:")
amplitude_label.grid(row=1, column=0)
amplitude_entry = ttk.Entry(input_frame)
amplitude_entry.grid(row=1, column=1)

phase_label = ttk.Label(input_frame, text="Phase:")
phase_label.grid(row=2, column=0)
phase_entry = ttk.Entry(input_frame)
phase_entry.grid(row=2, column=1)

# Apply FFT button
apply_fft_button = ttk.Button(input_frame, text="Apply FFT", command=apply_fft)
apply_fft_button.grid(row=3, columnspan=2)

# Modify Signal button
modify_signal_button = ttk.Button(input_frame, text="Modify Signal", command=modify_signal)
modify_signal_button.grid(row=4, columnspan=2)

# Reconstruct Signal button
reconstruct_signal_button = ttk.Button(input_frame, text="Reconstruct Signal", command=reconstruct_signal)
reconstruct_signal_button.grid(row=5, columnspan=2)

# Initial signal (Example: A single sinusoid)
fs = 1000  # Default sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)
signal = np.sin(2 * np.pi * 5 * t)  # A single sinusoid

# Plot initial signal
plot_signal()

app.mainloop()
