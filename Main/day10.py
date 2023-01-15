import tkinter as tk
import Globals as g

window = tk.Tk()

myVar = tk.StringVar(window)
myVar.set("Select")


window.title("Testing Day!")

w = 800 
h = 500 

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight() 

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)


window.geometry('%dx%d+%d+%d' % (w, h, x, y))

title = window.title()

day  = tk.Label(window, text = "Testing Day", font = "times 20", height = 0, width = 0)
day.place(x=0,y=0)

message = tk.Label(window, text = "It's finally, the day is here.\nI have spent these days getting ready even though it was hard.\n\nI can do this!", font = "times 10", height=5, bg = "white")
message.place(x=245,y=340)

stat = tk.Label(window, text = "Stress:"+str(g.p.stress) + "\nHealth:"+str(g.p.health) + "\nRest:"+str(g.p.rest) + "\nHappiness:"+str(g.p.readiness), font = "times 10", height=5)
stat.place(x=650,y=0)


test = tk.Button(window,text='Take Test', command=lambda:test())
test.place(x=370, y=430)



def test():
    total = g.p.stress * -1 + g.p.health + g.p.rest + g.p.happiness + g.p.readiness

    window.destroy()

    if total >=265:
        if g.p.rest<60:
            import sleepDeprived
        elif g.p.readiness<60:
            import hard
        
        import easy
    else:
        import hard

window.mainloop()
