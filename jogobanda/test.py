import pygame
from tkinter import *
 
def play():
  pygame.mixer.music.load('musica.mp3')
  pygame.mixer.music.play()
 
def pause():
  pygame.mixer.music.pause()
 
def unpause():
  pygame.mixer.music.unpause()

pygame.init()
 
root = Tk()
root.geometry('180x180')
 
myframe = Frame(root)
myframe.pack()
 
mylabel = Label(myframe, text = "It's Mario!")
mylabel.pack()
 
button1 = Button(myframe, text = "Play", command = play, width = 15)
button1.pack(pady = 5)
button2 = Button(myframe, text = "Pause", command = pause, width = 15)
button2.pack(pady = 5)
button3 = Button(myframe, text = "Unpause", command = unpause, width = 15)
button3.pack(pady = 5)
button4 = Button(myframe, text = "Sair", command = root.destroy, width = 15)
button4.pack(pady = 5)
 
root.mainloop()