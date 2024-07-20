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

View = Tk()
View.configure(bg='Aquamarine')
View.geometry('500x500')

def Retrieve_blob(ID):

        db = sql.connect(host = "localhost", user = "root", passwd = "778240",database = "login")
        cur = db.cursor()
        SQLStatement = "select * from images where ID ='{0}'"
        cur.execute(SQLStatement.format(str(ID)))
        result = cur.fetchone()[1]
        StoreFilePath = "Image_outputs./{0}.jpg".format(str(ID))
        print(result)
        with open(StoreFilePath, 'wb') as File:
            File.write(result)
            File.close()

db = sql.connect(host = "localhost", user = "root", passwd = "778240",database = "login")
cur1 = db.cursor()
query = "Select max(id) from images"
cur1.execute(query)
myresult = cur1.fetchall()

PicId = Entry(View, textvariable = IntVar().set(""))
PicId.place(x=200,y=200)
Id = PicId.get()
Id = int(Id)
print(Id)
Retrieve_blob(Id)
View.mainloop()