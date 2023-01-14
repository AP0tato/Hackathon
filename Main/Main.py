import keyboard as key
import tkinter as tk
import _thread as th

def CheckInput():
    while True:
        try:
            if(key.is_pressed()):
                print(1)
        except:
            continue

def Main():
    pass

if __name__=="__main__":
    pass