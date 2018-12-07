from tkinter import *

root= Tk()
root.geometry('500x500')
canvas = Canvas(root, width=500, height=500)
canvas.pack()

a = canvas.create_rectangle(10,30,60,35)
canvas.move(a,20,20)
