import importlib

import matplotlib.pyplot as plt
import numpy as np
signalType = 0
isPeriodic = 0
N = 0


def draw(x1=[], y1=[], x2=None, y2=None, label1="", label2="", type="disctete", title='Signal'):
    plt.close()
    plt.axhline(0, color='black')
    count = 0
    if x1 is not None and y1 is not None and len(x1) > 0:

        count += 1

        if (type == "continuous" or type == 'both' or (type != "continuous" and type != "discrete")):
            plt.plot(x1, y1, label=label1, color='#eb34ae')

        if(type == "discrete" or type == 'both'):
            plt.stem(x1, y1, linefmt='-',
                     markerfmt='ro', basefmt=' ')
        # if (type == "continuous" or type == 'both'):
        #     plt.plot(x1, y1, label=label1, color='black')

    if x2 is not None and y2 is not None and len(x2) > 0:
        if(type == "discrete" or type == 'both'):
            plt.stem(x2, y2, linefmt='-',
                     basefmt=' ')
        if (type == "continuous" or type == 'both'):
            plt.plot(x2, y2,  label=label2, color='black')

        count += 1

    plt.xlabel(label1)
    plt.ylabel(label2)
    plt.title(title)
    plt.grid(True)
    if(count > 1):
        plt.legend(loc='upper right')

    plt.show()


def read_file(filename=""):
    # Initialize variables
    signalType = 0
    isPeriodic = 0
    N = 0
    values = []

    # Read the file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Check if there are at least 4 lines in the file
    if len(lines) >= 4:
        signalType = int(lines[0].strip())
        isPeriodic = int(lines[1].strip())
        N = int(lines[2].strip())
        values_lines = lines[3:]

        # Split the remaining lines into pairs of numbers
        for line in values_lines:
            numbers = [int(num) for num in line.split()]
            if len(numbers) == 2:
                values.append(numbers)
    return signalType, isPeriodic, N, values


def read_signal_file(path='task1_data.signal1.txt'):
    global N, signalType, isPeriodic

    with open(path, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]

    signalType = int(lines[0])
    isPeriodic = int(lines[1])
    N = int(lines[2])
    if (N == 0):
        x_values = None
        y_values = None
    else:

        samples = [list(map(float, line.split(' ')))
                   for line in lines[3:]]

        samples = np.array(samples)

        x_values = samples[:, 0]
        y_values = samples[:, 1]
    file.close()
    return x_values, y_values


def write_file(file_name="", signalType=0, isPeriodic=0, N=0, x=[], y=[]):
    file_contents = ""

    with open(file_name, "w") as file:
        file.write(f"{signalType}\n")
        file.write(f"{isPeriodic}\n")
        file.write(f"{N}\n")

        for i in range(N):
            file.write(f"{x[i]} {y[i]}\n")

    output_file = file_name

    with open(output_file, 'r') as file:
        file_contents = file.read()
    return file_contents


def cast_to_(value, type='float'):
    if(type == 'float'):
        try:
            float(value)
            return float(value)
        except ValueError:
            return 0
    elif(type == 'int'):
        try:
            int(value)
            return int(value)
        except ValueError:
            return 0
    else:
        return 0

def back_main_menu(window):
    window.destroy()
    import main
    importlib.reload(main)
