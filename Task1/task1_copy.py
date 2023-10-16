import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

from Sin_Cos.comparesignals import SignalSamplesAreEqual


class SignalProcessing:

    def __init__(self):
        # Initialize the display canvas as None
        self.display_canvas = None

    def read_signal_file(self, filename='signal1.txt'):

        # Read the contents of the file
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Remove leading/trailing whitespaces and newline characters
        lines = [line.strip() for line in lines]

        # Read the first three rows into separate variables
        self.signalType = int(lines[0])
        self.isPeriodic = int(lines[1])
        self.N = int(lines[2])

        # Read the remaining rows into a list of lists
        samples = [list(map(float, line.split(' ')))
                   for line in lines[3:]]

        self.samples = np.array(samples)

        # Extract x and y values from the two-value groups
        self.x_values = self.samples[:, 0]
        self.y_values = self.samples[:, 1]

    def plot_digital(self):

        # Determine the range of the y-axis
        y_range = max(abs(min(self.y_values))+1, abs(max(self.y_values))+1)
        # Plot the digital signal with red points
        plt.stem(self.x_values, self.y_values, linefmt='-',
                 markerfmt='ro', basefmt=' ')

        # Draw the x-axis line
        plt.axhline(0, color='black')

        plt.xlim(min(self.x_values), max(self.x_values) + 1)
        plt.ylim(min(self.y_values) - 1, max(self.y_values) + 1)

        # Set labels and title
        plt.xlabel('n')
        plt.ylabel('x[n]')
        plt.title('Digital Representation')

        # Show the plot
        plt.show()

    def plot_continuous_discrete(self):
        y_range = max(abs(min(self.y_values))+1, abs(max(self.y_values))+1)

        plt.step(self.x_values, self.y_values, 'b', where='post')

        plt.axhline(0, color='black')
        plt.xlim(min(self.x_values), max(self.x_values) + 1)
        plt.ylim(min(self.y_values) - 1, max(self.y_values) + 1)
        plt.xlabel('n')
        plt.ylabel('x[n]')
        plt.title('Continuous(t) Discrete(A) Representation')
        plt.grid(True)
        plt.show()

    def plot_analog(self):
        # Determine the range of the y-axis
        y_range = max(abs(min(self.y_values))+1, abs(max(self.y_values))+1)

        # Polynomial curve fitting
        degree = 6  # Change the degree based on desired smoothness
        p = Polynomial.fit(self.x_values, self.y_values, degree)
        x_smooth = np.linspace(min(self.x_values), max(self.x_values), 1000)
        y_smooth = p(x_smooth)
        plt.plot(x_smooth, y_smooth, 'b')
        plt.axhline(0, color='black')
        # Set y-axis limits
        plt.xlim(min(x_smooth), max(x_smooth)+1)
        plt.ylim(min(y_smooth)-1, max(y_smooth)+1)
        plt.xlabel('n')
        plt.ylabel('x[n]')
        plt.title('Analog Representation')
        plt.grid(True)
        plt.show()

    def read_input(self, filename='Sin_Cos/Inputs.txt'):
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

    # Function to display sine or cosine wave
    def display_wave(self, wave_type):
        title = ''
        wave = []
        indicis = None

        if wave_type == "sin":
            # Calculate the angular frequency (ω) based on the Analog Frequency
            angular_frequency = 2 * np.pi * \
                int(self.test_cases[0]['AnalogFrequency'])
            # Initialize an empty list to store the modeled sine wave and indices
            indicis = range(
                0, int(self.test_cases[0]['SamplingFrequency']))

            # Loop through the data points
            for i in indicis:
                # Calculate the sine wave at this time point
                sine_value = int(self.test_cases[0]['A']) * np.sin(angular_frequency * i / int(
                    self.test_cases[0]['SamplingFrequency']) + float(self.test_cases[0]['PhaseShift']))

                # Append the modeled sine value to the list
                wave.append(sine_value)
            # Now, 'wave' contains the modeled sine wave for each data point
            print(indicis)
            print(wave)
            SignalSamplesAreEqual(
                file_name='Sin_Cos/SinOutput.txt', indices=indicis, samples=wave)

            title = "Sinusoidal Signal"

        elif wave_type == "cos":
            # Calculate the angular frequency (ω) based on the Analog Frequency
            angular_frequency = 2 * np.pi * \
                int(self.test_cases[1]['AnalogFrequency'])
            # Initialize an empty list to store the modeled sine wave and indices
            indicis = range(
                0, int(self.test_cases[1]['SamplingFrequency']))

            # Loop through the data points
            for i in indicis:
                # Calculate the cos wave at this time point
                cosine_value = int(self.test_cases[1]['A']) * np.cos(
                    angular_frequency * i / int(self.test_cases[1]['SamplingFrequency']) + float(
                        self.test_cases[1]['PhaseShift']))

                # Append the modeled sine value to the list
                wave.append(cosine_value)
            # Now, 'cos_wave' contains the modeled sine wave for each data point
            print(indicis)
            print(wave)
            SignalSamplesAreEqual(
                file_name='Sin_Cos/CosOutput.txt', indices=indicis, samples=wave)

            title = "Cosinusoidal Signal"
        # If the canvas exists, delete it
        if self.display_canvas:
            self.display_canvas.get_tk_widget().pack_forget()

        x_smooth = np.linspace(min(indicis), max(indicis), 10000)
        y_smooth = []
        for i in x_smooth:
            # Calculate the cos wave at this time point
            cosine_value = int(self.test_cases[1]['A']) * np.cos(
                angular_frequency * i / int(self.test_cases[1]['SamplingFrequency']) + float(
                    self.test_cases[1]['PhaseShift']))
            y_smooth.append(cosine_value)

        # Create a new figure for the plot
        fig, ax = plt.subplots()
        ax.plot(indicis[:10], wave[:10])
        ax.plot(indicis[:10], wave[1:11])

        ax.set_title(title)

        # Embed the plot in the Tkinter window
        self.display_canvas = FigureCanvasTkAgg(fig, master=self.window)
        self.display_canvas.get_tk_widget().pack()
        # self.display_canvas.draw()

    def gui_display(self):
        # Create the main window
        self.window = tk.Tk()
        self.window.title("Sine/Cosine Wave Viewer")

        # Create a label
        label = tk.Label(self.window, text="Select a wave to view:")
        label.pack()

        # Create radio buttons for selecting the wave type
        self.wave_var = tk.StringVar()
        self.wave_var.set("sin")  # Default selection

        sine_radio = tk.Radiobutton(
            self.window, text="sin", variable=self.wave_var, value="sin")

        cosine_radio = tk.Radiobutton(
            self.window, text="cos", variable=self.wave_var, value="cos")
        cosine_radio = tk.Radiobutton(
            self.window, text="both", variable=self.wave_var, value="both")

        sine_radio.pack()
        cosine_radio.pack()

        # Create a button to display the selected wave
        single_display_button = tk.Button(
            self.window, text="Display", command=lambda: self.display_wave(self.wave_var.get()))
        single_display_button.pack()
        display_all_button = tk.Button(self.window,
                                       title='Display All',
                                       command=display_all)
        # Program icon
        icon = tk.PhotoImage(
            file='../signal.png')

        self.window.iconphoto(True, icon)
        # Run the main loop
        self.window.mainloop()


signal = SignalProcessing()
# signal.read_signal_file(filename='signal1.txt')


# signal.plot_analog()
# signal.plot_digital()
# signal.plot_continuous_discrete()
signal.read_input()
signal.gui_display()
