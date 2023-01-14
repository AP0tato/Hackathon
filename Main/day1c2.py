import tkinter as tk
import Globals as g

window = tk.Tk()

myVar = tk.StringVar(window)
myVar.set("Select")

window.title("Day 1.2")
window.geometry("800x500")
title = window.title()

day  = tk.Label(window, text = "Day 1", font = "times 20", height = 0, width = 0)
day.place(x=0,y=0)

message = tk.Label(window, text = "It's pretty late now. I don't really feel tired but I also don't have much to do...", font = "times 10", height=5, bg = "white")
message.place(x=245,y=340)

sleep = tk.Button(window,text='Go to Sleep', command=lambda:healthy())
sleep.place(x=260, y=430)

stayUp = tk.Button(window,text='Stay Up', command=lambda:unhealthy())
stayUp.place(x=460, y=430)

window.mainloop()

def unhealthy():
    window.destroy()
    g.p.rest -= 5
    import day2c1

def healthy():
    window.destroy()
    g.p.rest += 5
    import day2c1
