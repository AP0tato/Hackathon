import tkinter as tk
import Globals as g


window = tk.Tk()

myVar = tk.StringVar(window)
myVar.set("Select")


window.title("Day 3.1")
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


message = tk.Label(window, text = "I have an early class today, I'm not sure if there's time to eat!", font = "times 10", height=5, bg = "white")
message.place(x=235,y=340)

stat = tk.Label(window, text = "Stress:"+str(g.p.stress) + "\nHealth:"+str(g.p.health) + "\nRest:"+str(g.p.rest) + "\nHappiness:"+str(g.p.happiness) + "\nReadiness"+str(g.p.readiness), font = "times 10", height=5)
stat.place(x=650,y=0)

eat = tk.Button(window,text='Eat Something', command=lambda:eat())
eat.place(x=460, y=430)

skip = tk.Button(window,text='Skip Breakfast', command=lambda:skip())
skip.place(x=260, y=430)



def eat():
    #physical health
    window.destroy()

    g.p.health += 4 if g.p.health+4 < 100 else 0
    g.p.stress += 2 if g.p.stress+2 < 100 else 0

    import day3c2

def skip():
    window.destroy()

    g.p.health -= 3
    
    import day3c2


window.mainloop()
