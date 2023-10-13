import numpy as np

# Parameters
A = 3
AnalogFrequency = 200
SamplingFrequency = 500
PhaseShift = 2.35619449019235

# Calculate the angular frequency (ω) based on the Analog Frequency
angular_frequency = 2 * np.pi * AnalogFrequency
print(np.pi)
print(angular_frequency)

# Given data points
data = [
    0,
    0,
    720,
    0, 2.771639,
    1, -2.771639,
    2, 2.771639,
    3, -2.771639,
    4, 2.771639,
    5, -2.771639,
    6, 2.771639,
    7, -2.771639,
    8, 2.771639,
    9, -2.771639
]

# Initialize an empty list to store the modeled sine wave
sine_wave = []

# Loop through the data points
for i in range(2, len(data), 2):
    time = i // 2
    print(time)# Time is derived from the data index
    value = data[i]  # Amplitude value from the data

    # Calculate the sine wave at this time point
    sine_value = A * np.cos(angular_frequency * time / SamplingFrequency + PhaseShift)

    # Append the modeled sine value to the list
    sine_wave.append(sine_value)
    print(f"Time = {time}, Modeled Sine Value = {sine_value:.6f}")
# Now, 'sine_wave' contains the modeled sine wave for each data point
