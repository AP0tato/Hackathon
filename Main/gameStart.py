import tkinter as tk

def show_window(window):
        window.destroy()
        import day1c1

def run():
    window = tk.Tk()
    window.resizable(False, False)
    window.geometry('800x500')

    myVar = tk.StringVar(window)
    myVar.set("Select")

    window.title("Intro")
    window.geometry("800x500")
    title = window.title()

    welcomeLabel = tk.Label(window, text = "Culminating Time (n.)\n\n A stressful time where students forget to balance out studying and health\n\nAnd I'm no different. But I won't this time.", height = 100, width = 500)
    welcomeLabel.pack()

    contBtn = tk.Button(window,text='Continue', command=lambda:show_window(window))
    contBtn.place(x=360, y=340)

    window.mainloop()
