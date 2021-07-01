import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox

mydb = mysql.connector.connect(user='lifechoices', password='@lifechoices1234', host='127.0.0.1', database='Hospital',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

window = tk.Tk()
window.title("Login Page")
window.geometry("500x300")

userx = Label(window, text="please enter username")
userx.place(x=75, y=60)
user_ent = Entry(window)
user_ent.place(x=250, y=60)
passx = Label(window, text="please enter password")
passx.place(x=75, y=100)
pass_ent = Entry(window)
pass_ent.place(x=250, y=100)


def check():
    xy = mycursor.execute('select user,password from Login')
    for i in mycursor:
        print(i)
        if user_ent.get() == i[0] and pass_ent.get() == i[1]:
            messagebox.showinfo("success", "You successfully logged in")
            window.destroy()
            root = Tk()
            root.title("welcome user")
            root.geometry("300x200")
            welcome_label = Label(root, text="welcome user you successfully logged in")
            welcome_label.place(x=20, y=80)
    else:
        messagebox.showerror("error", "the supplied information is incorrect")
        user_ent.delete(0, END)
        pass_ent.delete(0, END)


def erase():
    user_ent.delete(0, END)
    pass_ent.delete(0, END)


loginBTN = Button(window, text="Login", command=check, bg="magenta")
loginBTN.place(x=80, y=200)
clearBTN = Button(window, text="Clear", command=erase, bg="magenta")
clearBTN.place(x=230, y=200)
exitBTN = Button(window, text="Exit", command=exit, bg="magenta")
exitBTN.place(x=380, y=200)

window.mainloop()
