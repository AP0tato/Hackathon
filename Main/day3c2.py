import tkinter as tk
import Globals as g


window = tk.Tk()

myVar = tk.StringVar(window)
myVar.set("Select")


window.title("Day 3.2")
w = 800 
h = 500 

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight() 

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))
title = window.title()


day  = tk.Label(window, text = "Day 3", font = "times 20", height = 0, width = 0)
day.place(x=0,y=0)


message = tk.Label(window, text = "I've been sitting all day, maybe I should move around...", font = "times 10", height=5, bg = "white")
message.place(x=250,y=340)

stat = tk.Label(window, text = "Stress:"+str(g.p.stress) + "\nHealth:"+str(g.p.health) + "\nRest:"+str(g.p.rest) + "\nHappiness:"+str(g.p.happiness) + "\nReadiness"+str(g.p.readiness), font = "times 10", height=5)
stat.place(x=650,y=0)

walk = tk.Button(window,text='Walk for 20 min', command=lambda:walk())
walk.place(x=260, y=430)

gym = tk.Button(window,text='Go to a Gym', command=lambda:gym())
gym.place(x=460, y=430)



def walk():
    #adds, but less
    window.destroy()

    g.p.health += 2 if g.p.health+2 < 100 else 0
    g.p.stress -= 1
    g.p.readiness -= 2
    
    import day4

def gym():
    #adds, but more
    window.destroy()

    g.p.health += 4 if g.p.health+4 < 100 else 0
    g.p.stress += 1 if g.p.stress+1 < 100 else 0
    g.p.readiness -= 2

    import day4

window.mainloop()
