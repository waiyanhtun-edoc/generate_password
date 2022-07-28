# from platform import win32_edition
# import imp
# from operator import imod
from tkinter import *
import tkinter as tk
import pyperclip
from tkinter import END, ttk

root = tk.Tk()
canvas1 = tk.Canvas(root, width=600,height=200)
canvas1.pack()

def set_text(text):
    entry1.delete(0,END)
    entry1.insert(0,text)
    return

def clear():
    entry1.delete(0,END)
    return 

entry1 = tk.Entry(root)
canvas1.create_window(100,50,window=entry1)

button1 = ttk.Button(
    text="Generate",
    command=lambda:set_text("sometext")
    )

button2 = ttk.Button(
    text="clear",
    command=lambda:clear()
    )

canvas1.create_window(350,50,window=button2)
canvas1.create_window(250,50,window=button1)


if __name__ == '__main__':
    root.mainloop()