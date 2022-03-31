from tkinter import *
from tkinter import messagebox


def back_to_menu(current, menu):
    """Destroys current, reveals menu (MENU NEEDS TO HAVE BEEN HIDDEN USING .withdraw() IN ORDER TO BE REVEALED)"""
    current.destroy()
    menu.deiconify()


def close_all_on_x(*windows):
    """Destroys all passed windows"""
    if messagebox.askokcancel("Quit?", "Do you want to quit?"):
        for window in windows:
            window.destroy()
