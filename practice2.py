# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Data for plotting
# t = np.arange(0.0, 2.0, 0.01)
# s = 1 + np.sin(2 * np.pi * t)
#
# fig, ax = plt.subplots()
# ax.plot(t, s)
#
# ax.set(xlabel='time (s)', ylabel='voltage (mV)',
#        title='About as simple as it gets, folks')
# ax.grid()
#
# fig.savefig("test.png")
# plt.show()
#
#
# a = 1
# # Uses global because there is no local 'a'
# def f():
#     print('Inside f() : ', a)
#
# # Variable 'a' is redefined as a local
# def g():
#     a = 2
#     print('Inside g() : ', a)
#
# # Uses global keyword to modify global 'a'
# def h():
#     global a
#     a = 3
#     print('Inside h() : ', a)
#
# # Global scope
# print('global : ', a)
# f()
# print('global : ',a)
# g()
# print('global : ', a)
# h()
# print('global : ', a)
#
# def calculate(m,n):
#     result = m * n
#     return result
#
#
# print(calculate(2,3))
#
# import matplotlib.pyplot as plt
# import matplotlib.widgets as mwidgets
# fig, ax = plt.subplots()
# ax.plot([1, 2, 3], [10, 50, 100])
#
#
# def onselect(vmin, vmax):
#     print(vmin, vmax)
#     rectprops = dict(facecolor='blue', alpha=0.5)
#     span = mwidgets.SpanSelector(ax, onselect, 'horizontal', rectprops=rectprops)
#
#     fig.show()
#
# import tkinter as Tk
# from tkinter import *
#
# # widget.pack( pack_options )
# root = Tk()
# frame = Frame(root)
# frame.pack()
#
# bottomframe = Frame(root)
# bottomframe.pack( side = BOTTOM )
#
# redbutton = Button(frame, text="Red", fg="red")
# redbutton.pack( side = LEFT)
#
# greenbutton = Button(frame, text="green", fg="green")
# greenbutton.pack( side = LEFT )
#
# bluebutton = Button(frame, text="Blue", fg="blue")
# bluebutton.pack( side = LEFT )
#
# blackbutton = Button(bottomframe, text="Black", fg="black")
# blackbutton.pack( side = BOTTOM)
#
# root.mainloop()

import tkinter
from tkinter.constants import *
tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
label = tkinter.Label(frame, text="Hello, World")
label.pack(fill=X, expand=1)
button = tkinter.Button(frame,text="Exit",command=tk.destroy)
button.pack(side=BOTTOM)
tk.mainloop()