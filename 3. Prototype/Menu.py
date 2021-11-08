# "change password" button

from tkinter import *
    
def destroy_window(window):
    return window.destroy

def open_add_book_window(): # working!
    menu_window.destroy()
    add_book_window = Tk()
    test_lbl = Label(add_book_window, text = "test").pack()
    add_book_window.mainloop()
    
menu_window = Tk()
menu_window.title("Menu")
menu_window.geometry("550x200")
menu_window.resizable(width=False, height=False)

# menu_window buttons:
add_book_btn = Button(menu_window, text = "Add a new book", command = open_add_book_window)
add_member_btn = Button(menu_window, text = "Add a new member")
add_loan_btn = Button(menu_window, text = "Add a new loan")
add_request_btn = Button(menu_window, text = "Add a new request")
close_menu_btn = Button(menu_window, text = "Close Menu", command = destroy_window(menu_window))

# menu_window buttons geometry:
add_book_btn.grid(row = 0, column = 0, padx = 5, pady = 5)
add_member_btn.grid(row = 0, column = 1, padx = 5, pady = 5)
add_loan_btn.grid(row = 0, column = 2, padx = 5, pady = 5)
add_request_btn.grid(row = 0, column = 3, padx = 5, pady = 5)
close_menu_btn.grid(row = 0, column = 4, padx = 5, pady = 5)

menu_window.mainloop()