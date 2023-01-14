import tkinter as tk

window = tk.Tk()

myVar = tk.StringVar(window)
myVar.set("Select")


window.title("Day 2.1")
window.geometry("800x500")
title = window.title()


day  = tk.Label(window, text = "Day 2", font = "times 20", height = 0, width = 0)
day.place(x=0,y=0)


message = tk.Label(window, text = "It's a new day! I have quite some time before class. What should I do now that I'm ready?", font = "times 10", height=5, bg = "white")
message.place(x=205,y=340)

exercise = tk.Button(window,text='Exercise', command=lambda:phys())
exercise.place(x=260, y=430)

hobby = tk.Button(window,text='Do a Hobby', command=lambda:hobby())
hobby.place(x=460, y=430)



def phys():
    #points to physical health
    window.destroy()
    import day2c2

def hobby():
    #points to happiness
    window.destroy()
    import day2c2

window.mainloop()