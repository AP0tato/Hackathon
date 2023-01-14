import keyboard as key
import tkinter as tk
import _thread as th
import sys

class Player:
    xVelocity = 0.0
    yVelocity = 0.0
    stress = 0  # Max 100
    health = 80 # Max 100, factors such as eating habits and physical activity

p = Player()

def CheckInput():
    while True:
        try:
            if(key.is_pressed('w')):
                p.yVelocity = 1.0
            elif(key.is_pressed('s')):
                p.yVelocity = -1.0
            elif(key.is_pressed('a')):
                p.xVelocity = -1.0
            elif(key.is_pressed('d')):
                p.xVelocity = 1.0
            elif(key.is_pressed('Esc')):
                sys.exit(0)
            else:
                p.xVelocity = 0.0
                p.yVelocity = 0.0
        except:
            continue

def Main():
    try:
        th.start_new_thread( CheckInput )
    except:
        print("Error: Unable to start thread")

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