import tkinter as tk
import Globals as g

window = tk.Tk()

myVar = tk.StringVar(window)
myVar.set("Select")

window.title("Day 1.2")
w = 800 
h = 500 

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight() 

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))
title = window.title()

day  = tk.Label(window, text = "Day 1", font = "times 20", height = 0, width = 0)
day.place(x=0,y=0)

message = tk.Label(window, text = "It's pretty late now. I don't really feel tired but I also don't have much to do...", font = "times 10", height=5, bg = "white")
message.place(x=245,y=340)

stat = tk.Label(window, text = "Stress:"+str(g.p.stress) + "\nHealth:"+str(g.p.health) + "\nRest:"+str(g.p.rest) + "\nHappiness:"+str(g.p.happiness) + "\nReadiness"+str(g.p.readiness), font = "times 10", height=5)
stat.place(x=650,y=0)

sleep = tk.Button(window,text='Go to Sleep', command=lambda:healthy())
sleep.place(x=260, y=430)

stayUp = tk.Button(window,text='Stay Up', command=lambda:unhealthy())
stayUp.place(x=460, y=430)

def unhealthy():
    window.destroy()

    g.p.health -= 4
    g.p.rest -= 5
    g.p.happiness += 5 if g.p.happiness+5 < 100 else 0
    g.p.stress += 5 if g.p.stress+5 < 100 else 0
    g.p.readiness -= 2

    import day2c1

def healthy():
    window.destroy()

    g.p.health += 5 if g.p.health+5 < 100 else 0
    g.p.rest += 4 if g.p.rest+5 < 100 else 0
    g.p.happiness -= 5
    g.p.stress += 2 if g.p.stress+5 < 100 else 0
    g.p.readiness -=2

    import day2c1

window.mainloop()
