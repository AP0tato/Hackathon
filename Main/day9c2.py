import tkinter as tk
import Globals as g

window = tk.Tk()

myVar = tk.StringVar(window)
myVar.set("Select")

window.title("Day 9.2")
w = 800 
h = 500 

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight() 

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))
title = window.title()

day  = tk.Label(window, text = "Day 9", font = "times 20", height = 0, width = 0)
day.place(x=0,y=0)

message = tk.Label(window, text = "I feel pretty hungry after working out.\nLet's see what there is to eat...", font = "times 10", height=5, bg = "white")
message.place(x=245,y=340)

stat = tk.Label(window, text = "Stress:"+str(g.p.stress) + "\nHealth:"+str(g.p.health) + "\nRest:"+str(g.p.rest) + "\nHappiness:"+str(g.p.happiness) + "\nReadiness"+str(g.p.readiness), font = "times 10", height=5)
stat.place(x=650,y=0)

fast = tk.Button(window,text='Ancient Convenience Store Ramen', command=lambda:unhealthy())
fast.place(x=460, y=430)

cook = tk.Button(window,text="Last Night's Leftovers", command=lambda:healthy())
cook.place(x=260, y=430)

def unhealthy():
    window.destroy()

    g.p.health -= 6
    g.p.happiness += 5

    import day10

def healthy():
    window.destroy()

    g.p.health += 6
    g.p.happiness +=1

    import day10

window.mainloop()
