import tkinter as tk
import Globals as g


window = tk.Tk()

myVar = tk.StringVar(window)
myVar.set("Select")


window.title("Day 7")

w = 800 
h = 500 

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight() 

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))

title = window.title()


day  = tk.Label(window, text = "Day 7", font = "times 20", height = 0, width = 0)
day.place(x=0,y=0)


message = tk.Label(window, text = "I slept in on my day off. There isn't a lot of time left in the day.\nMy old classmates asked me out to a small outing\nI think I deserve a break...", font = "times 10", height=5, bg = "white")
message.place(x=250,y=340)

stat = tk.Label(window, text = "Stress:"+str(g.p.stress) + "\nHealth:"+str(g.p.health) + "\nRest:"+str(g.p.rest) + "\nHappiness:"+str(g.p.readiness), font = "times 10", height=5)
stat.place(x=650,y=0)

friends= tk.Button(window,text='Go With Classmates', command=lambda:friends())
friends.place(x=450, y=430)

review = tk.Button(window,text='Stay Home to Study', command=lambda:review())
review.place(x=240, y=430)



def review():
    window.destroy()
    g.p.happiness-=9
    g.p.rest-=8
    g.p.readiness+=9 if g.p.readiness+9 < 100 else 0
    g.p.stress+=6 if g.p.stress+6 < 100 else 0
    g.p.health -= 8
    import day8

def friends():
    window.destroy()
    g.p.happiness +=9 if g.p.happiness+9 < 100 else 0
    g.p.stress+=3 if g.p.stress+3 < 100 else 0
    g.p.readiness-=7
    g.p.rest-=8

    import day8

window.mainloop()
