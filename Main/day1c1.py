import tkinter as tk
import Globals as g

window = tk.Tk()

myVar = tk.StringVar(window)
myVar.set("Select")

window.title("Day 1")
w = 800 
h = 500 

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight() 

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))
title = window.title()

day  = tk.Label(window, text = "Day 1", font = "times 20", height = 0, width = 0)
day.place(x=0,y=0)

message = tk.Label(window, text = "Today is the first day, I've decided to start small. Good in, good out!\nSo what should I eat?", font = "times 10", height=5, bg = "white")
message.place(x=245,y=340)

stat = tk.Label(window, text = "Stress:"+str(g.p.stress) + "\nHealth:"+str(g.p.health) + "\nRest:"+str(g.p.rest) + "\nHappiness:"+str(g.p.readiness), font = "times 10", height=5)
stat.place(x=650,y=0)

fast = tk.Button(window,text='Fast Food', command=lambda:unhealthy())
fast.place(x=260, y=430)

cook = tk.Button(window,text=' Homecooked', command=lambda:healthy())
cook.place(x=460, y=430)

def unhealthy():
    window.destroy()

    g.p.health -= 5 
    g.p.happiness += 5 if g.p.happiness+5 < 100 else 0
    g.p.stress += 2 if g.p.stress+2 < 100 else 0

    import day1c2

def healthy():
    window.destroy()

    g.p.health += 5 if g.p.health+5 < 100 else 0
    g.p.happiness -= 5
    g.p.stress += 2 if g.p.stress+2 < 100 else 0

    import day1c2

window.mainloop()


# stat = tk.Text(window, height=5, font="times 16", takefocus=0, bg='white')
# stat.insert('1.0', "Stress: "+str(g.p.stress) + "\nHealth: "+str(g.p.health) + "\nRest: "+str(g.p.rest) + "\nHappiness: "+str(g.p.happiness) + "\nReadiness: "+str(g.p.readiness))

# stat.tag_add("Stress", 1.8, 2.0)
# stat.tag_config("Stress", foreground='#3ade65' if g.p.stress<87 else '#de4040' if g.p.stress>=93 else '#f0ac37')

# stat.tag_add("Health", 2.8, 3.0)
# stat.tag_config("Health", foreground='#3ade65' if g.p.stress<=87 else '#de4040' if g.p.stress>=93 else '#f0ac37')

# stat.tag_add("Rest", 3.6, 3.8)
# stat.tag_config("Rest", foreground='#3ade65' if g.p.stress<=87 else '#de4040' if g.p.stress>=93 else '#f0ac37')

# stat.tag_add("Happiness", 4.11, 4.13)
# stat.tag_config("Happiness", foreground='#3ade65' if g.p.stress<=87 else '#de4040' if g.p.stress>=93 else '#f0ac37')

# stat.tag_add("Readiness", 5.11, 5.13)
# stat.tag_config("Readiness", foreground='#3ade65' if g.p.stress<=87 else '#de4040' if g.p.stress>=93 else '#f0ac37')

# stat.config(state="disabled")
# stat.pack()
# stat.place(x=690,y=0)
