import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial


class SignalProcessing:

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
signal = SignalProcessing()
signal.read_signal_file(filename='signal1.txt')


# signal.plot_analog()
# signal.plot_digital()
# signal.plot_continuous_discrete()
signal.read_input()
