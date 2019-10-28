
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
# import tkinter as Tk

import time
import sys
import os
import re
import numpy as np


def las_pick():
    input_0 = filedialog.askdirectory(title="Choose .LAS Directory")
    input_entry.delete(0, END)
    input_entry.insert(0, input_0)


def out_dir_pick():
    output = filedialog.askdirectory(title="Choose Output Folder")
    output_entry.delete(0, END)
    output_entry.insert(0, output)


def tops_pick():
    tops = filedialog.askdirectory(title="Choose Tops Directory")
    tops_entry.delete(0, END)
    tops_entry.insert(0, tops)

# def open():
#     dir = input_entry.get()


def batch_run(input_dir, output_dir, network, smoothing=101):
    las_files = [x for x in os.listdir(input_dir) if os.path.splitext(x)[1].lower() == '.las']

    num = len(las_files)

    print_strings = []
    print_strings.append("Neural Network Automation")
    print_strings.append("Using Neural Network: {}".format(os.path.basename(network)))
    print_strings.append("Found {0} .LAS Files".format(num))
    [print(x) for x in print_strings]

    error_array = []
    time_array = []

    for i, file in enumerate(las_files):

        try:
            output_file = os.path.splitext(file)[0] + '.strat'
            os.system('cls')
            [print(x) for x in print_strings]

            print("Running: ", output_file)
            if len(time_array) == 0:
                time_left = None
            else:
                time_left = np.around((sum(time_array)/len(time_array)) * (num-i), decimals=0)
                hrs_left = int(time_left // 3600)
                time_left = int(time_left % 3600)
                min_left = int(time_left // 60)
                sec_left = int(time_left % 60)
            if time_left is not None:
                print("Estimated Time Remaining: {} hrs, {} min, {} s".format(hrs_left, min_left, sec_left))
            print('{0}/{1} files done ({2}%)'.format(i, num, np.around(i/num*100, decimals=2)), end='\r')
            if output_file in os.listdir(output_dir):
                error_array.append("File already exists: {}".format(output_file))
                continue

            file = os.path.join(input_dir, file)
            process_time = test_data_file(file, output_dir=output_dir, output_file=output_file, network=network, smoothing=smoothing, verbosity=0)
            print('{0}/{1} files done({2}%)'.format(i+1, num, np.around((i+1)/num*100, decimals=2)), end='\r')
            time_array.append(process_time)

        except indexException as exc:
            error_array.append("Error: {}".format(file))

    if len(error_array) != 0:
        print("\nErrors occured in these files: ")
        [print(f) for f in error_array]


def create():
    input_0 = input_str.get()
    output = output_str.get()
    measurement = measurement_str.get()
    tops = tops_str.get()
    if input_0 == '' or output == '' or measurement == '' or tops == '':
        messagebox.showerror("Error", "Please Correctly Input all fields")
        return
    window.destroy()
    batch_run(input_0, output, tops, int(measurement))
    input()


def cancel():
    window.destroy()


# def las_pick():
#     las_dir = filedialog.askdirectory(title="Choose .LAS Directory")
#     las_dir_entry.delete(0, Tk.END)
#     las_dir_entry.insert(0, las_dir)


# def out_dir_pick():
#     out_dir = filedialog.askdirectory(title="Choose Output Folder")
#     out_dir_entry.delete(0, Tk.END)
#     out_dir_entry.insert(0, out_dir)


# def nn_pick():
#     nn_name = filedialog.askopenfilename(filetypes=(("Neural Network File", "*.h5"), ("All Files", "*.*")), title="Load Neural Network")
#     nn_entry.delete(0, Tk.END)
#     nn_entry.insert(0, nn_name)

if __name__ == '__main__':

    window = Tk()
    window.resizable(False, False)
    try:
        icon_file = 'images/icon.ico'
        if hasattr(sys, '_MEIPASS'):
            icon_file = os.path.join(sys._MEIPASS, icon_file)
        window.iconbitmap(icon_file)
    except Exception as exc:
        pass


    window.title("Geochronological Table")
    window.configure(background="white")
    p = 1
    input_str = StringVar()
    input_label = Label(window, text="Input LAS Directory", bg="white", fg="black", font="none 10 bold") .grid(row=1, column=0, padx=10)
    input_entry = Entry(window, textvariable=input_str, width=35, bg="white")
    input_entry.grid(row=1, column=1, padx=p, pady=p)
    input_button_0 = Button(window, text="Open", width=4, command=las_pick) .grid(row=1, column=2, padx=10, pady=p)
    input_entry.insert(0, "C:/Users/azer/IdeaProjects/Triangles_Code/auto/test_dir_MP/input_las/OCSG-04903")

    output_str = StringVar()
    output_label = Label(window, text="Output Strat Directory", bg="white", fg="black", font="none 10 bold") .grid(row=2, column=0, padx=10, pady=p)
    # output_label.place(x=230, y=230)
    output_entry = Entry(window, textvariable=output_str, width=35, bg="white")
    output_entry.grid(row=2, column=1, padx=p, pady=p)
    output_button_0 = Button(window, text="Open", width=4, command=out_dir_pick) .grid(row=2, column=2, padx=10, pady=p)
    output_entry.insert(0, "C:/Users/azer/IdeaProjects/Triangles_Code/auto/test_dir_MP/output_strat")

    measurement_str = StringVar()
    label = Label(window, text="Measurement", bg="white", fg="black", font="none 10 bold") .grid(row=3, column=0, padx=10, pady=p)
    # label.place(x=0, y=130)
    Radiobutton(window, text="MD", padx=p, variable=measurement_str, value=1) .place(x=200, y=55)
    Radiobutton(window, text="TVD", padx=p, variable=measurement_str, value=2) .place(x=250, y=55)

    tops_str = StringVar()
    tops_label = Label(window, text="Tops", bg="white", fg="black", font="none 10 bold") .grid(row=4, column=0, padx=10, pady=p)
    tops_entry = Entry(window, textvariable=tops_str, width=35, bg="white")
    tops_entry.grid(row=4, column=1, padx=p, pady=p)
    tops_button_0 = Button(window, text="Open", width=4, command=tops_pick) .grid(row=4, column=2, padx=10, pady=p)
    tops_entry.insert(0, "C:/Users/azer/OneDrive/Desktop/Test_tops")


    create_button = Button(window, text="Create", width=6, command=create) .grid(row=5, column=1, padx=p, pady=p)

    cancel_button = Button(window, text="Cancel", width=6, command=cancel) .grid(row=5, column=2, padx=10, pady=p)



    # las_dir_str = StringVar()
    # las_dir_entry = Entry(window, textvariable=las_dir_str, width=35)
    # las_dir_button = Button(window, text=".LAS Directory", command=las_pick)
    #
    # out_dir_str = Tk.StringVar()
    # out_dir_entry = Tk.Entry(window, textvariable=out_dir_str, width=35)
    # out_dir_button = Tk.Button(window, text="Output Directory", command=out_dir_pick)
    #
    # nn_str = Tk.StringVar()
    # nn_entry = Tk.Entry(window, textvariable=nn_str, width=35)
    # nn_button = Tk.Button(window, text="Choose Neural Network", command=nn_pick)
    #
    # smoothing_str = Tk.StringVar(value="101")
    # smoothing_label = Tk.Label(text="Choose Smoothing Size: ")
    # smoothing_entry = Tk.Entry(window, textvariable=smoothing_str)
    #
    # apply_button = Tk.Button(window, text="Apply", command=apply)
    # cancel_button = Tk.Button(window, text="Cancel", command=cancel)
    #
    # p = 1
    # las_dir_entry.grid(row=0, column=0, padx=p, pady=p)
    # las_dir_button.grid(row=0, column=1, padx=p, pady=p)
    # out_dir_entry.grid(row=1, column=0, padx=p, pady=p)
    # out_dir_button.grid(row=1, column=1, padx=p, pady=p)
    # nn_entry.grid(row=2, column=0, padx=p, pady=p)
    # nn_button.grid(row=2, column=1, padx=p, pady=p)
    # smoothing_label.grid(row=3, column=0, padx=p, pady=p)
    # smoothing_entry.grid(row=3, column=1, padx=p, pady=p)
    # apply_button.grid(row=4, column=1, padx=p, pady=p)
    # cancel_button.grid(row=4, column=2, padx=p, pady=p)

    window.mainloop()