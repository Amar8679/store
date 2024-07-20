#Import the library
import mysql.connector as mc
import tkinter as tk
from tkinter import font

#Create an instance of window
Login_win = tk.Tk()

#Set the geometry of the window
Login_win.geometry("700x400")
   
def SignUp():
   Login=mc.connect(host='localhost',user='root',password='778240',database='Project') 
   cursor = Login.cursor()
   query = 'select * from login where name = "{}"',format(u_entry)
   cursor.execute(query)
   
   
   Login_win.destroy()
   a = tk.Tk()
   a.geometry("400x200")

#Create a Label
username = tk.Label(Login_win,text="Username",font=('Helvetica bold', 20),fg="black")
username.place(x=220,y=30)
u_entry = tk.Entry(Login_win,font=('arial',16),bg='white')
u_entry.place(x=220,y=70)

password = tk.Label(Login_win,text="Password",font=('Helvetica bold', 20),fg="black")
password.place(x=220,y=110)
p_entry = tk.Entry(Login_win, font=('arial',16),bg='white')
p_entry.place(x=220,y=150)


b = tk.Button(Login_win, text= "Sign Up", command= SignUp,fg= "white",bg="black", width= 20)
b.place(x=270,y=190)

#win.withdraw()
Login_win.mainloop()