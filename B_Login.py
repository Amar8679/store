import mysql.connector as sql
from tkinter import *
from PIL import Image,ImageTk
import os
import sys

if sys.argv:
    filepath = sys.argv[0]
    folder, filename = os.path.split(filepath)
    os.chdir(folder)


win = Tk()

win.configure(bg='DarkGoldenRod2')

win.geometry("1000x500")

win.title("Login Page")


def login() :

    db = sql.connect(host = "localhost", user = "root", passwd = "778240")

    cur = db.cursor()


    try :

        cur.execute("create database login")

        db = sql.connect(host = "localhost", user = "root", passwd = "778240", database = "login")

        cur = db.cursor()


    except sql.errors.DatabaseError:

        db = sql.connect(host = "localhost", user = "root", passwd = "778240", database = "login")

        cur = db.cursor()


        try :

            cur.execute("create table main(username varchar(50), NOT NULL, password int NOT NULL)")


        except sql.errors.ProgrammingError:

            pass


    finally :

        try :

            cur.execute("create table main(username varchar(50) NOT NULL, "

                        "password int NOT NULL)")


        except sql.errors.ProgrammingError:

            pass


    while True :


        user = user1.get()

        passwd = passwd1.get()
        
        cur.execute("select * from main where username = '%s' and password = %s" % (user, passwd))

        rud = cur.fetchall()


        if rud:

            print("Welcome")

            break


        else:

            cur.execute("insert into main values('{}', {})".format(str(user), passwd))

            db.commit()

            print("Account Created")

            break


    cur.close()
    db.close()
    win.destroy()
    import buying

Title = Label(win, text = "Login",bg='DarkGoldenRod2',font='STIX')

userlvl = Label(win, text = "Username :",bg='DarkGoldenRod2')

passwdlvl = Label(win, text = "Password  :",bg='DarkGoldenRod2')

user1 = Entry(win, textvariable = StringVar())

passwd1 = Entry(win, textvariable = IntVar().set(""))


enter = Button(win, text = "Enter", command = lambda: login(), bd = 0)

enter.configure(bg = "blue")

Title.place(x = 830, y = 80)

user1.place(x = 800, y = 160)

passwd1.place(x = 800, y = 240)


userlvl.place(x = 720, y = 160)

passwdlvl.place(x = 720, y = 240)


enter.place(x = 845, y = 350)

user = user1.get()

Log_img = Image.open("Login_image.jpg")
resize_image = Log_img.resize((700, 496))
img = ImageTk.PhotoImage(resize_image)
Log_img = Label(win,image=img)
Log_img.place(relx=0.0,rely=0.0)

win.mainloop()