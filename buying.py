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

x = True
while x == True:
    
    Buy = Tk()
    Buy.configure(bg='Aquamarine')

    Buy.geometry('1050x500')

    def Page_destroy():
        global x
        x = False
        Buy.destroy()

    def BuyNow():
        win = Tk()

        win.configure(bg='goldenrod')
        
        win.geometry('500x500')
        l = Label(win,text='ORDER PLACED!',bg = 'goldenrod',font='STIX')
        l.place(relx=0.35,rely=0.4)
        def win_des():
            win.destroy()
        b = Button(win,text='Quit',command=win_des,width=20)
        b.place(relx=0.35,rely=0.8)

    def Details():

        win = Tk()
        win.geometry('500x500')
        win.configure(bg='DarkGoldenrod2')

        userlvl = Label(win, text = "Credit card info:",bg='DarkGoldenRod2')
        Or = Label(win, text = "OR",bg='DarkGoldenRod2')
        user1 = Entry(win, textvariable = StringVar())

        var1 = IntVar()
        x = Checkbutton(win, text="Cash on delivery", variable=var1,bg = 'DarkGoldenRod2')
        x.place(x=200,y=320)

        user1.place(x =240, y = 160)
        Or.place(x = 200, y = 240)
        userlvl.place(x = 120, y = 160)
        
        userlvl = Label(win, text = "Username :",bg='DarkGoldenRod2')
        Or = Label(win, text = "Password  :",bg='DarkGoldenRod2')

        user1 = Entry(win, textvariable = StringVar())

        def win_des():
            win.destroy()
        b = Button(win,text='Place Order',command=lambda:[win_des(),BuyNow()],width=20)
        b.place(relx=0.35,rely=0.8)

        
    Quit = Button(Buy, text= "Quit", command=Page_destroy, width= 20, bg = 'blue', fg = 'black')
    Quit.place(relx= 0.4 , rely= 0.9)

    def Mobile():
        Buy.destroy()
    
        Desc = Tk()
        Desc.configure(bg='pale green')
        Desc.geometry('500x500')

        def Desc_destroy():
            Desc.destroy()

        def End():
            global x
            x = False

        resize_image = mobile.resize((400, 200))
        img = ImageTk.PhotoImage(resize_image)
    
        label = Label(image=img)
        label.mobile = img
        label.place(x=50,y=50)

        back = Button(Desc, text= "back", command=Desc_destroy, width= 20, bg = 'blue', fg = 'black')
        back.place(relx= 0.0 , rely= 0.95)

        mb_desc = '\tTouchscreen Phone with \n \t  1) 108 megapixel camera \n2) 6 Gb RAM \n      3) 64 Gb storage \n    Price: Rs 17500'
        desc = Label(Desc, text = mb_desc, bg = 'pale green', font='STIX')
        desc.place(relx=0.05,rely=0.6)

        buynow = Button(Desc,text = "BUY NOW", command=lambda:[Details(),Desc_destroy(),End()], width= 20)
        buynow.place(relx=0.7,rely=0.95)
    

    mobile = Image.open("mobile.jfif")
    resize_image = mobile.resize((200, 100))
    img = ImageTk.PhotoImage(resize_image)
    Listing = Button(Buy, image = img, command=Mobile, width= 200)
    Listing.place(x=50,y=50)

    def Laptop():
        Buy.destroy()
    
        Desc = Tk()
        Desc.configure(bg='pale green')
        Desc.geometry('500x500')

        def Desc_destroy():
            Desc.destroy()

        def End():
            global x
            x = False

        resize_image = laptop.resize((400, 200))
        img1 = ImageTk.PhotoImage(resize_image)
    
        label1 = Label(image=img1)
        label1.laptop = img1
        label1.place(x=50,y=50)

        back = Button(Desc, text= "back", command=Desc_destroy, width= 20, bg = 'blue', fg = 'black')
        back.place(relx= 0.0 , rely= 0.95)

        mb_desc = '\t16 Inch Laptop with \n \t      1) 6 Gb Graphics Card  \n        2) 16 Gb RAM \n        3) 1 Tb storage \n        Price: Rs 60000'
        desc = Label(Desc, text = mb_desc, bg = 'pale green', font='STIX')
        desc.place(relx=0.05,rely=0.6)

        buynow = Button(Desc,text = "BUY NOW", command=lambda:[Details(),Desc_destroy(),End()], width= 20)
        buynow.place(relx=0.7,rely=0.95)
    
        #enter description as label and add image with buy now option

    laptop = Image.open("laptop.jfif")
    resize_image = laptop.resize((200, 100))
    img1 = ImageTk.PhotoImage(resize_image)
    Listing1 = Button(Buy, image = img1, command=Laptop, width= 200)
    Listing1.place(x=300,y=50)

    def Camera():
        Buy.destroy()
    
        Desc = Tk()
        Desc.configure(bg='pale green')
        Desc.geometry('500x500')

        def Desc_destroy():
            Desc.destroy()

        def End():
            global x
            x = False

        resize_image = camera.resize((400, 200))
        img2 = ImageTk.PhotoImage(resize_image)
    
        label2 = Label(image=img2)
        label2.camera = img2
        label2.place(x=50,y=50)

        back = Button(Desc, text= "back", command=Desc_destroy, width= 20, bg = 'blue', fg = 'black')
        back.place(relx= 0.0 , rely= 0.95)

        mb_desc = '\tMirrorless Camera \n \t  1) Full Frame Sensor \n          2) 24 Megapixel \n         Price: Rs 35000'
        desc = Label(Desc, text = mb_desc, bg = 'pale green', font='STIX')
        desc.place(relx=0.05,rely=0.6)

        buynow = Button(Desc,text = "BUY NOW", command=lambda:[Details(),Desc_destroy(),End()], width= 20)
        buynow.place(relx=0.7,rely=0.95)
    
        #enter description as label and add image with buy now option

    camera = Image.open("camera01.webp")
    resize_image = camera.resize((200, 100))
    img2 = ImageTk.PhotoImage(resize_image)
    Listing2 = Button(Buy, text= "List Item", image = img2, command=Camera, width= 200)
    Listing2.place(x=550,y=50)


    def Speakers():
        Buy.destroy()
    
        Desc = Tk()
        Desc.configure(bg='pale green')
        Desc.geometry('500x500')

        def Desc_destroy():
            Desc.destroy()

        def End():
            global x
            x = False

        resize_image = speakers.resize((400, 200))
        img3 = ImageTk.PhotoImage(resize_image)
    
        label3 = Label(image=img3)
        label3.speakers = img3
        label3.place(x=50,y=50)

        back = Button(Desc, text= "back", command=Desc_destroy, width= 20, bg = 'blue', fg = 'black')
        back.place(relx= 0.0 , rely= 0.95)

        mb_desc = '\tDolby Speakers with \n \t  1) 5.1 Surround Sound \n\t 2) upto 105 db sound \n       Price: Rs 15000'
        desc = Label(Desc, text = mb_desc, bg = 'pale green', font='STIX')
        desc.place(relx=0.05,rely=0.6)

        buynow = Button(Desc,text = "BUY NOW", command=lambda:[Details(),Desc_destroy(),End()], width= 20)
        buynow.place(relx=0.7,rely=0.95)
    
        #enter description as label and add image with buy now option

    speakers = Image.open("speakers.jpg")
    resize_image = speakers.resize((200, 100))
    img3 = ImageTk.PhotoImage(resize_image)
    Listing3 = Button(Buy, text= "List Item", image = img3, command=Speakers, width= 200)
    Listing3.place(x=800,y=50)

    mainloop()
