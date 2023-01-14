from pynput import keyboard
import tkinter as tk
import _thread as th
import sys

class Player:
    xVelocity = 0.0
    yVelocity = 0.0
    stress = 0  # Max 100
    health = 80 # Max 100, factors such as eating habits and physical activity

p = Player()

def on_press(key):
    try:
        if(key.char=='w'):
            p.yVelocity = 1.0
        elif(key.char=='s'):
            p.yVelocity = -1.0
        elif(key.char=='a'):
            p.xVelocity = -1.0
        elif(key.char=='d'):
            p.xVelocity = 1.0
    except AttributeError:
        pass

def on_release(key):
    if key==keyboard.Key.esc:
        sys.exit(0)
    elif( key.char=='w' or key.char=='s' or key.char=='a' or key.char=='d' ):
        p.xVelocity = 0.0
        p.yVelocity = 0.0

def Main():
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

    #blank setup, maybe a start screen?
window = tk.Tk()

myVar = tk.StringVar(window)
myVar.set("Select")


window.title("Game")
window.geometry("800x500")
title = window.title()

play = tk.Label(window, text='Play Game', font='times 25')
play.pack(fill='both',expand=True)

playBtn = tk.Button(window,text='Play', command=lambda:show_window())
playBtn.place(x=250, y=340)

quitBtn = tk.Button(window,text='Quit', command=lambda:quit_window())
quitBtn.place(x=550, y=340)

def show_window():
    window.destroy()
    import gameStart

def quit_window():
    window.destroy()



window.mainloop()


if __name__=="__main__":
    pass
