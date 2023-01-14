from pynput import keyboard
import tkinter as tk
import _thread as th
import sys

window = tk.Tk()

myVar = tk.StringVar(window)
myVar.set("Select")


window.title("Day 1")
window.geometry("800x500")
title = window.title()


day  = tk.Label(window, text = "Day 1", font = "times 20", height = 0, width = 0)
day.place(x=0,y=0)


message = tk.Label(window, text = "Today is the first day, I've decided to start small. Good in, good out!\nSo what should I eat?", font = "times 10", height=5, bg = "white")
message.place(x=245,y=340)

fast = tk.Button(window,text='Fast Food', command=lambda:unhealthy())
fast.place(x=260, y=430)

cook = tk.Button(window,text=' Homecooked', command=lambda:healthy())
cook.place(x=460, y=430)



def unhealthy():
    window.destroy()
    import day1c2

def healthy():
    window.destroy()
    import day1c2

window.mainloop()
