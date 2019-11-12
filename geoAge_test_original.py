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


def create():
    input_0 = input_str.get()
    output = output_str.get()
    if input_0 == '' or output == '':
        messagebox.showerror("Error", "Please Correctly Input all fields")
        return
    # window.destroy()

    print(input_0)
    print(output)

    lst = os.listdir('C:\\Users\\azer\\OneDrive\\Desktop\\geoAge\\input')

    name_list = []

    for index in range(len(lst)):
        name_list.append('C:\\Users\\azer\\OneDrive\\Desktop\\geoAge\\input\\' + lst[index])
        # print(index)
        print(name_list[index])
    print(name_list)

    for index in range(len(lst)):
        # print("After", name_list[index])
        f = open(name_list[index], 'r')
        f_contents = f.readlines()
        las_to_strat = name_list[index].replace('LAS', 'strat')
        las_to_strat = las_to_strat.replace('input', 'output')
        # las_to_strat= las_to_strat.replace('MP_LAS_by_zones\\MP313', 'MP_Strat_by_zones\\las2strat_output_MP313')
        print("replace", las_to_strat)
        wf = open(las_to_strat, 'w')
        api=str([int(i) for i in f_contents[13].split() if i.isdigit()][0])
        well_name=re.search('LL.(.+?):WE',f_contents[12]).group(1)

        wf.write("~1D SEQUENCE STRAT\n#\n")
        wf.write("VERSION: 2.3\n")
        wf.write("FILE NAME: \n")
        wf.write("WELL FILE: "+well_name.strip().replace(" 1","_1_")+"("+api+")"+"\n")
        wf.write("API: "+api+"\n")
        wf.write("WELL NAME: "+well_name.strip().replace(" 1","_1")+"\n")
        wf.write("MEASUREMENT: TVD\n#\n\n")
        wf.write("~DATA\t1\n")
        wf.write("VSH\n")
        wf.write("~VSH\n")

        data_flag=False
        for i in range(len(f_contents)):
            if f_contents[i].startswith("~A"):
                data_flag=True
                wf.write("~A"+"\t"+"MD"+"\t"+"VSH"+"\t"+"TVD"+"\n")
            if data_flag==False:
                continue
            elif f_contents[i].startswith("~A"):
                continue

            line=f_contents[i].split()
            md=line[0]
            tvd=line[1]
            if len(line)>20:
                vsh=line[-3]
            if len(line)<20:
                vsh=line[-1]
            # print(f_contents[i])
            wf.write(md+"\t"+vsh+"\t"+tvd+"\n")
        f.close()
        wf.close()

def cancel():
    window.destroy()


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
    # lst = os.listdir('C:\\Users\\azer\\OneDrive\\Desktop\\geoAge\\input')
    # input_entry.insert(0, lst)

    output_str = StringVar()
    output_label = Label(window, text="Output Strat Directory", bg="white", fg="black", font="none 10 bold") .grid(row=2, column=0, padx=10, pady=p)
    # output_label.place(x=230, y=230)
    output_entry = Entry(window, textvariable=output_str, width=35, bg="white")
    output_entry.grid(row=2, column=1, padx=p, pady=p)
    output_button_0 = Button(window, text="Open", width=4, command=out_dir_pick) .grid(row=2, column=2, padx=10, pady=p)
    # output_entry.insert(0, "C:/Users/azer/IdeaProjects/Triangles_Code/auto/test_dir_MP/output_strat")

    create_button = Button(window, text="Create", width=6, command=create) .grid(row=5, column=1, padx=p, pady=p)

    cancel_button = Button(window, text="Cancel", width=6, command=cancel) .grid(row=5, column=2, padx=10, pady=p)

    window.mainloop()

