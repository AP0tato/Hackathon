import tkinter as tk
import Globals as g


window = tk.Tk()

myVar = tk.StringVar(window)
myVar.set("Select")


window.title("Day 8")

w = 800 
h = 500 

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight() 

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))

title = window.title()


day  = tk.Label(window, text = "Day 8", font = "times 20", height = 0, width = 0)
day.place(x=0,y=0)


message = tk.Label(window, text = "I have another day mostly to myself. Hey, I haven't exercised in a while...\nBut I don't want to waste precious studying time...\nBut I also don't really want to do anything...", font = "times 10", height=5, bg = "white")
message.place(x=250,y=340)

stat = tk.Label(window, text = "Stress:"+str(g.p.stress) + "\nHealth:"+str(g.p.health) + "\nRest:"+str(g.p.rest) + "\nHappiness:"+str(g.p.readiness), font = "times 10", height=5)
stat.place(x=650,y=0)

study= tk.Button(window,text='Go to Library', command=lambda:review())
study.place(x=250, y=430)

gym = tk.Button(window,text='Workout Time!', command=lambda:gym())
gym.place(x=510, y=430)

relax = tk.Button(window,text='Go Do Something Fun', command=lambda:relax())
relax.place(x=340, y=430)



def review():
    window.destroy()
    g.p.happiness-=9
    g.p.rest-=8
    g.p.readiness+=10
    g.p.stress-=8
    g.p.health-=7
    import day9c1

def gym():
    window.destroy()
    g.p.health+=7
    g.p.happiness +=9
    g.p.stress+=7
    g.p.readiness-=4
    g.p.rest-=7

    import day9c1

def relax():
    window.destroy()
    g.p.health+=6
    g.p.happiness +=8
    g.p.stress-=7
    g.p.readiness-=5
    g.p.rest+=8

    import day9c1

window.mainloop()
