from tkinter import *
from PIL import Image,ImageTk,ImageSequence 
import time
import pygame  
from pygame import mixer
mixer.init()

root = Tk()
root.geometry("2100x800")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open("giphy.gif")
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0
    mixer.music.load("jarvis_plug_in.mp3")
    mixer.music.play()
    
    for img in ImageSequence.Iterator(img):
        img = img.resize((2100,800))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.01)
    root.destroy()

play_gif()
root.mainloop()

