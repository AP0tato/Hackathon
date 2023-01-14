import tkinter as tk
import Globals as g

window = tk.Tk()

myVar = tk.StringVar(window)
myVar.set("Select")


window.title("Day 4")
window.geometry("800x500")
title = window.title()


day  = tk.Label(window, text = "Day 4", font = "times 20", height = 0, width = 0)
day.place(x=0,y=0)


message = tk.Label(window, text = "My friends want to have study group at the library.\nI guess I do have time.", font = "times 10", height=5, bg = "white")
message.place(x=250,y=340)

#this is where the attribute error occurs, but it shows on repl
stat = tk.Label(window, text = "Stress:"+str(g.p.stress) + "\nHealth:"+str(g.p.health) + "\nRest:"+str(g.p.rest) + "\nHappiness:"+str(g.p.readiness), font = "times 10", height=5)
stat.place(x=650,y=0)


go = tk.Button(window,text='Join Them', command=lambda:go())
go.place(x=260, y=430)

dontGo = tk.Button(window,text='Stay at Home', command=lambda:home())
dontGo.place(x=460, y=430)



def go():
    window.destroy()
    g.p.readiness += 5
    g.p.happiness += 5
    import day5c1

def home():
    window.destroy()
    g.p.rest+= 4
    import day5c1

window.mainloop()
