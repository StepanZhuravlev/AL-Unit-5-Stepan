from tkinter import *


def close_current_open_new(current_window, new_window):
    """Closes <current_window> and opens <new_window>"""
    new_window = Toplevel(current_window)
    new_window.mainloop()
