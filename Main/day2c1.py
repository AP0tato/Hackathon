import tkinter as tk
import Globals as g

window = tk.Tk()

myVar = tk.StringVar(window)
myVar.set("Select")


window.title("Day 2.1")
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


message = tk.Label(window, text = "It's a new day! I have quite some time before class. What should I do now that I'm ready?", font = "times 10", height=5, bg = "white")
message.place(x=205,y=340)

stat = tk.Label(window, text = "Stress:"+str(g.p.stress) + "\nHealth:"+str(g.p.health) + "\nRest:"+str(g.p.rest) + "\nHappiness:"+str(g.p.readiness), font = "times 10", height=5)
stat.place(x=650,y=0)

exercise = tk.Button(window,text='Exercise', command=lambda:phys())
exercise.place(x=260, y=430)

hobby = tk.Button(window,text='Do a Hobby', command=lambda:hobby())
hobby.place(x=460, y=430)



def phys():
    #points to physical health
    window.destroy()

    g.p.health += 5
    g.p.happiness -= 3
    g.p.stress -= 2

    import day2c2

def hobby():
    #points to happiness
    window.destroy()

    g.p.health += 3
    g.p.happiness += 5
    g.p.stress -= 3

    import day2c2

window.mainloop()
