# from helper_functions import *
# from task4 import *
# import numpy as np
# from task6_7_8_data.TestCases.Derivative_Updated.DerivativeSignal import *
# import math

# import numpy as np


# # # this is first phase
# # def Smoothing(x, k):
# #     out_from_smooth = []
# #     for i in range(len(x) - k + 1):
# #         temp_sum = 0
# #         for j in range(k):
# #             temp_sum += x[i + j]
# #         out_from_smooth.append(round(float(temp_sum / k), 6))
# #     return out_from_smooth
# # x, y = read_signal_file('task2_data/input/Signal1.txt')
# # x2 , y2 = read_signal_file('task2_data/input/Signal2.txt')
# # print(x)
# # x_x = Smoothing(y, 3)
# # print(x_x)
# # print(len(x_x))
# # x_x2 = Smoothing(y2, 5)
# # print(x_x2)
# # print(len(x_x2))

# # # this the second phase
# # DerivativeSignal()

# # # this is third phase
# # def Delaying_or_advancing(x,y,k):
# #     new_x = [a + k for a in x]
# #     return new_x, y
# #
# #
# # # this is fourth phase

# def Folding_a_signal(x, y):
#     output_signals = {}
#     signal_map = {}
#     for i in range(len(x)):
#         signal_map[x[i]] = y[i]
#     for i, j in signal_map.items():
#         output_signals[int(i)] = int(signal_map[-int(i)])
#     print("keys: ", list(output_signals.keys()))
#     print("values: ", list(output_signals.values()))
#     return list(output_signals.keys()), list(output_signals.values())

# # x, y = read_signal_file('task6_7_8_data/TestCases/Shifting_and_Folding/input_fold.txt')
# x = [-2,-1,0,1,2]
# y = [1, 2,5, -2, -1]
# reX, reY = Folding_a_signal(x,y)
# print(reX)
# print(reY)

# #
# # # this is the fifth phase
# #
# # def Folding_with_Delaying_or_advancing (x,y,k):
# #     x_folded,y_folded=Folding_a_signal(x,y)
# #     output_signals_x,output_signals_y = Delaying_or_advancing(x_folded,y_folded,k)
# #     return output_signals_x, output_signals_y
# #
# # x,y = Folding_with_Delaying_or_advancing(x,y,-500)
# # print(x)
# # print(y)

# # # this is the sixth phase (final phase)
# # def Remove_DC(x, y):
# #     amplitude, phase = dft(y, len(x))
# #     amplitude[0] = np.abs(complex(0, 0))
# #     phase[0] = np.angle(complex(0, 0))
# #     final_output = idft(amplitude, phase, len(x))
# #     final_output = [np.round(z, 3) for z in final_output]
# #     final_output = [value.real for value in final_output]
# #     return x, final_output
# #
# # xx, yy = read_signal_file('task5_data/RM_DC/DC_component_input.txt')
# #
# # x, fin_out = Remove_DC(xx,yy)
# # print(x)
# # print(fin_out)
# import numpy as np
# min = 0 + 0
# max = 5 + 3
# indices = np.arange(min, max+1)
# print("indices: ", indices)
# for index in indices:
#     print(index)
# def Convolve(signal_x,signal_y, filter_x, filter_y):
#     map_x= {key: value for key, value in zip(signal_x, signal_y)}
#     map_h = {key: value for key, value in zip(filter_x, filter_y)}
#
#     min_h = filter_x[0]
#     max_h = filter_x[-1]
#
#     min_x = signal_x[0]
#     max_x = signal_x[-1]
#
#     min = min_h + min_x
#     max = max_h + max_x
#
#     indices = np.arange(min, max+1)
#
#     samples = []
#     print("indices: ", indices)
#     print(map_x)
#     print(map_h)
#     print('\n\n\n')
#     print(f"min_x: {min_x}, min_y: {max_x}, min_h: {min_h}, max_h: {max_h}")
#     for n in indices:
#
#         sum = 0
#         i_x, i_h = 0, 0
#         k = signal_x[0]
#         print(f"y[{n}]:")
#         while True:
#
#             i_x = k
#             i_h = n - k
#
#             if (i_x< min_x or i_h > max_h):
#                 k+=1
#                 continue
#             if (i_x > max_x or i_h < min_h):
#                 break
#             print(f"\ni_x: {i_x}, i_h = {i_h}")
#
#             # i = np.where(indices == i_x)[0][0]
#             # j = np.where(indices == i_h)[0][0]
#             # print(map_x[i_x], ", ", map_h[i_h])
#
#
#             sum += map_x[i_x] * map_h[i_h]
#             k+=1
#
#         samples.append(sum)
#
#     print("res: ")
#     print(int(samples))
#     print(int(indices))
#
#
# x = [-2,-1,0,1]
# y = [1,2,1,1]
# f_x = [0,1,2,3,4,5]
# f_y = [1,-1,0,0,1,1]
# Convolve(x,y,f_x, f_y)

# def shift_list(lst):
#     return np.concatenate((lst[1:], lst[:1]))
# def average_correlation(lst1,lst2):
#     lst1 = np.array(lst1)
#     lst2 = np.array(lst2)
#     lst1_square = np.sum(lst1 ** 2)
#     lst2_square = np.sum(lst2 ** 2)
#     mul = lst1_square*lst2_square
#     return math.sqrt(mul)/len(lst1)
#
# def Correlate(signal_x,signal_y, filter_y):
#     samples = []
#     length = len(signal_x)
#     print(length)
#     print(signal_y)
#     print(filter_y)
#     for i in range(length):
#         corr = 0
#         for j in range(length):
#             corr += signal_y[j]*filter_y[j]
#         corr = corr/length
#         samples.append(corr/average_correlation(signal_y,filter_y))
#         filter_y = shift_list(filter_y)
#         print(filter_y)
#     return signal_x, samples
#
# x,y=Correlate(signal_x=[0,1,2,3,4],signal_y=[2,1,0,0,3],filter_y=[3,2,1,1,5])
# print(x)
# print(y)