from tkinter import *

phrase = input("Enter phrase: ").upper()

window = Tk()
canvas = Canvas(width=1024, height=1024, background='#F78C58')
coords = open('coords.txt', 'r')
for line in coords:
    canvas.create_text(int((line.rstrip().split(' '))[0]), int((line.rstrip().split(' '))[1]), anchor='nw', font='Helvetica 20 bold', text=phrase)


canvas.pack()
