
from task1_data.Sin_Cos.comparesignals import SignalSamplesAreEqual
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt
import numpy as np
import helper_functions as hf


class SignalProcessing:
    def __init__(self):
        # Initialize the display canvas as None
        self.display_canvas = None

    def read_signal_file(self, filename='task1_data.signal1.txt'):

        # Read the contents of the file
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Remove leading/trailing whitespaces and newline characters
        lines = [line.strip() for line in lines]

        # Read the first three rows into separate variables
        self.signalType = int(lines[0])
        self.isPeriodic = int(lines[1])
        self.N = int(lines[2])
        if (self.N == 0):
            self.x_values = None
            self.y_values = None
        else:
            # Read the remaining rows into a list of lists
            samples = [list(map(float, line.split(' ')))
                       for line in lines[3:]]

            self.samples = np.array(samples)

            # Extract x and y values from the two-value groups
            self.x_values = self.samples[:, 0]
            self.y_values = self.samples[:, 1]
        file.close()

    def plot_discrete(self):
        hf.draw(self.x_values, self.y_values,
                type='discrete', title='Discrete Signal')

    def plot_continuous_discrete(self):

        hf.draw(self.x_values, self.y_values, type='both',
                title='Continous & Discrete signal')

    def plot_continuous(self):
        hf.draw(self.x_values, self.y_values, type='continuous')

    def read_input(self, filename='task1_data/Sin_Cos/Inputs.txt'):
        with open(filename, "r") as file:
            file_content = file.read()

        self.test_cases = []
        current_test_case = {}

        lines = file_content.split("\n")
        for line in lines:
            if line.strip() == "":
                if current_test_case:
                    self.test_cases.append(current_test_case)
                    current_test_case = {}
            elif "=" in line:
                key, value = line.split("=")
                key = key.strip()
                value = value.strip().strip('"')  # Remove double quotes if present
                current_test_case[key] = value

        if current_test_case:
            self.test_cases.append(current_test_case)

        file.close()

    def toggle_entry(self):
        if self.data_var.get() == 'input':
            self.amplitude_label.pack()
            self.amplitude_entry.pack()
            self.analog_frequency_label.pack()
            self.analog_frequency_entry.pack()
            self.sampling_frequency_label.pack()
            self.sampling_frequency_entry.pack()
            self.phase_shift_label.pack()
            self.phase_shift_entry.pack()
            # data check porpuse
            # self.completed_data = True
        else:
            self.amplitude_label.pack_forget()
            self.amplitude_entry.pack_forget()
            self.analog_frequency_label.pack_forget()
            self.analog_frequency_entry.pack_forget()
            self.sampling_frequency_label.pack_forget()
            self.sampling_frequency_entry.pack_forget()
            self.phase_shift_label.pack_forget()
            self.phase_shift_entry.pack_forget()
            # data check porpuse
            # self.completed_data = True

    # Function to display sine or cosine wave

    def display_wave(self):
        title = ''
        wave_sin = []
        wave_cos = []

        if(self.data_var.get() == 'input'):

            analog_frequency_sin = analog_frequency_cos = self.analog_frequency_entry.get()
            amblitude_sin = amblitude_cos = self.amplitude_entry.get()
            sampling_frequency_sin = sampling_frequency_cos = self.sampling_frequency_entry.get()
            phase_shift_sin = phase_shift_cos = self.phase_shift_entry.get()
            if(phase_shift_sin == "" or analog_frequency_sin == "" or amblitude_sin == "" or sampling_frequency_sin == ""):
                print("There is missing data !!")
                return

        else:
            analog_frequency_sin = self.test_cases[0]['AnalogFrequency']
            amblitude_sin = self.test_cases[0]['A']
            sampling_frequency_sin = self.test_cases[0]['SamplingFrequency']
            phase_shift_sin = self.test_cases[0]['PhaseShift']
            # cos
            analog_frequency_cos = self.test_cases[1]['AnalogFrequency']
            amblitude_cos = self.test_cases[1]['A']
            sampling_frequency_cos = self.test_cases[1]['SamplingFrequency']
            phase_shift_cos = self.test_cases[1]['PhaseShift']
        if(sampling_frequency_cos == "0" or sampling_frequency_sin == "0"):
            print("incorrect value of sampling frequency")
        # =====================================
        # ---             SIN
        # Calculate the angular frequency (ω) based on the Analog Frequency
        angular_frequency = 2 * np.pi * \
            int(analog_frequency_sin)
        # Initialize an empty list to store the modeled sine wave and indices
        indicis_sin = range(
            0, int(sampling_frequency_sin))

        # Loop through the data points
        for i in indicis_sin:
            # Calculate the sine wave at this time point
            sine_value = int(amblitude_sin) * np.sin(angular_frequency * i / int(
                sampling_frequency_sin) + float(phase_shift_sin))

            # Append the modeled sine value to the list
            wave_sin.append(sine_value)

        # =====================================
        # ---             COS
        # Calculate the angular frequency (ω) based on the Analog Frequency
        angular_frequency = 2 * np.pi * \
            int(analog_frequency_cos)
        # Initialize an empty list to store the modeled sine wave and indices
        indicis_cos = range(
            0, int(sampling_frequency_cos))

        # Loop through the data points
        for i in indicis_cos:
            # Calculate the cos wave at this time point
            cosine_value = int(amblitude_cos) * np.cos(
                angular_frequency * i / int(sampling_frequency_cos) + float(
                    phase_shift_cos))

            # Append the modeled sine value to the list
            wave_cos.append(cosine_value)

        # If the canvas exists, delete it
        if self.display_canvas:
            self.display_canvas.get_tk_widget().pack_forget()

        # Create a new figure for the plot
        fig, ax = plt.subplots()

        if(self.wave_var.get() == 'sin'):

            SignalSamplesAreEqual(
                file_name='task1_data/Sin_Cos/SinOutput.txt', indices=indicis_sin, samples=wave_sin)

            hf.draw(x1=indicis_sin[:10], y1=wave_sin[:10],
                    type="both", title='Sin Signals')

        elif(self.wave_var.get() == 'cos'):

            SignalSamplesAreEqual(
                file_name='task1_data/Sin_Cos/CosOutput.txt', indices=indicis_cos, samples=wave_cos)

            hf.draw(x2=indicis_cos[:10], y2=wave_cos[:10],
                    type="both", title='Cos Signals')

        else:

            hf.draw(x1=indicis_sin[:10], y1=wave_sin[:10], x2=indicis_cos[:10], y2=wave_cos[:10],
                    label1="Sin sinal", label2='Cos signal', type="both", title='Sin & Cos signals')

    def gui_display(self):
        # Create the main window
        self.window = tk.Tk()
        self.window.title("Sine/Cosine Wave Viewer")
        self.window.geometry('700x700')
        # Create a label
        label = tk.Label(self.window, text="Select a wave to view:")
        label.pack()
        # Program icon
        icon = tk.PhotoImage(
            file='signal.png')

        self.window.iconphoto(True, icon)

        # Create radio buttons for selecting the wave type
        self.wave_var = tk.StringVar()
        self.wave_var.set("sin")  # Default selection

        sine_radio = tk.Radiobutton(
            self.window, text="sin", variable=self.wave_var, value="sin")
        sine_radio.pack()

        cosine_radio = tk.Radiobutton(
            self.window, text="cos", variable=self.wave_var, value="cos")
        cosine_radio.pack()

        both_radio = tk.Radiobutton(
            self.window, text="both", variable=self.wave_var, value="both")
        both_radio.pack()

        self.data_var = tk.StringVar()
        self.data_var.set('default')  # Default selection

        # Data source selection
        self.data_var = tk.StringVar()
        self.data_var.set('default')  # Default selection

        data_label = tk.Label(self.window, text="Select Data Source:")

        input_button = tk.Radiobutton(
            self.window, text="Enter Own Data", variable=self.data_var, value='input', command=self.toggle_entry)
        input_button.pack()

        default_button = tk.Radiobutton(
            self.window, text="Default Data", variable=self.data_var, value='default', command=self.toggle_entry)
        default_button.pack()

        # Amplitude input
        self.amplitude_label = tk.Label(self.window, text="Enter Amplitude:")
        self.amplitude_entry = tk.Entry(self.window)

        # analog Frequency input
        self.analog_frequency_label = tk.Label(
            self.window, text="Enter Analog Frequency:")
        self.analog_frequency_entry = tk.Entry(self.window)

        # sampling Frequency input
        self.sampling_frequency_label = tk.Label(
            self.window, text="Enter Sampling Frequency:")
        self.sampling_frequency_entry = tk.Entry(self.window)

        # Phase shift input
        self.phase_shift_label = tk.Label(
            self.window, text="Enter Phase Shift:")
        self.phase_shift_entry = tk.Entry(self.window)

        # Create a button to display the selected wave
        single_display_button = tk.Button(
            self.window, text="Display", command=self.display_wave)
        single_display_button.pack()
        # Run the main loop
        self.window.mainloop()


signal = SignalProcessing()
signal.read_signal_file(filename='task1_data/signal1.txt')


signal.plot_continuous_discrete()
signal.plot_continuous()
signal.plot_discrete()

# signal.read_input()

# signal.gui_display()
