import tkinter as tk
import Globals as g


window = tk.Tk()

myVar = tk.StringVar(window)
myVar.set("Select")


window.title("Day 9.1")

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


message = tk.Label(window, text = "Today is the last day before the exams begin!\nI'm nervous, what should I do to make the most of my time?", font = "times 10", height=5, bg = "white")
message.place(x=250,y=340)

stat = tk.Label(window, text = "Stress:"+str(g.p.stress) + "\nHealth:"+str(g.p.health) + "\nRest:"+str(g.p.rest) + "\nHappiness:"+str(g.p.happiness) + "\nReadiness"+str(g.p.readiness), font = "times 10", height=5)
stat.place(x=650,y=0)

study= tk.Button(window,text='One More All-Nighter', command=lambda:review())
study.place(x=380, y=430)


gym = tk.Button(window,text='Exercise and Relax', command=lambda:gym())
gym.place(x=510, y=430)

friends= tk.Button(window,text='Go Hang Out with Friends for the Evening', command=lambda:friends())
friends.place(x=140, y=430)



def review():
    window.destroy()
    g.p.happiness-=10
    g.p.rest-=10
    g.p.readiness-=6
    g.p.stress+=8
    g.p.health-=10
    import day10

def gym():
    window.destroy()
    g.p.health+=8
    g.p.happiness +=6
    g.p.stress+=7
    g.p.readiness-=4
    g.p.rest+=6

    import day9c2

def friends():
    window.destroy()
    g.p.health-=4
    g.p.happiness +=9
    g.p.stress-=7
    g.p.readiness-=7
    g.p.rest-=6

    import day10

window.mainloop()
