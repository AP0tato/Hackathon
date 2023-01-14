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

    window.title("Testing")
    window.geometry("800x500")
    title = window.title()

    welcomeLabel = tk.Label(window, text = "Welcome\nThis is the start! ", height = 5, width = 20)
    welcomeLabel.pack()

    window.mainloop()

if __name__=="__main__":
    Main()