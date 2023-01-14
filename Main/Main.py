import keyboard as key
import tkinter as tk
import _thread as th

class Player:
    xVelocity = 0.0
    yVelocity = 0.0
    stress = 0  # Max 100
    health = 80 # Max 100, factors such as eating habits and physical activity

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