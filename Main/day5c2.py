import tkinter as tk
import Globals as g


window = tk.Tk()

myVar = tk.StringVar(window)
myVar.set("Select")


window.title("Day 5.2")

w = 800 
h = 500 

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight() 

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))

title = window.title()


day  = tk.Label(window, text = "Day 5", font = "times 20", height = 0, width = 0)
day.place(x=0,y=0)


message = tk.Label(window, text = '"Hey! What are you up to right now? Wanna join us?"\nI ran into some classmates heading out for some fun.\nShould I? It is pretty late...', font = "times 10", height=5, bg = "white")
message.place(x=250,y=340)

stat = tk.Label(window, text = "Stress:"+str(g.p.stress) + "\nHealth:"+str(g.p.health) + "\nRest:"+str(g.p.rest) + "\nHappiness:"+str(g.p.readiness), font = "times 10", height=5)
stat.place(x=650,y=0)

join= tk.Button(window,text='"Sure, why not?"', command=lambda:join())
join.place(x=260, y=430)


reject = tk.Button(window,text='"No thanks, you guys have fun."', command=lambda:dont())
reject.place(x=380, y=430)



def join():
    window.destroy()

    g.p.happiness += 7
    g.p.rest -= 8
    g.p.readiness -= 8

    import day6c1

def dont():
    window.destroy()

    g.p.rest += 7
    g.p.happiness -= 6
    g.p.stress -= 3

    import day6c1

window.mainloop()
