import keyboard as key
import tkinter as tk
import _thread as th

xVelocity = 0.0
yVelocity = 0.0

def CheckInput():
    while True:
        try:
            if(key.is_pressed('w')):
                yVelocity = 1.0
            elif(key.is_pressed('s')):
                yVelocity = -1.0
            elif(key.is_pressed('a')):
                xVelocity = -1.0
            elif(key.is_pressed('d')):
                xVelocity = 1.0
            else:
                xVelocity = 0.0
                yVelocity = 0.0
        except:
            continue

def Main():
    pass

if __name__=="__main__":
    pass