import tkinter as tk
import Globals as g

window = tk.Tk()

ans1 = tk.StringVar(window)
ans1.set("Select")

ans2 = tk.StringVar(window)
ans2.set("Select")

ans3 = tk.StringVar(window)
ans3.set("Select")

ans4 = tk.StringVar(window)
ans4.set("Select")

ans5 = tk.StringVar(window)
ans5.set("Select")

window.title("Test")

w = 800 
h = 500 

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight() 

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)


window.geometry('%dx%d+%d+%d' % (w, h, x, y))

title = window.title()

day  = tk.Label(window, text = "Congratulations on Taking the Exam!", font = "times 30", height = 0, width = 0)
day.place(x=0,y=0)

day  = tk.Label(window, text = "Remember, having a balanced life in all aspects keeps you as healthy as possible.", font = "times 15", height = 0, width = 0)
day.place(x=0,y=50)



window.mainloop()
