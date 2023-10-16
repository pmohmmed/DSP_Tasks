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
        file.close()

    def plot_discrete(self):

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
        plt.title('Discrete Representation')

        # Show the plot
        plt.show()

    def plot_continuous_discrete(self):
        # Plot continuous representation
        x_continuous = np.linspace(0, len(self.x_values) - 1, 1000)  # Generate x values for a smooth curve
        y_continuous = np.interp(x_continuous, self.x_values, self.y_values)  # Interpolate for a smooth curve
        # Draw the x-axis line
        plt.axhline(0, color='black')
        # Plot discrete representation
        # Plot the digital signal with red points
        plt.stem(self.x_values, self.y_values, linefmt='-',
                 markerfmt='ro', basefmt=' ', label="Discrete")
        plt.xlim(min(self.x_values), max(self.x_values) + 1)
        plt.ylim(min(self.y_values) - 1, max(self.y_values) + 1)

        plt.plot(x_continuous, y_continuous, 'b-', label="Continuous")

        plt.xlabel('n')
        plt.ylabel('x[n]')
        plt.title('Continuous and Discrete Representation')
        plt.grid(True)
        plt.legend()
        plt.show()

    def plot_continuous(self):
        # Plot continuous representation
        x_continuous = np.linspace(0, len(self.x_values) - 1, 1000)  # Generate x values for a smooth curve
        y_continuous = np.interp(x_continuous, self.x_values, self.y_values)  # Interpolate for a smooth curve
        plt.plot(x_continuous, y_continuous, 'b')
        plt.axhline(0, color='black')
        # Set y-axis limits
        plt.xlim(min(x_continuous), max(x_continuous)+1)
        plt.ylim(min(y_continuous)-1, max(y_continuous)+1)
        plt.xlabel('n')
        plt.ylabel('x[n]')
        plt.title('Continuous Representation')
        plt.grid(True)
        plt.show()

    def read_input(self, filename='Sin_Cos\Inputs.txt'):
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

    # Function to display sine or cosine wave
    def display_wave(self):
        title = ''
        wave_sin = []
        wave_cos = []

        # =====================================
        # ---             SIN
        # Calculate the angular frequency (ω) based on the Analog Frequency
        angular_frequency = 2 * np.pi * \
            int(self.test_cases[0]['AnalogFrequency'])
        # Initialize an empty list to store the modeled sine wave and indices
        indicis_sin = range(
            0, int(self.test_cases[0]['SamplingFrequency']))

        # Loop through the data points
        for i in indicis_sin:
            # Calculate the sine wave at this time point
            sine_value = int(self.test_cases[0]['A']) * np.sin(angular_frequency * i / int(
                self.test_cases[0]['SamplingFrequency']) + float(self.test_cases[0]['PhaseShift']))

            # Append the modeled sine value to the list
            wave_sin.append(sine_value)

        # =====================================
        # ---             COS
        # Calculate the angular frequency (ω) based on the Analog Frequency
        angular_frequency = 2 * np.pi * \
            int(self.test_cases[1]['AnalogFrequency'])
        # Initialize an empty list to store the modeled sine wave and indices
        indicis_cos = range(
            0, int(self.test_cases[1]['SamplingFrequency']))

        # Loop through the data points
        for i in indicis_cos:
            # Calculate the cos wave at this time point
            cosine_value = int(self.test_cases[1]['A']) * np.cos(
                angular_frequency * i / int(self.test_cases[1]['SamplingFrequency']) + float(
                    self.test_cases[1]['PhaseShift']))

            # Append the modeled sine value to the list
            wave_cos.append(cosine_value)

        # If the canvas exists, delete it
        if self.display_canvas:
            self.display_canvas.get_tk_widget().pack_forget()
        # Create a new figure for the plot
        fig, ax = plt.subplots()

        if(self.wave_var.get() == 'sin'):
            ax.plot(indicis_sin[:10], wave_sin[:10], color='#eb34ae')
            print(f'sin indicis: {indicis_sin}')
            print(f'sin wave: {wave_sin}')
            SignalSamplesAreEqual(
                file_name='Sin_Cos\SinOutput.txt', indices=indicis_sin, samples=wave_sin)
            title = 'Sin Signals'

        elif(self.wave_var.get() == 'cos'):
            ax.plot(indicis_cos[:10], wave_cos[:10], color='#524a49')
            print(f'cos indicis: {indicis_cos}')
            print(f'cos wave: {wave_cos}')
            SignalSamplesAreEqual(
                file_name='Sin_Cos\CosOutput.txt', indices=indicis_cos, samples=wave_cos)
            title = 'Cos Signals'

        else:
            ax.plot(indicis_cos[:10], wave_cos[:10],
                    label='Cos', color='#524a49')
            ax.plot(indicis_sin[:10], wave_sin[:10],
                    label='Sin', color='#eb34ae')
            title = 'Sin & Cos signals'
            print(f'sin indicis: {indicis_sin}')
            print(f'sin wave: {wave_sin}')
            print(f'cos indicis: {indicis_cos}')
            print(f'cos wave: {wave_cos}')
            plt.legend(loc='upper right')

        ax.set_title(title)
        # Embed the plot in the Tkinter window
        self.display_canvas = FigureCanvasTkAgg(figure=fig, master=self.window)
        self.display_canvas.get_tk_widget().pack()
        # self.display_canvas.draw()

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
            file='..\signal.png')

        self.window.iconphoto(True, icon)

        # Create radio buttons for selecting the wave type
        self.wave_var = tk.StringVar()
        self.wave_var.set("sin")  # Default selection

        sine_radio = tk.Radiobutton(
            self.window, text="sin", variable=self.wave_var, value="sin")

        cosine_radio = tk.Radiobutton(
            self.window, text="cos", variable=self.wave_var, value="cos")

        both_radio = tk.Radiobutton(
            self.window, text="both", variable=self.wave_var, value="both")

        sine_radio.pack()
        cosine_radio.pack()
        both_radio.pack()

        # Create a button to display the selected wave
        single_display_button = tk.Button(
            self.window, text="Display", command=self.display_wave)
        single_display_button.pack()
        # Run the main loop
        self.window.mainloop()


signal = SignalProcessing()
signal.read_signal_file(filename='signal1.txt')


signal.plot_continuous_discrete()
signal.plot_continuous()
signal.plot_discrete()

signal.read_input()
signal.gui_display()
