# "change password" button
#Book (ISBN, BookTitle, Series, Author, Genre, Publisher, PublicationDate, Price, Summary, Keywords, Image, CoverType, ChargeIfLost, ChargeIfDamaged, CopiesOwned, CopiesAvailable, DateAdded)

from tkinter import *
    
    
def destroy_window(window):
    """Destroys a window passed as an argument"""
    return window.destroy


def open_add_book_window():
    """Opens the add_book_window and closes the menu_window"""
    # Can the user upload the Image using a tkinter form?
    # How to automatically generate and append today's date to the end of the record?
    
    menu_window.destroy()
    add_book_window = Tk()
    
    # add_book_window labels:
    isbn_lbl = Label(add_book_window, text = "ISBN:")
    book_title_lbl = Label(add_book_window, text = "Book title:")
    series_lbl = Label(add_book_window, text = "Series:")
    author_lbl = Label(add_book_window, text = "Author:")
    genre_lbl = Label(add_book_window, text = "Genre:")
    publisher_lbl = Label(add_book_window, text = "Publisher:")
    publication_date_lbl = Label(add_book_window, text = "Publication date:")
    price_lbl = Label(add_book_window, text = "Price:")
    summary_lbl = Label(add_book_window, text = "Summary:")
    keywords_lbl = Label(add_book_window, text = "Keywords:")
    cover_type_lbl = Label(add_book_window, text = "Cover type:")
    charge_if_lost_lbl = Label(add_book_window, text = "Charge if lost:")
    charge_if_damaged_lbl = Label(add_book_window, text = "Charge if damaged:")
    copies_owned_lbl = Label(add_book_window, text = "Copies owned:")
    copies_available_lbl = Label(add_book_window, text = "Copies available:")
    
    # add_book_window entry fields:
    isbn_ent = Entry(add_book_window)
    book_title_ent = Entry(add_book_window)
    series_ent = Entry(add_book_window)
    author_ent = Entry(add_book_window)
    genre_ent = Entry(add_book_window)
    publisher_ent = Entry(add_book_window)
    publication_date_ent = Entry(add_book_window) # calendar?
    price_ent = Entry(add_book_window)
    summary_ent = Entry(add_book_window)
    keywords_ent = Entry(add_book_window)
    cover_type_ent = Entry(add_book_window) # combobox?
    charge_if_lost_ent = Entry(add_book_window)
    charge_if_damaged_ent = Entry(add_book_window)
    copies_owned_ent = Entry(add_book_window)
    copies_available_ent = Entry(add_book_window)
    
    add_book_window.mainloop()
    
    
def open_add_member_window():
    """Opens the add_member_window and closes the menu_window"""
    menu_window.destroy()
    add_member_window = Tk()
    member_test_lbl = Label(add_member_window, text = "member test").pack()
    add_member_window.mainloop()
    
    
def open_add_loan_window():
    """Opens the add_loan_window and closes the menu_window"""
    menu_window.destroy()
    add_loan_window = Tk()
    loan_test_lbl = Label(add_loan_window, text = "loan test").pack()
    add_loan_window.mainloop()
    
    
def open_add_book_request_window():
    """Opens the add_book_request_window and closes the menu_window"""
    menu_window.destroy()
    add_book_request_window = Tk()
    book_request_test_lbl = Label(add_book_request_window, text = "book request test").pack()
    add_book_request_window.mainloop()


menu_window = Tk()
menu_window.title("Menu")
menu_window.geometry("600x200")
menu_window.resizable(width=False, height=False)

# menu_window buttons:
add_book_btn = Button(menu_window, text = "Add a new book", command = open_add_book_window)
add_member_btn = Button(menu_window, text = "Add a new member", command = open_add_member_window)
add_loan_btn = Button(menu_window, text = "Add a new loan", command = open_add_loan_window)
add_request_btn = Button(menu_window, text = "Add a new book request", command = open_add_book_request_window)
close_menu_btn = Button(menu_window, text = "Close Menu", command = destroy_window(menu_window))

# menu_window buttons geometry:
add_book_btn.grid(row = 0, column = 0, padx = 5, pady = 5)
add_member_btn.grid(row = 0, column = 1, padx = 5, pady = 5)
add_loan_btn.grid(row = 0, column = 2, padx = 5, pady = 5)
add_request_btn.grid(row = 0, column = 3, padx = 5, pady = 5)
close_menu_btn.grid(row = 0, column = 4, padx = 5, pady = 5)

menu_window.mainloop()