from helper_functions import *
from task6_data.TestCases.Derivative_Updated.DerivativeSignal import *

# # this is first phase
# def Smoothing(x, k):
#     out_from_smooth = []
#     for i in range(len(x) - k + 1):
#         temp_sum = 0
#         for j in range(k):
#             temp_sum += x[i + j]
#         out_from_smooth.append(format(temp_sum / k, '.6f'))
#     return out_from_smooth
# x, y = read_signal_file('task2_data/input/Signal1.txt')
# x2 , y2 = read_signal_file('task2_data/input/Signal2.txt')
#
# x_x = Smoothing(y, 3)
# print(x_x)
# print(len(x_x))
# x_x2 = Smoothing(y2, 5)
# print(x_x2)
# print(len(x_x2))

# # this the second phase
# DerivativeSignal()

# # this is fourth phase
# def Folding_a_signal(x, y):
#     output_signals = {}
#     signal_map = {}
#     for i in range(len(x)):
#         signal_map[x[i]] = y[i]
#     for i, j in signal_map.items():
#         output_signals[int(i)] = int(signal_map[-int(i)])
#     return list(output_signals.keys()), list(output_signals.values())
#
# x, y = read_signal_file('task6_data/TestCases/Shifting_and_Folding/input_fold.txt')
# reX, reY = Folding_a_signal(x,y)
# print(reX)
# print(reY)


