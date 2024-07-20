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

Sell = Tk()
Sell.configure(bg='Aquamarine')

Sell.geometry('1000x500')

image = Image.open("camera1.png")

resize_image = image.resize((200, 100))

img = ImageTk.PhotoImage(resize_image)

def listing():

    item = Tk()
    
    item.geometry('300x300')

    userlvl = Label(item, text = "Username :")
    userlvl.place(x = 50, y = 80)

    user1 = Entry(item, textvariable = StringVar())
    user1.place(x = 150, y = 80)
    
    Itm1 = Label(item, text = 'Enter file path:')
    Itm1.place(x = 50, y = 120)

    Item1 = Entry(item, textvariable = StringVar())
    Item1.place(x = 150, y = 120)

    def query1():

        def insert_blob(FilePath):
            with open(FilePath, "rb") as File:
                BinaryData = File.read()

            #SQLStatement = "update sell set item1 ='{}' where username = '{}'".format(I1, User1)

            SQLStatement = "Insert into images(photo) values(%s)"

            cur.execute(SQLStatement, (BinaryData, ))
            db.commit()

        I1 = Item1.get()

        db = sql.connect(host = "localhost", user = "root", passwd = "778240",database = "login")
        cur = db.cursor()
    
        insert_blob(I1)
        db.commit()


    enter = Button(item, text = "Enter", command = lambda:[query1(),item.destroy()], bd = 0)
    enter.configure(bg = "blue")
    enter.place(x = 138, y = 175)

Listing = Button(Sell, image = img,command=lambda:[listing(),Sell.destroy()], width= 200)
Listing.place(x=50,y=50)

def Retrieve_blob(ID):

        db = sql.connect(host = "localhost", user = "root", passwd = "778240",database = "login")
        cur = db.cursor()
        cur.execute('create table if not exists images(Id int primary key,Photo longblob)')
        SQLStatement = "select * from images where ID ='{0}'"
        cur.execute(SQLStatement.format(str(ID)))
        result = cur.fetchone()[1]
        StoreFilePath = "Image_outputs./{0}.jpg".format(str(ID))
        print(result)
        with open(StoreFilePath, 'wb') as File:
            File.write(result)
            File.close()

'''db = sql.connect(host = "localhost", user = "root", passwd = "778240",database = "login")
cur1 = db.cursor()
query = "Select max(id) from images"
cur1.execute(query)
myresult = cur1.fetchall()
Retrieve_blob(1)'''

Sell.mainloop()
