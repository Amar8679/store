from msilib.schema import File
import mysql.connector as sql
from tkinter import *
from PIL import Image,ImageTk
import os
import sys

from mysqlx import SqlStatement


if sys.argv:
    filepath = sys.argv[0]
    folder, filename = os.path.split(filepath)
    os.chdir(folder)

'''ufp = input()''' #remove if not working

Sell = Tk()

Sell.geometry('1000x500')

image = Image.open("C:\\Users\\thvai\\OneDrive\\Desktop\\Store\\camera1.png")

resize_image = image.resize((200, 100))

img = ImageTk.PhotoImage(resize_image)

def listing():

    item = Tk()
    
    item.geometry('300x300')

    userlvl = Label(item, text = "Username :")
    userlvl.place(x = 50, y = 80)

    user1 = Entry(item, textvariable = StringVar())
    user1.place(x = 150, y = 80)
    User1 = user1.get()
    
    Itm1 = Label(item, text = 'Enter file path:')
    Itm1.place(x = 50, y = 120)

    Item1 = Entry(item, textvariable = StringVar())
    Item1.place(x = 150, y = 120)

    def query1():

        def insert_blob(FilePath):
            with open(FilePath, "rb") as File:
                BinaryData = File.read()

            #SQLStatement = "update sell set item1 ='{}' where username = '{}'".format(I1, User1)

            SQLStatement = "Insert into sell(item1) values(%s)"

            cur.execute(SQLStatement, (BinaryData, ))
            db.commit()

        I1 = Item1.get()
        
        #New_item = I1.replace('\\','/') #make proper statement

        db = sql.connect(host = "localhost", user = "root", passwd = "778240",database = "login")
        cur = db.cursor()
    
        insert_blob(I1)
        db.commit()


    enter = Button(item, text = "Enter", command = query1, bd = 0)
    enter.configure(bg = "blue")
    enter.place(x = 138, y = 175)

    


'''listing = Label(text="LIST ITEM")
listing.place(x=140,y=160)'''

'''label1 = Label(image=img)
label1.image = img
label1.place(x=20,y=30)'''

Listing = Button(Sell, text= "List Item", image = img,command=listing, width= 200)
Listing.place(x=50,y=50)

Sell.mainloop()

