import os
import tkinter as tk
import random
from tkinter import filedialog
from tkinter.ttk import *
import helper_functions as hf
import numpy as np
import task3_data.test1.QuanTest1 as t1
import task3_data.test2.QuanTest2 as t2


x = None
y = None

levels = None


def open_file():

    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    file_name = os.path.basename(file_path)

    global x, y
    x, y = hf.read_signal_file(path=file_path)

    entry.delete(0, 'end')
    entry.insert(0, file_name)

    print('x: ', x)
    print('y: ', y)


def quntization():
    levels = hf.cast_to_(num_entry.get(), type="int")
    choice = num_choice.get()
    interval_index = np.zeros(hf.N, dtype=int)
    mid_points = None

    if ((y is None) or (levels == 0)):
        print("invalid input")
        return

    # check radio
    # 0 : bits
    # 1 : levels
    if(choice == 0):
        levels = np.power(2, levels)
        print(levels)

    # 1.
    # min, max

    min = np.min(y)
    max = np.max(y)

    # 2.
    # delta
    delta = (max - min) / levels

    # 3,4. (ranges, mid points)
    mid_points = np.zeros(levels)

    n = min
    for i in range(levels):

        mid_points[i] = ((n + (n+delta)) / 2)
        n = n+delta
    for i in range(hf.N):
        y_tmp = np.abs(mid_points - y[i])
        min_indices = np.where(y_tmp == np.min(y_tmp))[0]
        min_index = min_indices[0]
        interval_index[i] = min_index

    # for i in range(hf.N):
    #     y_tmp = np.abs(mid_points - y[i])
    #     min_indices = np.where(y_tmp == np.min(y_tmp))[0]
    #     min_index = min_indices[0]
    #     interval_index[i] = min_index

    # for i in range(hf.N):
    #     y_tmp = np.abs(mid_points - y[i])
    #     min_indx = 0
    #     min_val = 100000000
    #     print("iteration: ", i+1)
    #     print(y_tmp)
    #     for j in range(levels):
    #         print(f'min: {min_val}, new: {y_tmp[j]}')

    #         if(y_tmp[j] < min_val):
    #             print('here')
    #             min_val = y_tmp[j]
    #             min_indx = j

    #     interval_index[i] = min_indx
    # for i in range(hf.N):
    #     y_tmp = np.abs(mid_points - y[i])
    #     min_indx = 0
    #     min_val = np.finfo(float).max
    #     print("iteration: ", i+1)
    #     print(y_tmp)
    #     for j in range(levels):
    #         print(f'min: {min_val}, new: {y_tmp[j]}')
    #         if y_tmp[j] < min_val:
    #             print('here')
    #             min_val = y_tmp[j]
    #             min_indx = j

    #     interval_index[i] = min_indx
    tolerance = 1e-10  # Adjust the tolerance as needed

    for i in range(hf.N):
        y_tmp = np.abs(mid_points - y[i])
        min_indx = 0
        min_val = np.finfo(float).max

        for j in range(levels):

            if y_tmp[j] < min_val - tolerance:
                min_val = y_tmp[j]
                min_indx = j

        interval_index[i] = min_indx

    bits = int(np.ceil((np.log2(levels))))

    encoded_list = np.vectorize(
        lambda x: np.binary_repr(x, width=bits))(interval_index)

    # encoded_list = np.unpackbits(interval_index.astype(np.uint8)[
    #                              :, np.newaxis], axis=1)[:, -bits:]

    quantized_list = mid_points[(interval_index)]
    eq = quantized_list - y

    print('interval:\n', (interval_index + 1).reshape(hf.N, 1))
    print('encoded:\n', encoded_list.reshape(hf.N, 1))
    print('quntized:\n', quantized_list.reshape(hf.N, 1))
    print('error:\n', eq.reshape(hf.N, 1))
    # draw
    if(choice == 1):
        t2.QuantizationTest2('task3_data/test2/Quan2_Out.txt', interval_index+1,
                             encoded_list, quantized_list, eq)
    else:
        t1.QuantizationTest1('task3_data/test1/Quan1_Out.txt',
                             encoded_list, quantized_list)

    hf.draw(x1=x, y1=y, x2=x, y2=quantized_list, title='Quantization signal',
            label1='Original signal', label2='Quantized signal', type='both')


window = tk.Tk()
window.title("Quntization")
window.geometry("500x500")
# Program icon
icon = tk.PhotoImage(
    file='signal.png')

window.iconphoto(True, icon)


# choice
# 0 : bits
# 1 : levels

num_choice = tk.IntVar()
num_choice.set(0)  # Default selection

bit_radio = tk.Radiobutton(
    window, text="Bits",
    variable=num_choice, value=0, padx=9)

# choice 2
level_radio = tk.Radiobutton(
    window, text="Levels",
    variable=num_choice, value=1)

# display
bit_radio.pack()
level_radio.pack()

num_frame = tk.Frame(window)
# number of levels/bits
num_label = tk.Label(num_frame, text="#:", font=('Arial', 15))
num_entry = tk.Entry(num_frame, width=36)


label = tk.Label(num_frame,
                 text=f"File:",
                 font=('Arial', 15))  # label
entry = tk.Entry(num_frame, width=36)  # entry
button = tk.Button(num_frame,
                   text="Browse",
                   command=open_file)  # button

# display
num_label.grid(row=0, column=0)
num_entry.grid(row=0, column=1)


label.grid(row=1, column=0, padx=5)
entry.grid(row=1, column=1, padx=5)
button.grid(row=1, column=2)

# display frame
num_frame.pack()


# ================= Display Button ==================

display_button = Button(window, text="Display",
                        command=quntization, width=36, padding=5)  # button
# display
display_button.pack()


# Run the main loop
window.mainloop()
