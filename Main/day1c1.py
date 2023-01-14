import tkinter as tk
import Globals as g

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

window.mainloop()

def unhealthy():
    window.destroy()

    g.p.health = g.p.health*1.25-25
    g.p.satisfaction -= 5

    import day1c2

def healthy():
    window.destroy()

    g.p.health = g.p.health*0.75+25
    g.p.satisfaction -= 5

    import day1c2
