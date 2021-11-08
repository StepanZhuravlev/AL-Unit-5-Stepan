# root = Tk()
# top = Toplevel()
# top.mainloop()

# "change password" button

from tkinter import *

def open_new(current, new):
    new = Toplevel()
    current.destroy
    

menu_window = Tk()
menu_window.title("Menu")
menu_window.geometry("550x200")
menu_window.resizable(width=False, height=False)

add_book_btn = Button(text = "Add a new book", command = open_new(menu_window, add_book_window))
add_member_btn = Button(text = "Add a new member")
add_loan_btn = Button(text = "Add a new loan")
add_request_btn = Button(text = "Add a new request")
close_menu_btn = Button(text = "Close Menu", command = menu_window.destroy)

add_book_btn.grid(row = 0, column = 0, padx = 5, pady = 5)
add_member_btn.grid(row = 0, column = 1, padx = 5, pady = 5)
add_loan_btn.grid(row = 0, column = 2, padx = 5, pady = 5)
add_request_btn.grid(row = 0, column = 3, padx = 5, pady = 5)
close_menu_btn.grid(row = 0, column = 4, padx = 5, pady = 5)

menu_window.mainloop()