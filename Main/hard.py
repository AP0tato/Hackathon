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

q1 = tk.Label(window, text = "What is called when muscles stiffen from not being used?:")
q1.grid(column = 0, row = 2)

menu1 = tk.OptionMenu(window,ans1,"epiphany","symphony","atrophy", "decay")
menu1.grid(column=2,row=2)

q2 = tk.Label(window, text = "How many chambers are in the heart?")
q2.grid(column = 0, row = 3)

menu2 = tk.OptionMenu(window, ans2, "4","5","6", "7")
menu2.grid(column=2,row=3)

q3 = tk.Label(window, text = "What are potatoes clasified as?")
q3.grid(column = 0, row = 4)

menu3 = tk.OptionMenu(window, ans3, "vegetables","starch","protein", "fat")
menu3.grid(column=2,row=4)

submit = tk.Button(window,text='Submit', command=lambda:tally())
submit.grid(column=0, row = 5)

def tally():
    tally = 0
    if ans1.get() == "atrophy":
        tally+=1
    if ans2.get() == "4":
        tally+=1
    if ans3.get() == "starch":
        tally+=1
    
    
    score = tk.Label(window, text = str(tally)+"/3", font = "times 20", height = 0, width = 0)
    score.grid(column = 0, row =6)

    cont = tk.Button(window,text='Continue', command=lambda:end())
    cont.grid(column=0, row = 7)


def end():
    window.destroy()
    import end


window.mainloop()
