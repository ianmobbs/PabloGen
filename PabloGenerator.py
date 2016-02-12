#Import tkinter library for use to draw image
from tkinter import *

#Ask user for phrase, convert it to all upper case
phrase = input("Enter phrase: ").upper()

#Establish all of our constants
dimension = 1024
bgcolor = '#F78C58'
coords = open('coords.txt', 'r')

#Create a Tkinter canvas
window = Tk()
canvas = Canvas(width=dimension, height=dimension, background=bgcolor)

#Print lines of text to Canvas
for line in coords:
	coord = line.rstrip().split(' ')
	canvas.create_text(int(coord[0]), int(coord[1]), anchor='nw', font='Helvetica 29 bold', text=phrase)

#Pack it all up!
canvas.pack()

###TODO###
#Figure out how to export canvas as JPG
#	Use PIL or QT or something to export?
#	Draw in PIL or QT or something then export?
#Create a Twitter bot, replies to all mentions with image using text
#	Run off Heroku instance?
#	Buy raspberry pi?