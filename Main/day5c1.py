import tkinter as tk
import Globals as g

window = tk.Tk()

myVar = tk.StringVar(window)
myVar.set("Select")

window.title("Day 5.1")
window.geometry("800x500")
title = window.title()

day  = tk.Label(window, text = "Day 5", font = "times 20", height = 0, width = 0)
day.place(x=0,y=0)

message = tk.Label(window, text = "I just came back from school, and I'm feeling kind of tired,\nbut I haven't really studied for school.", font = "times 10", height=5, bg = "white")
message.place(x=250,y=340)

stat = tk.Label(window, text = "Stress:"+str(g.p.stress) + "\nHealth:"+str(g.p.health) + "\nRest:"+str(g.p.rest) + "\nHappiness:"+str(g.p.readiness), font = "times 10", height=5)
stat.place(x=650,y=0)

study = tk.Button(window,text='Study', command=lambda:study())
study.place(x=260, y=430)

sleep = tk.Button(window,text='Sleep', command=lambda:sleep())
sleep.place(x=460, y=430)



def study():
    window.destroy()
    g.p.readiness += 5
    g.p.happiness += 10
    g.p.stress -= 3
    import day5c1

def sleep():
    window.destroy()

    g.p.rest+= 7
    g.p.stress += 7
    g.p.readiness -= 4
    
    import day5c1

window.mainloop()
