from pynput import keyboard
import tkinter as tk
import os
import sys

class Player:
    xVelocity = 0
    yVelocity = 0
    stress = 50  # Max 100
    health = 80 # Max 100, factors such as eating habits and physical activity
    rest = 100
    satisfaction = 80

p = Player()

def on_press(key):
    try:
        if(key.char=='w'):
            p.yVelocity = 1
        elif(key.char=='s'):
            p.yVelocity = -1
        elif(key.char=='a'):
            p.xVelocity = -1
        elif(key.char=='d'):
            p.xVelocity = 1
    except AttributeError:
        pass

def on_release(key):
    if key==keyboard.Key.esc:
        sys.exit(0)
    elif( key.char=='w' or key.char=='s' or key.char=='a' or key.char=='d' ):
        p.xVelocity = 0
        p.yVelocity = 0

def Main():
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

    os.system("python3 gameStart.py")

if __name__=="__main__":
    Main()