# https://www.activestate.com/resources/quick-reads/how-to-display-data-in-a-table-using-tkinter/
# "change password" button
# function that closes ANY current window and opens menu
# def insert_book_data

from tkinter import *
from tkinter import ttk
from book_database import *


def open_add_book_window():
    """Opens the add_book_window and closes the menu_window"""
    
    def get_book_data():
        """Gets the values of all StringVars in "Book data capture window" and adds them to a list, then inserts the list's elements into "Book" table"""
        list_of_stringvars = [isbn_ent_var, book_title_ent_var, series_ent_var, author_ent_var, genre_ent_var, publisher_ent_var, publication_date_ent_var,
                          price_ent_var, summary_ent_var, keywords_ent_var, cover_type_cbx_var, charge_if_lost_ent_var, charge_if_damaged_ent_var,
                          copies_owned_ent_var, copies_available_ent_var, date_added_ent_var]  # stores the names of all the StringVars
        list_of_values = []  # stores the values of all the StringVars from list_of_fields
        for stringvar in list_of_stringvars:
            list_of_values.append(stringvar.get())
        print(list_of_values)
        insert_book_data(list_of_values)  # imported from book_database
        list_of_values.clear()  # clears the list for next database record

    # can the user upload an image using a tkinter form?
    # appending "date added" to the database record?

    menu_window.destroy()
    add_book_window = Tk()
    add_book_window.title("Book data capture window")
    add_book_window.geometry("500x500")

    # add_book_window - labels
    isbn_lbl = Label(add_book_window, text="ISBN:")
    book_title_lbl = Label(add_book_window, text="Book title:")
    series_lbl = Label(add_book_window, text="Series:")
    author_lbl = Label(add_book_window, text="Author:")
    genre_lbl = Label(add_book_window, text="Genre:")
    publisher_lbl = Label(add_book_window, text="Publisher:")
    publication_date_lbl = Label(add_book_window, text="Publication date:")
    price_lbl = Label(add_book_window, text="Price:")
    summary_lbl = Label(add_book_window, text="Summary:")
    keywords_lbl = Label(add_book_window, text="Keywords:")
    cover_type_lbl = Label(add_book_window, text="Cover type:")
    charge_if_lost_lbl = Label(add_book_window, text="Charge if lost:")
    charge_if_damaged_lbl = Label(add_book_window, text="Charge if damaged:")
    copies_owned_lbl = Label(add_book_window, text="Copies owned:")
    copies_available_lbl = Label(add_book_window, text="Copies available:")
    date_added_lbl = Label(add_book_window, text="Date added:")

    # add_book_window geometry - labels
    isbn_lbl.grid(row=0, column=0, padx=5, pady=5)
    book_title_lbl.grid(row=1, column=0, padx=5, pady=5)
    series_lbl.grid(row=2, column=0, padx=5, pady=5)
    author_lbl.grid(row=3, column=0, padx=5, pady=5)
    genre_lbl.grid(row=4, column=0, padx=5, pady=5)
    publisher_lbl.grid(row=5, column=0, padx=5, pady=5)
    publication_date_lbl.grid(row=6, column=0, padx=5, pady=5)
    price_lbl.grid(row=7, column=0, padx=5, pady=5)
    summary_lbl.grid(row=8, column=0, padx=5, pady=5)
    keywords_lbl.grid(row=9, column=0, padx=5, pady=5)
    cover_type_lbl.grid(row=10, column=0, padx=5, pady=5)
    charge_if_lost_lbl.grid(row=11, column=0, padx=5, pady=5)
    charge_if_damaged_lbl.grid(row=12, column=0, padx=5, pady=5)
    copies_owned_lbl.grid(row=13, column=0, padx=5, pady=5)
    copies_available_lbl.grid(row=14, column=0, padx=5, pady=5)
    date_added_lbl.grid(row=15, column=0, padx=5, pady=5)


    # add_book_window - entry fields and StringVars
    isbn_ent_var = StringVar()
    isbn_ent = Entry(add_book_window, textvariable=isbn_ent_var)
    
    book_title_ent_var = StringVar()
    book_title_ent = Entry(add_book_window, textvariable=book_title_ent_var)
    
    series_ent_var = StringVar()
    series_ent = Entry(add_book_window, textvariable=series_ent_var)
    
    author_ent_var = StringVar()
    author_ent = Entry(add_book_window, textvariable=author_ent_var)
    
    genre_ent_var = StringVar()
    genre_ent = Entry(add_book_window, textvariable=genre_ent_var)
    
    publisher_ent_var = StringVar()
    publisher_ent = Entry(add_book_window, textvariable=publisher_ent_var)
    
    publication_date_ent_var = StringVar()
    publication_date_ent = Entry(add_book_window, textvariable=publication_date_ent_var)  # date picker?
    
    price_ent_var = StringVar()
    price_ent = Entry(add_book_window, textvariable=price_ent_var)
    
    summary_ent_var = StringVar()
    summary_ent = Entry(add_book_window, textvariable=summary_ent_var)
    
    keywords_ent_var = StringVar()
    keywords_ent = Entry(add_book_window, textvariable=keywords_ent_var)
    
    cover_type_cbx_var = StringVar()
    cover_type_cbx = ttk.Combobox(add_book_window, values=["Paperback", "Hardback"], textvariable=cover_type_cbx_var)
    
    charge_if_lost_ent_var = StringVar()
    charge_if_lost_ent = Entry(add_book_window, textvariable=charge_if_lost_ent_var)
    
    charge_if_damaged_ent_var = StringVar()
    charge_if_damaged_ent = Entry(add_book_window, textvariable=charge_if_damaged_ent_var)
    
    copies_owned_ent_var = StringVar()
    copies_owned_ent = Entry(add_book_window, textvariable=copies_owned_ent_var)
    
    copies_available_ent_var = StringVar()
    copies_available_ent = Entry(add_book_window, textvariable=copies_available_ent_var)
    
    date_added_ent_var = StringVar()
    date_added_ent = Entry(add_book_window, textvariable=date_added_ent_var)


    # add_book_window geometry - entry fields
    isbn_ent.grid(row=0, column=1, padx=5, pady=5)
    book_title_ent.grid(row=1, column=1, padx=5, pady=5)
    series_ent.grid(row=2, column=1, padx=5, pady=5)
    author_ent.grid(row=3, column=1, padx=5, pady=5)
    genre_ent.grid(row=4, column=1, padx=5, pady=5)
    publisher_ent.grid(row=5, column=1, padx=5, pady=5)
    publication_date_ent.grid(row=6, column=1, padx=5, pady=5)
    price_ent.grid(row=7, column=1, padx=5, pady=5)
    summary_ent.grid(row=8, column=1, padx=5, pady=5)
    keywords_ent.grid(row=9, column=1, padx=5, pady=5)
    cover_type_cbx.grid(row=10, column=1, padx=5, pady=5)
    charge_if_lost_ent.grid(row=11, column=1, padx=5, pady=5)
    charge_if_damaged_ent.grid(row=12, column=1, padx=5, pady=5)
    copies_owned_ent.grid(row=13, column=1, padx=5, pady=5)
    copies_available_ent.grid(row=14, column=1, padx=5, pady=5)
    date_added_ent.grid(row=15, column=1, padx=5, pady=5)

    # add_book_window - buttons
    book_insert_database_btn = Button(add_book_window, text="Save to the database", command=get_book_data)
    back_to_menu_btn = Button(add_book_window, text="Back to Menu")

    # add_book_window geometry - buttons, centering the button - check the code on school computer
    book_insert_database_btn.grid(row=16, column=1, padx=5, pady=5)
    back_to_menu_btn.grid(row=16, column=0, padx=5, pady=5)  

    add_book_window.mainloop()
    
    
def open_add_member_window():
    """Opens the add_member_window and closes the menu_window"""
    menu_window.destroy()
    add_member_window = Tk()
    member_test_lbl = Label(add_member_window, text="member test").pack()
    add_member_window.mainloop()
    
    
def open_add_loan_window():
    """Opens the add_loan_window and closes the menu_window"""
    menu_window.destroy()
    add_loan_window = Tk()
    loan_test_lbl = Label(add_loan_window, text="loan test").pack()
    add_loan_window.mainloop()
    
    
def open_add_book_request_window():
    """Opens the add_book_request_window and closes the menu_window"""
    menu_window.destroy()
    add_book_request_window = Tk()
    book_request_test_lbl = Label(add_book_request_window, text="book request test").pack()
    add_book_request_window.mainloop()


menu_window = Tk()
menu_window.title("Menu")
menu_window.geometry("600x200")
menu_window.resizable(width=False, height=False)

# menu_window buttons:
add_book_btn = Button(menu_window, text="Add a new book", command=open_add_book_window)
add_member_btn = Button(menu_window, text="Add a new member", command=open_add_member_window)
add_loan_btn = Button(menu_window, text="Add a new loan", command=open_add_loan_window)
add_request_btn = Button(menu_window, text="Add a new book request", command=open_add_book_request_window)
close_menu_btn = Button(menu_window, text="Close Menu", command=menu_window.destroy)

# menu_window geometry - buttons:
add_book_btn.grid(row=0, column=0, padx=5, pady=5)
add_member_btn.grid(row=0, column=1, padx=5, pady=5)
add_loan_btn.grid(row=0, column=2, padx=5, pady=5)
add_request_btn.grid(row=0, column=3, padx=5, pady=5)
close_menu_btn.grid(row=0, column=4, padx=5, pady=5)

menu_window.mainloop()
