import tkinter as tk
import Globals as g


window = tk.Tk()

myVar = tk.StringVar(window)
myVar.set("Select")


window.title("Day 2.2")
w = 800 
h = 500 

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight() 

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))
title = window.title()


day  = tk.Label(window, text = "Day 2", font = "times 20", height = 0, width = 0)
day.place(x=0,y=0)


message = tk.Label(window, text = "Class is over now and I have free time. What should I do now?", font = "times 10", height=5, bg = "white")
message.place(x=235,y=340)

stat = tk.Label(window, text = "Stress:"+str(g.p.stress) + "\nHealth:"+str(g.p.health) + "\nRest:"+str(g.p.rest) + "\nHappiness:"+str(g.p.readiness), font = "times 10", height=5)
stat.place(x=650,y=0)

study = tk.Button(window,text='Study', command=lambda:study())
study.place(x=260, y=430)

friends = tk.Button(window,text='Meet with Friends', command=lambda:hobby())
friends.place(x=460, y=430)



def study():
    #not sure which stats are affected rn
    window.destroy()

    g.p.readiness += 5
    g.p.stress -= 3
    
    import day3c1

def hobby():
    #points to happiness
    window.destroy()

    g.p.health += 3
    g.p.happiness += 5
    g.p.stress -= 2
    g.p.readiness -= 1

    import day3c1

window.mainloop()
