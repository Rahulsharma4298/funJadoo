from tkinter import *
import PIL.Image, PIL.ImageTk
import winsound
import pygame
import time

WIDTH = 720
HEIGHT = 480
global count
count = 0
pygame.init()


def start(event):
    winsound.Beep(4000, 50)
    updateImg()
    time.sleep(0.4)
    img = PIL.Image.open("img1.png")
    img = PIL.ImageTk.PhotoImage(img)
    canvas.image = img
    canvas.create_image(0, 0, anchor=NW, image=img)
    root.bind('<Key>', press)

def press(event):
    global count
    kp = event.char
    print ("pressed", kp)


    if kp == 'b':
        print("b played")
        img = PIL.Image.open("img2.png")
        img = PIL.ImageTk.PhotoImage(img)
        canvas.image = img
        canvas.create_image(0, 0, anchor=NW, image=img)
        pygame.mixer.music.load("b.mp3")
        pygame.mixer.music.play()
        count+=1


    if kp == 'c':
        print("c played")
        img = PIL.Image.open("img3.png")
        img = PIL.ImageTk.PhotoImage(img)
        canvas.image = img
        canvas.create_image(0, 0, anchor=NW, image=img)
        pygame.mixer.music.load("c.mp3")
        pygame.mixer.music.play()
        count+=1

    if kp == 'f':
        print("f played")
        img = PIL.Image.open("img4.png")
        img = PIL.ImageTk.PhotoImage(img)
        canvas.image = img
        canvas.create_image(0, 0, anchor=NW, image=img)
        pygame.mixer.music.load("f.mp3")
        pygame.mixer.music.play()
        count+=1

    if kp == 'e':
        img = PIL.Image.open("img1.png")
        img = PIL.ImageTk.PhotoImage(img)
        canvas.image = img
        canvas.create_image(0, 0, anchor=NW, image=img)
        print("e played")
        pygame.mixer.music.load("e.mp3")
        pygame.mixer.music.play()
        count+=1

    if kp == 'h':
        pygame.mixer.music.load("bcef.mp3")
        pygame.mixer.music.play()
        count+=1

    if kp == 'd':
        pygame.mixer.music.load("d.mp3")
        pygame.mixer.music.play()
        count+=1

    print(count)
    if count>12:
        contactJadoo()



def contactJadoo():
    print("Contacting Jadoo...")
    return





def updateImg():
    print("Image Change")
    wImg = PIL.Image.open("jadoo.png")
    welcomeImg = PIL.ImageTk.PhotoImage(wImg)
    canvas.image = welcomeImg
    canvas.create_image(0, 0, image=welcomeImg, anchor=NW)
    canvas.update()

    


root = Tk()
root.title("Jadoo Simulator by RjRahul")
root.geometry("720x480")
root.resizable(0, 0)

canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
wImg = PIL.Image.open("main_sc.png")
welcomeImg = PIL.ImageTk.PhotoImage(wImg)
canvas.image = welcomeImg
canvas.create_image(0, 0, image=welcomeImg, anchor=NW)


root.bind('<Return>', start)




root.mainloop()
