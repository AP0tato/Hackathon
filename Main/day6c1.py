import tkinter as tk
import Globals as g


window = tk.Tk()

myVar = tk.StringVar(window)
myVar.set("Select")


window.title("Day 6.1")

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


message = tk.Label(window, text = 'The teacher has organized a review session, but it runs for most of the evening. \nClasses felt so long and I feel so stiff. And hungry.\nMy friends are going out to eat later too. ', font = "times 10", height=5, bg = "white")
message.place(x=250,y=340)

stat = tk.Label(window, text = "Stress:"+str(g.p.stress) + "\nHealth:"+str(g.p.health) + "\nRest:"+str(g.p.rest) + "\nHappiness:"+str(g.p.readiness), font = "times 10", height=5)
stat.place(x=650,y=0)

friends= tk.Button(window,text='Go With Friends', command=lambda:friends())
friends.place(x=250, y=430)


gym = tk.Button(window,text='Work Out a Bit', command=lambda:gym())
gym.place(x=390, y=430)

review = tk.Button(window,text='Go to Review Session', command=lambda:review())
review.place(x=510, y=430)



def review():
    window.destroy()
    g.p.happiness-=8
    g.p.rest-=7
    g.p.readiness+=9
    g.p.stress-=4
    import day6c2

def gym():
    window.destroy()
    g.p.health+=7 if g.p.health+7 < 100 else 0
    g.p.happiness +=8 if g.p.happiness+8 < 100 else 0
    g.p.stress+=8 if g.p.stress+8 < 100 else 0
    g.p.readiness-=4

    import day6c2

def friends():
    window.destroy()
    g.p.health-=4
    g.p.happiness +=9 if g.p.happiness+9 < 100 else 0
    g.p.stress+=7 if g.p.stress+7 < 100 else 0
    g.p.readiness-=5

    import day6c2

window.mainloop()
