# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 22:11:14 2022

@author: Suthapalli.Akhil
"""

import tkinter as tk
from tkinter import Label, YES, BOTH
import os, threading, time
from PIL import Image, ImageTk


root = tk.Tk()
os.chdir("E:\\HUD\\MockImages")
running = True
width = 0
height = 0
rotate = 0
img = []

load_image_temp = Image.open("A1.png")
imgA1 = Image.open("A1.png")
imgA2 = Image.open("A2.png")
imgA3 = Image.open("A3.png")
imgA4 = Image.open("A4.png")
imgA5 = Image.open("A5.png")
imgA6 = Image.open("A6.png")
imgA7 = Image.open("A7.png")

def exit_fun(event):
    global running
    print("Destroyed")
    running = False
    root.destroy()

def loop():
    global label,img
    i=1
    while(running):
        time.sleep(5)
        try:
            label.configure(image = img[i])
        except:
            label.configure(image = load_image)
            print("exception")
            return
        i = i+1
        if i==7:
            i=0




def load_images():
    global img, rotate
    img = []
    imgB1 = imgA1.resize((width,height))
    imgC1 = imgB1.rotate(angle=rotate)
    img1 = ImageTk.PhotoImage(imgC1)

    imgB2 = imgA2.resize((width,height))
    imgC2 = imgB2.rotate(angle=rotate)
    img2 = ImageTk.PhotoImage(imgC2)

    imgB3 = imgA3.resize((width,height))
    imgC3 = imgB3.rotate(angle=rotate)
    img3 = ImageTk.PhotoImage(imgC3)

    imgB4 = imgA4.resize((width,height))
    imgC4 = imgB4.rotate(angle=rotate)
    img4 = ImageTk.PhotoImage(imgC4)

    imgB5 = imgA5.resize((width,height))
    imgC5 = imgB5.rotate(angle=rotate)
    img5 = ImageTk.PhotoImage(imgC5)

    imgB6 = imgA6.resize((width,height))
    imgC6 = imgB6.rotate(angle=rotate)
    img6 = ImageTk.PhotoImage(imgC6)

    imgB7 = imgA7.resize((width,height))
    imgC7 = imgB7.rotate(angle=rotate)
    img7 = ImageTk.PhotoImage(imgC7)

    img = [img1 , img2, img3, img4, img5, img6, img7]

def rotate_fun(event):
    global rotate

    rotate = rotate + 90
    if rotate == 360:
        rotate = 0

    print("rotating to ",rotate)
    load_images()


if __name__ == "__main__" :
    print("App starting")
    root.attributes('-fullscreen', True)
    root.bind("<Button-1>",exit_fun)
    root.bind("<Button-3>",rotate_fun)

    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    load_images()
    #change all images
    imgtemp = load_image_temp.resize((width,height))
    load_image = ImageTk.PhotoImage(imgtemp)

    label = Label(root,image = load_image)
    label.pack(fill = BOTH, expand = YES)
    threading.Thread(target = loop).start()
    root.mainloop()
