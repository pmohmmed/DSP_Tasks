import matplotlib.pyplot as plt

def draw(x1 = [], y1 = [],x2 = None, y2 = None, label1 = "", label2="",type = "disctete", title = 'Signal'):
    plt.close()
    plt.axhline(0, color='black')
    count = 0
    if x1 is not None and y1 is not None and len(x1) > 0:
            
        count +=1

        if (type == "discrete" or type == 'both'):
            plt.stem(x1, y1, linefmt='-',
                     markerfmt='ro', basefmt=' ')
        if (type == "continuous" or type == 'both'):
            plt.plot(x1, y1, label=label1,color='black')
            
    if x2 is not None and y2 is not None and len(x2) > 0:
        if(type == "discrete" or type == 'both'):
            plt.stem(x2, y2, linefmt='-',
                         basefmt=' ')
        if (type == "continuous" or type == 'both'):
            plt.plot(x2, y2,  label=label2, color='black')

        count +=1
    
        

    plt.xlabel('n')
    plt.ylabel('x[n]')
    plt.title(title)
    plt.grid(True)
    if(count >1):
        plt.legend(loc='upper right')
    
    plt.show()

def read_file(filename = ""):
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
    return signalType,isPeriodic,N,values

def write_file(file_name = "",signalType = 0,isPeriodic = 0,N = 0,x = [],y=[]):
    file_contents = ""
    # Write the values back to a file in the same format
    with open(file_name, "w") as file:
        file.write(f"{signalType}\n")
        file.write(f"{isPeriodic}\n")
        file.write(f"{N}\n")

        for i in range(N):
            file.write(f"{x[i]} {y[i]}\n")
    # Specify the file name you want to read and print
    output_file = file_name
    # Read and print the contents of the file
    with open(output_file, 'r') as file:
        file_contents = file.read()
    return file_contents
    