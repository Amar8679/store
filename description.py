from msilib.schema import File
import mysql.connector as sql
from tkinter import *
from PIL import Image,ImageTk
import os
import sys

from mysqlx import SqlStatement

Desc = Tk()
Desc.geometry('500x500')

def Buy():
    Desc.destroy
    import buying

def Speaker():
    
    speakers = Image.open("C:\\Users\\thvai\\OneDrive\\Desktop\\Store\\speakers.jpg")
    resize_image = speakers.resize((400, 200))
    img3 = ImageTk.PhotoImage(resize_image)
    
    label3 = Label(image=img3)
    label3.speakers = img3
    label3.place(x=50,y=50)
        
    #enter description as label and add image with buy now option

    buy = Button(Desc, text= "back", command=Buy, width= 20, bg = 'blue', fg = 'black')
    buy.place(relx= 0.0 , rely= 0.95)

Speaker()

mainloop()
