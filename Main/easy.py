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

day  = tk.Label(window, text = "Exam", font = "times 30", height = 0, width = 0)
day.grid(column = 0, row=1)

q1 = tk.Label(window, text = "What is the recommended number of hours of sleep each night?:")
q1.grid(column = 0, row = 2)

menu1 = tk.OptionMenu(window,ans1,"12","7","10", "8")
menu1.grid(column=2,row=2)

q2 = tk.Label(window, text = "How many bones does an adult have?:")
q2.grid(column = 0, row = 3)

menu2 = tk.OptionMenu(window, ans2, "187","340","206", "93")
menu2.grid(column=2,row=3)

q3 = tk.Label(window, text = "How many food groups are there?:")
q3.grid(column = 0, row = 4)

menu3 = tk.OptionMenu(window, ans3, "13","7","5", "11")
menu3.grid(column=2,row=4)

q4 = tk.Label(window, text = "What is the recommended amount of water to drink each day?:")
q4.grid(column = 0, row =5)

menu4 = tk.OptionMenu(window, ans4, "2.7-3.7L","3.5-4.5L","10.3-12.2L", "8.1-9.4L")
menu4.grid(column=2,row=5)

q5 = tk.Label(window, text = "Balanced mental and physical health have an impact on daily performance:")
q5.grid(column = 0, row =6)

menu5 = tk.OptionMenu(window, ans5, "True","False")
menu5.grid(column=2,row=6)

submit = tk.Button(window,text='Submit', command=lambda:tally())
submit.grid(column=0, row = 7)

def tally():
    tally = 0
    if ans1.get() == "8":
        tally+=1
    if ans2.get() == "206":
        tally+=1
    if ans3.get() == "5":
        tally+=1
    if ans4.get() == "2.7-3.7L":
        tally+=1
    if ans5.get() == "True":
        tally+=1
    
    score = tk.Label(window, text = str(tally)+"/5", font = "times 20", height = 0, width = 0)
    score.grid(column = 0, row =8)

    cont = tk.Button(window,text='Continue', command=lambda:end())
    cont.grid(column=0, row = 9)


def end():
    window.destroy()
    import end



window.mainloop()
