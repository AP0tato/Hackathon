from pynput import keyboard
import tkinter as tk
import os
import gameStart
import sys

class Player:
    stress = 50  # Max 100
    health = 80 # Max 100, factors such as eating habits and physical activity
    rest = 100
    satisfaction = 80

p = Player()

def on_press(key):
    try:
        pass
    except AttributeError:
        pass

def on_release(key):
    if():
        pass
    elif():
        pass

def Main():
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

    v = gameStart()

if __name__=="__main__":
    Main()