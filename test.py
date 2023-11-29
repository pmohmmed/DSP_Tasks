from helper_functions import *
from task4 import *
import numpy as np
from task6_data.TestCases.Derivative_Updated.DerivativeSignal import *

# # this is first phase
# def Smoothing(x, k):
#     out_from_smooth = []
#     for i in range(len(x) - k + 1):
#         temp_sum = 0
#         for j in range(k):
#             temp_sum += x[i + j]
#         out_from_smooth.append(round(float(temp_sum / k), 6))
#     return out_from_smooth
# x, y = read_signal_file('task2_data/input/Signal1.txt')
# x2 , y2 = read_signal_file('task2_data/input/Signal2.txt')
# print(x)
# x_x = Smoothing(y, 3)
# print(x_x)
# print(len(x_x))
# x_x2 = Smoothing(y2, 5)
# print(x_x2)
# print(len(x_x2))

# # this the second phase
# DerivativeSignal()

# # this is third phase
# def Delaying_or_advancing(x,y,k):
#     new_x = [a + k for a in x]
#     return new_x, y
#
#
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
#
#
# # this is the fifth phase
#
# def Folding_with_Delaying_or_advancing (x,y,k):
#     x_folded,y_folded=Folding_a_signal(x,y)
#     output_signals_x,output_signals_y = Delaying_or_advancing(x_folded,y_folded,k)
#     return output_signals_x, output_signals_y
#
# x,y = Folding_with_Delaying_or_advancing(x,y,-500)
# print(x)
# print(y)

# # this is the sixth phase (final phase)
# def Remove_DC(x, y):
#     amplitude, phase = dft(y, len(x))
#     amplitude[0] = np.abs(complex(0, 0))
#     phase[0] = np.angle(complex(0, 0))
#     final_output = idft(amplitude, phase, len(x))
#     final_output = [np.round(z, 3) for z in final_output]
#     final_output = [value.real for value in final_output]
#     return x, final_output
#
# xx, yy = read_signal_file('task5_data/RM_DC/DC_component_input.txt')
#
# x, fin_out = Remove_DC(xx,yy)
# print(x)
# print(fin_out)
