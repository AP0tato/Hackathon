import keyboard as key
import tkinter as tk
import _thread as th
import sys

import tkinter as tk
window = tk.Tk()
window.geometry('800x500')


myVar = tk.StringVar(window)
myVar.set("Select")

window.title("Game Screen")
window.geometry("800x500")
title = window.title()

welcomeLabel = tk.Label(window, text = "Welcome\nThis is the start! ", height = 5, width = 20)
welcomeLabel.pack()

window.mainloop()
