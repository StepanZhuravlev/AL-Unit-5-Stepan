from tkinter import *
from tkinter import messagebox


def login():
    """
    For now, the valid username and password are "admin" and "password" respectively
    """
    username = username_ent.get()
    password = password_ent.get()
    
    if username == "admin" and password == "password":
        return messagebox.showinfo("", "Login successful")
    else:
        return messagebox.showerror("Error", "Username and password combination is invalid")

login_screen = Tk()
login_screen.title("Login Screen")
login_screen.geometry("250x100")
login_screen.resizable(width=False, height=False)


frm1 = Frame(login_screen)
frm1.pack()

username_lbl = Label(frm1, text="Username :", width=10)
username_lbl.grid(row=0, column=0, pady=5)
username_ent = Entry(frm1)
username_ent.grid(row=0, column=1, pady=5, padx=5)

password_lbl = Label(frm1, text="Password :", width=10)
password_lbl.grid(row=1, column=0, pady=5)
password_ent = Entry(frm1)
password_ent.grid(row=1, column=1, pady=5, padx=5)

frm2 = Frame(login_screen)
frm2.pack()

login_btn = Button(text="Login", command=login)
login_btn.pack(pady=5)


    