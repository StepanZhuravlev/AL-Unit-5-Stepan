from tkinter import *
from tkinter import messagebox


def back_to_menu(current, menu):
    """Destroys current, reveals menu (MENU NEEDS TO HAVE BEEN HIDDEN USING .withdraw() IN ORDER TO BE REVEALED)"""
    current.destroy()
    menu.deiconify()


def closing_using_x(current, menu):
    """Runs when the user tries to close a window using the "X" button.
    Asks the user if they want to quit, closes all windows if they do"""
    if messagebox.askokcancel("", "Do you want to quit?"):  # the windows get closed if askokcancel() evaluates to True
        current.destroy()
        menu.destroy()
