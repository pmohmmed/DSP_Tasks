import helper_functions as hf
# Initialize variables
signalType = 0
isPeriodic = 0
N = 0
values = []

signalType, isPeriodic, N, values = hf.read_file("task2_data\\input\\Input Shifting.txt")

# Define the constant for shifting the first number
constant = 500 * -1  # You can replace this with your desired constant value

# Shift the first number in each pair in variable4
shifted_variable4 = []
for pair in values:
    shifted_pair = [pair[0] + constant, pair[1]]
    shifted_variable4.append(shifted_pair)

# Print the shifted_variable4 (you can replace this with any desired use)
print(f"Shifted Variable 4: {shifted_variable4}")

file_content = hf.write_file("output.txt", signalType, isPeriodic, N, shifted_variable4)
print(file_content)