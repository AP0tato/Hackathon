import tkinter as tk
import Globals as g


window = tk.Tk()

myVar = tk.StringVar(window)
myVar.set("Select")


window.title("Day 6.2")

w = 800 
h = 500 

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight() 

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))

title = window.title()


day  = tk.Label(window, text = "Day 6", font = "times 20", height = 0, width = 0)
day.place(x=0,y=0)


message = tk.Label(window, text = "I'm back home now but it's not reeeeeaaaaly that late...\nI don't think I should sleep yet, and I've been studying all day...", font = "times 10", height=5, bg = "white")
message.place(x=250,y=340)

stat = tk.Label(window, text = "Stress:"+str(g.p.stress) + "\nHealth:"+str(g.p.health) + "\nRest:"+str(g.p.rest) + "\nHappiness:"+str(g.p.readiness), font = "times 10", height=5)
stat.place(x=650,y=0)

sleep= tk.Button(window,text='Sleep regardless', command=lambda:sleep())
sleep.place(x=220, y=430)


stayPlay = tk.Button(window,text='Stay Up Doing Something Fun', command=lambda:stay())
stayPlay.place(x=350, y=430)

stayPlay = tk.Button(window,text='Stay Up Studying', command=lambda:study())
stayPlay.place(x=540, y=430)


def sleep():
    window.destroy()
    g.p.happiness+=7
    g.p.rest+=9
    g.p.readiness+=6
    g.p.health+=7 if g.p.health+5 < 100 else 0
    import day7

def stay():
    window.destroy()
    g.p.rest-=7
    g.p.happiness +=8 if g.p.happiness+5 < 100 else 0
    g.p.stress-=4
    g.p.health-=7
    g.p.readiness-=6

    import day7

def study():
    window.destroy()
    g.p.rest-=7
    g.p.happiness -=8
    g.p.stress+=6 if g.p.health+5 < 100 else 0
    g.p.health-=7
    g.p.readiness+=6 if g.p.readiness+6 < 100 else 0

    import day7

window.mainloop()
