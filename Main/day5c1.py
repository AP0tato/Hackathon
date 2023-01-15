import tkinter as tk
import Globals as g

window = tk.Tk()

myVar = tk.StringVar(window)
myVar.set("Select")

window.title("Day 5.1")

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


message = tk.Label(window, text = "Class ran late today, I'm feel pretty drained. What should I do for today?", font = "times 10", height=5, bg = "white")
message.place(x=250,y=340)

stat = tk.Label(window, text = "Stress:"+str(g.p.stress) + "\nHealth:"+str(g.p.health) + "\nRest:"+str(g.p.rest) + "\nHappiness:"+str(g.p.readiness), font = "times 10", height=5)
stat.place(x=650,y=0)

study= tk.Button(window,text='All Nighter', command=lambda:study())
study.place(x=260, y=430)

gym = tk.Button(window,text='Go to a Gym', command=lambda:gym())
gym.place(x=360, y=430)

goOut = tk.Button(window,text='Eat Somewhere Outside', command=lambda:out())
goOut.place(x=460, y=430)



def study():
    window.destroy()

    g.p.readiness += 6
    g.p.rest -= 7
    g.p.happiness -=7
    g.p.health -=7
    g.p.stress+=6
    
    import day6c1

def gym():
    window.destroy()
    g.p.health+= 6
    g.p.stress-=3
    g.p.happiness+=5
    import day5c2

def out():
    window.destroy()
    g.p.health+= 4
    g.p.happiness +=6
    g.p.stress-=4

    import day5c2

window.mainloop()
