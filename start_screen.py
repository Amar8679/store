from tkinter import *

Start = Tk()

Start.configure(bg='SlateBlue2')

Start.geometry('1000x500')

def selling():
    Start.destroy()
    import S_Login

def buying():
    Start.destroy()
    import B_Login

title = Label(Start, text="ONLINE STORE",font=("DejaVu",24),width=40,height=5,bg='SlateBlue2',fg='gold')
title.place(x=120,y=10)

    
Selling = Button(Start, text= "Seller", command= selling,fg= "white",bg="black", width= 30,height=10,font='STIX')
Selling.place(x=100,y=150)

Buyer = Button(Start, text= "Buyer", command= buying,fg= "white",bg="black", width= 30,height=10,font='STIX')
Buyer.place(x=550,y=150)

Start.mainloop()