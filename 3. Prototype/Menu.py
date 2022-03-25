# Done:
#
# Current goal:
#


import tkinter as tk
from tkinter import *
from tkinter import ttk
from library_database import insert_book_data, insert_member_data
from get_table_records import display_table_records
from switch_windows import back_to_menu, closing_using_x
from get_form_data import get_form_data_func
import sqlite3


def open_add_book_window():
    """Opens the add_book_window and closes the menu_window"""

    def get_book_data():  # Leave at the top as a different function OR call get_form_data_func() directly but after instantiation of entry fields?
        list_of_ent_fields = [isbn_ent, book_title_ent, series_ent, author_ent, genre_ent, publisher_ent,
                              publication_date_ent, price_ent, summary_ent, keywords_ent, cover_type_cbx,
                              charge_if_lost_ent, charge_if_damaged_ent, copies_owned_ent, copies_available_ent,
                              date_added_ent]
        get_form_data_func(list_of_ent_fields, insert_book_data)  # imported from get_form_data.py

    menu_window.withdraw()  # menu_window.destroy() | .withdraw() keeps the menu_window hidden -> needs to be revealed again when X is clicked, or else the program keeps running
    add_book_window = Tk()
    add_book_window.title("Book data capture window")

    # add_book_window - labels - instantiation
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

    # add_book_window geometry - labels - geometry
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

    # add_book_window - entry fields - instantiation & StringVars - Current purpose of StringVars?
    # 1.
    isbn_ent_var = StringVar()
    isbn_ent = Entry(add_book_window, textvariable=isbn_ent_var)
    # 2.
    book_title_ent_var = StringVar()
    book_title_ent = Entry(add_book_window, textvariable=book_title_ent_var)
    # 3.
    series_ent_var = StringVar()
    series_ent = Entry(add_book_window, textvariable=series_ent_var)
    # 4.
    author_ent_var = StringVar()
    author_ent = Entry(add_book_window, textvariable=author_ent_var)
    # 5.
    genre_ent_var = StringVar()
    genre_ent = Entry(add_book_window, textvariable=genre_ent_var)
    # 6.
    publisher_ent_var = StringVar()
    publisher_ent = Entry(add_book_window, textvariable=publisher_ent_var)
    # 7.
    publication_date_ent_var = StringVar()
    publication_date_ent = Entry(add_book_window, textvariable=publication_date_ent_var)  # date picker?
    # 8.
    price_ent_var = StringVar()
    price_ent = Entry(add_book_window, textvariable=price_ent_var)
    # 9.
    summary_ent_var = StringVar()
    summary_ent = Entry(add_book_window, textvariable=summary_ent_var)
    # 10.
    keywords_ent_var = StringVar()
    keywords_ent = Entry(add_book_window, textvariable=keywords_ent_var)
    # 11.
    cover_type_cbx_var = StringVar()
    cover_type_cbx = ttk.Combobox(add_book_window, values=["Paperback", "Hardback"], textvariable=cover_type_cbx_var)
    # 12.
    charge_if_lost_ent_var = StringVar()
    charge_if_lost_ent = Entry(add_book_window, textvariable=charge_if_lost_ent_var)
    # 13.
    charge_if_damaged_ent_var = StringVar()
    charge_if_damaged_ent = Entry(add_book_window, textvariable=charge_if_damaged_ent_var)
    # 14.
    copies_owned_ent_var = StringVar()
    copies_owned_ent = Entry(add_book_window, textvariable=copies_owned_ent_var)
    # 15.
    copies_available_ent_var = StringVar()
    copies_available_ent = Entry(add_book_window, textvariable=copies_available_ent_var)
    # 16.
    date_added_ent_var = StringVar()
    date_added_ent = Entry(add_book_window, textvariable=date_added_ent_var)

    # add_book_window - entry fields - geometry
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

    # add_book_window - buttons - instantiation
    book_insert_database_btn = Button(add_book_window, text="Save to the database", command=get_book_data)
    back_to_menu_btn = Button(add_book_window, text="Back to Menu", command=lambda: back_to_menu(add_book_window, menu_window))  # imported from switch_windows.py

    # add_book_window geometry - buttons - geometry
    book_insert_database_btn.grid(row=16, column=0, padx=5, pady=5)
    back_to_menu_btn.grid(row=16, column=1, padx=5, pady=5)

    add_book_window.protocol("WM_DELETE_WINDOW", lambda: closing_using_x(add_book_window, menu_window))  # imported from switch_windows.py
    add_book_window.mainloop()
    
    
def open_add_member_window():
    """Opens the add_member_window and closes the menu_window"""

    def get_member_data():
        list_of_ent_fields = [member_id_ent, member_title_cbx, first_name_ent, last_name_ent, date_of_birth_ent,
                              email_lbl_ent, school_year_cbx, member_type_cbx]
        get_form_data_func(list_of_ent_fields, insert_member_data)  # imported from get_form_data.py

    menu_window.withdraw()
    add_member_window = Tk()
    add_member_window.title("Member data capture window")
    
    # add_member_window - labels - instantiation
    member_id_lbl = Label(add_member_window, text="Member ID:")
    member_title_lbl = Label(add_member_window, text="Member title:")  # combobox
    first_name_lbl = Label(add_member_window, text="First name:")
    last_name_lbl = Label(add_member_window, text="Last name:")
    date_of_birth_lbl = Label(add_member_window, text="Date of birth:")
    email_lbl = Label(add_member_window, text="Email:")
    school_year_lbl = Label(add_member_window, text="School year (if applicable):")  # combobox
    member_type_lbl = Label(add_member_window, text="Member type:")  # combobox
    # Combobox example:
    # cover_type_cbx = ttk.Combobox(add_book_window, values=["Paperback", "Hardback"], textvariable=cover_type_cbx_var)
    # Fields changed: member_title, school_year, member_type
    
    # add_member_window - labels - geometry
    member_id_lbl.grid(row=0, column=0, padx=5, pady=5)
    member_title_lbl.grid(row=1, column=0, padx=5, pady=5)
    first_name_lbl.grid(row=2, column=0, padx=5, pady=5)
    last_name_lbl.grid(row=3, column=0, padx=5, pady=5)
    date_of_birth_lbl.grid(row=4, column=0, padx=5, pady=5)
    email_lbl.grid(row=5, column=0, padx=5, pady=5)
    school_year_lbl.grid(row=6, column=0, padx=5, pady=5)
    member_type_lbl.grid(row=7, column=0, padx=5, pady=5)
    
    # add_member_window - entry fields - instantiation & StringVars
    # 1.
    member_id_ent_var = StringVar()
    member_id_ent = Entry(add_member_window, textvariable=member_id_ent_var)
    # 2.
    member_title_cbx_var = StringVar()
    member_title_cbx = ttk.Combobox(add_member_window, values=["Mr", "Mrs", "Ms", "Dr"], textvariable=member_title_cbx_var)
    # 3.
    first_name_ent_var = StringVar()
    first_name_ent = Entry(add_member_window, textvariable=first_name_ent_var)
    # 4.
    last_name_ent_var = StringVar()
    last_name_ent = Entry(add_member_window, textvariable=last_name_ent_var)
    # 5.
    date_of_birth_ent_var = StringVar()
    date_of_birth_ent = Entry(add_member_window, textvariable=date_of_birth_ent_var)
    # 6.
    email_lbl_ent_var = StringVar()
    email_lbl_ent = Entry(add_member_window, textvariable=email_lbl_ent_var)
    # 7.
    school_year_cbx_var = StringVar()
    school_year_cbx = ttk.Combobox(add_member_window, values=["n/a", "8", "9", "10", "11", "12", "13", "14"], textvariable=school_year_cbx_var)
    # 8.
    member_type_cbx_var = StringVar()
    member_type_cbx = ttk.Combobox(add_member_window, values=["Student", "Teacher", "Teaching Assistant", "Staff (other)"], textvariable=member_type_cbx_var)
    
    # add_member_window - entry fields - geometry
    member_id_ent.grid(row=0, column=1, padx=5, pady=5)
    member_title_cbx.grid(row=1, column=1, padx=5, pady=5)
    first_name_ent.grid(row=2, column=1, padx=5, pady=5)
    last_name_ent.grid(row=3, column=1, padx=5, pady=5)
    date_of_birth_ent.grid(row=4, column=1, padx=5, pady=5)
    email_lbl_ent.grid(row=5, column=1, padx=5, pady=5)
    school_year_cbx.grid(row=6, column=1, padx=5, pady=5)
    member_type_cbx.grid(row=7, column=1, padx=5, pady=5)
    
    # add_member_window - buttons - instantiation
    member_insert_btn = Button(add_member_window, text="Save to the database", command=get_member_data)
    back_to_menu_btn = Button(add_member_window, text="Back to Menu", command=lambda: back_to_menu(add_member_window, menu_window))  # imported from switch_windows.py
    
    # add_member_window - buttons - geometry
    member_insert_btn.grid(row=8, column=0, padx=5, pady=5)
    back_to_menu_btn.grid(row=8, column=1, padx=5, pady=5)

    add_member_window.protocol("WM_DELETE_WINDOW", lambda: closing_using_x(add_member_window, menu_window))  # imported from switch_windows.py
    add_member_window.mainloop()
    
    
def open_find_member_window():
    """"""
    # Progress:
    # Value of id_or_name_var getting changed successfully on Radiobutton click
    # Appropriate widgets displayed on Radiobutton selection
    # Records retrieved successfully by MemberID, and by FirstName and LastName

    # Current task:
    # Allow user to choose member and confirm their choice
    # Open new window, put necessary member data in a list
    # Provide entry boxes, add inputs to list, write list contents to Loans table

    # Resources:
    # https://www.plus2net.com/python/tkinter-sqlite-id.php - Done
    # Loans table format: LoanID, LoanDate, LoanDuration, DueForReturn, IsDamaged, IsLost, ISBN (FK), MemberID (FK)
    # LoanID - generate
    # LoanDate - Entered by user in add loan window, suggest today's date
    # LoanDuration - Entered by user in add loan window, suggest typical duration (2 or 3 weeks)
    # DueForReturn - Calculate based on LoanDate and LoanDuration
    # IsDamaged - must be entered later
    # IsLost - must be entered later
    # ISBN - let user search for book, import from found record
    # MemberID - import from the found record

    menu_window.withdraw()
    find_member_window = Tk()
    find_member_window.title("Find a member")

    def selection():
        """Shows either (find_by_id_lbl AND find_by_id_ent) | (find_by_fname_lbl AND find_by_lname_lbl AND find_by_fname_ent AND find_by_lname_ent,
        depending on the value of id_or_name_var"""

        if id_or_name_var.get() == "ID":
            # delete fname and lname widgets
            find_by_fname_lbl.grid_forget()
            find_by_lname_lbl.grid_forget()
            find_by_fname_ent.grid_forget()
            find_by_lname_ent.grid_forget()
            # display id widgets
            find_by_id_lbl.grid(row=1, column=0, padx=5, pady=5)
            find_by_id_ent.grid(row=1, column=1, padx=5, pady=5)

        if id_or_name_var.get() == "Name":  # display find_by_fname_lbl, find_by_lname_lbl, find_by_fname_ent, find_by_lname_ent
            # delete id widgets
            find_by_id_lbl.grid_forget()
            find_by_id_ent.grid_forget()
            # display fname and lname widgets
            find_by_fname_lbl.grid(row=1, column=0, padx=5, pady=5)
            find_by_lname_lbl.grid(row=2, column=0, padx=5, pady=5)
            find_by_fname_ent.grid(row=1, column=1, padx=5, pady=5)
            find_by_lname_ent.grid(row=2, column=1, padx=5, pady=5)

        if id_or_name_var.get() == "Default":  # hide all (only active at the beginning)
            # delete all widgets
            find_by_id_lbl.grid_forget()
            find_by_id_ent.grid_forget()
            find_by_fname_lbl.grid_forget()
            find_by_lname_lbl.grid_forget()
            find_by_fname_ent.grid_forget()
            find_by_lname_ent.grid_forget()

    def get_record_by_user_input(member_id, fname, lname):
        if id_or_name_var.get() == "ID":
            db_connect = sqlite3.connect("Library.db")
            db_cursor = db_connect.execute(f"SELECT * FROM Members WHERE MemberID={member_id}")
            output_var.set(db_cursor.fetchone())
            db_connect.close()
        if id_or_name_var.get() == "Name":
            db_connect = sqlite3.connect("Library.db")
            db_cursor = db_connect.execute("SELECT * FROM Members WHERE FirstName=? AND LastName=?", (fname, lname))
            output_var.set(db_cursor.fetchone())
            db_connect.close()

    # StringVars
    id_or_name_var = StringVar(find_member_window, value="Default")  # used to store the result of selection
    output_var = StringVar(find_member_window)

    # labels - instantiation
    heading_lbl = Label(find_member_window, text="Find a member by: ")
    or_lbl = Label(find_member_window, text="OR")
    find_by_id_lbl = Label(find_member_window, text="Member ID:")
    find_by_fname_lbl = Label(find_member_window, text="First name:")
    find_by_lname_lbl = Label(find_member_window, text="Last name:")
    output_lbl = Label(find_member_window, textvariable=output_var)  # Contains the found record

    # labels - geometry
    heading_lbl.grid(row=0, column=0, padx=5, pady=5)
    or_lbl.grid(row=0, column=2, padx=5, pady=5)
    output_lbl.grid(row=3, column=0, padx=5, pady=5)
    # Other labels - declared within selection() function

    # entry fields - instantiation
    find_by_id_ent_var = StringVar(find_member_window)
    find_by_id_ent = Entry(find_member_window, textvariable=find_by_id_ent_var)
    find_by_fname_ent_var = StringVar(find_member_window)
    find_by_fname_ent = Entry(find_member_window, textvariable=find_by_fname_ent_var)
    find_by_lname_ent_var = StringVar(find_member_window)
    find_by_lname_ent = Entry(find_member_window, textvariable=find_by_lname_ent_var)

    # entry fields - geometry
    # Declared within selection() function

    # radiobuttons - instantiation
    find_member_id_rbtn = Radiobutton(find_member_window, text="ID", variable=id_or_name_var, value="ID", command=selection)
    find_member_name_rbtn = Radiobutton(find_member_window, text="First name and last name", variable=id_or_name_var, value="Name", command=selection)

    # radiobuttons - geometry
    find_member_id_rbtn.grid(row=0, column=1, padx=5, pady=5)
    find_member_name_rbtn.grid(row=0, column=3, padx=5, pady=5)

    # buttons - instantiation
    find_member_btn = Button(find_member_window, text="Find a member", command=lambda: get_record_by_user_input(find_by_id_ent_var.get(), find_by_fname_ent_var.get(), find_by_lname_ent_var.get()))  # passes user entered data to a function to get the record details
    back_to_menu_btn = Button(find_member_window, text="Back to Menu", command=lambda: back_to_menu(find_member_window, menu_window))  # imported from switch_windows.py

    # buttons - geometry
    find_member_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
    back_to_menu_btn.grid(row=4, column=2, columnspan=2, padx=5, pady=5)

    find_member_window.protocol("WM_DELETE_WINDOW", lambda: closing_using_x(find_member_window, menu_window))  # imported from switch_windows.py
    find_member_window.mainloop()


def open_add_loan_window():
    """Loan details entry interface"""
    pass


def open_add_book_request_window():
    """Opens the add_book_request_window and closes the menu_window"""
    menu_window.withdraw()
    add_book_request_window = Tk()
    book_request_test_lbl = Label(add_book_request_window, text="book request test").pack()

    add_book_request_window.protocol("WM_DELETE_WINDOW", lambda: closing_using_x(add_book_request_window, menu_window))  # imported from switch_windows.py
    add_book_request_window.mainloop()
    
    
def open_view_books_table_window():
    """Opens the view_books_table_window and closes the menu_window"""
    menu_window.withdraw()
    view_books_table_window = Tk()
    view_books_table_window.title("View Books Table")
    
    # .column(minwidth=0, width=100, stretch=NO)
    # Treeview:
    view_books_table_treeview = ttk.Treeview(view_books_table_window, columns=("col_1", "col_2", "col_3", "col_4",
                                                                               "col_5", "col_6", "col_7", "col_8",
                                                                               "col_9", "col_10", "col_11", "col_12",
                                                                               "col_13", "col_14", "col_15", "col_16"),
                                             show='headings')
    view_books_table_treeview.column("#1", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#1", text="ISBN")
    view_books_table_treeview.column("#2", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#2", text="BookTitle")
    view_books_table_treeview.column("#3", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#3", text="Series")
    view_books_table_treeview.column("#4", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#4", text="Author")
    view_books_table_treeview.column("#5", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#5", text="Genre")
    view_books_table_treeview.column("#6", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#6", text="Publisher")
    view_books_table_treeview.column("#7", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#7", text="PublicationDate")
    view_books_table_treeview.column("#8", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#8", text="Price")
    view_books_table_treeview.column("#9", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#9", text="Summary")
    view_books_table_treeview.column("#10", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#10", text="Keywords")
    view_books_table_treeview.column("#11", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#11", text="CoverType")
    view_books_table_treeview.column("#12", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#12", text="ChargeIfLost")
    view_books_table_treeview.column("#13", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#13", text="ChargeIfDamaged")
    view_books_table_treeview.column("#14", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#14", text="CopiesOwned")
    view_books_table_treeview.column("#15", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#15", text="CopiesAvailable")
    view_books_table_treeview.column("#16", anchor=CENTER, width=100, stretch=NO)
    view_books_table_treeview.heading("#16", text="DateAdded")

    view_books_table_treeview.grid(row=0, column=0, padx=5, pady=5)
    display_books_table_btn = Button(view_books_table_window, text="Display data", command=lambda: display_table_records("Books", view_books_table_treeview, tk.END))  # imported from get_table_records.py
    back_to_menu_btn = Button(view_books_table_window, text="Back to Menu", command=lambda: back_to_menu(view_books_table_window, menu_window))
    display_books_table_btn.grid(row=1, column=0, padx=5, pady=5)
    back_to_menu_btn.grid(row=2, column=0, padx=5, pady=5)

    view_books_table_window.protocol("WM_DELETE_WINDOW", lambda: closing_using_x(view_books_table_window, menu_window))  # imported from switch_windows.py
    view_books_table_window.mainloop()


def open_view_members_table_window():
    menu_window.withdraw()
    view_members_table_window = Tk()
    view_members_table_window.title("View Members Table")

    # Treeview
    view_members_table_treeview = ttk.Treeview(view_members_table_window, columns=("col_1", "col_2", "col_3", "col_4",
                                                                                   "col_5", "col_6", "col_7", "col_8"),
                                               show="headings")
    view_members_table_treeview.column("#1", anchor=CENTER, width=100, stretch=NO)
    view_members_table_treeview.heading("#1", text="MemberID")
    view_members_table_treeview.column("#2", anchor=CENTER, width=100, stretch=NO)
    view_members_table_treeview.heading("#2", text="MemberTitle")
    view_members_table_treeview.column("#3", anchor=CENTER, width=100, stretch=NO)
    view_members_table_treeview.heading("#3", text="FirstName")
    view_members_table_treeview.column("#4", anchor=CENTER, width=100, stretch=NO)
    view_members_table_treeview.heading("#4", text="LastName")
    view_members_table_treeview.column("#5", anchor=CENTER, width=100, stretch=NO)
    view_members_table_treeview.heading("#5", text="DateOfBirth")
    view_members_table_treeview.column("#6", anchor=CENTER, width=100, stretch=NO)
    view_members_table_treeview.heading("#6", text="Email")
    view_members_table_treeview.column("#7", anchor=CENTER, width=100, stretch=NO)
    view_members_table_treeview.heading("#7", text="SchoolYear")
    view_members_table_treeview.column("#8", anchor=CENTER, width=100, stretch=NO)
    view_members_table_treeview.heading("#8", text="MemberType")

    view_members_table_treeview.grid(row=0, column=0, padx=5, pady=5)

    # view_members_table_window - buttons - instantiation
    display_members_table_btn = Button(view_members_table_window, text="Display data", command=lambda: display_table_records("Members", view_members_table_treeview, tk.END))  # imported from get_table_records.py
    back_to_menu_btn = Button(view_members_table_window, text="Back to Menu", command=lambda: back_to_menu(view_members_table_window, menu_window))

    # view_members_table_window - buttons - geometry
    display_members_table_btn.grid(row=1, column=0, padx=5, pady=5)
    back_to_menu_btn.grid(row=2, column=0, padx=5, pady=5)

    view_members_table_window.protocol("WM_DELETE_WINDOW", lambda: closing_using_x(view_members_table_window, menu_window))  # imported from switch_windows.py
    view_members_table_window.mainloop()


def open_view_loans_table_window():

    # Issue: IsDamaged and IsLost displayed as 0 or 1
    # Convert 0 -> False and 1 -> True for Boolean values in Loans table
    # OR add comboboxes that only allow user to enter True or False <---- preferred solution

    menu_window.withdraw()
    view_loans_table_window = Tk()
    view_loans_table_window.title("View Loans Table")

    # Treeview:
    view_loans_table_treeview = ttk.Treeview(view_loans_table_window, columns=("col_1", "col_2", "col_3", "col_4",
                                                                               "col_5", "col_6", "col_7", "col_8"), show="headings")
    view_loans_table_treeview.column("#1", anchor=CENTER, width=100, stretch=NO)
    view_loans_table_treeview.heading("#1", text="LoanID")
    view_loans_table_treeview.column("#2", anchor=CENTER, width=100, stretch=NO)
    view_loans_table_treeview.heading("#2", text="LoanDate")
    view_loans_table_treeview.column("#3", anchor=CENTER, width=100, stretch=NO)
    view_loans_table_treeview.heading("#3", text="LoanDuration")
    view_loans_table_treeview.column("#4", anchor=CENTER, width=100, stretch=NO)
    view_loans_table_treeview.heading("#4", text="DueForReturn")
    view_loans_table_treeview.column("#5", anchor=CENTER, width=100, stretch=NO)
    view_loans_table_treeview.heading("#5", text="IsDamaged")
    view_loans_table_treeview.column("#6", anchor=CENTER, width=100, stretch=NO)
    view_loans_table_treeview.heading("#6", text="IsLost")
    view_loans_table_treeview.column("#7", anchor=CENTER, width=100, stretch=NO)
    view_loans_table_treeview.heading("#7", text="ISBN")
    view_loans_table_treeview.column("#8", anchor=CENTER, width=100, stretch=NO)
    view_loans_table_treeview.heading("#8", text="MemberID")

    view_loans_table_treeview.grid(row=0, column=0, padx=5, pady=5)

    # view_loans_table_window - buttons - instantiation
    display_loans_table_btn = Button(view_loans_table_window, text="Display data", command=lambda: display_table_records("Loans", view_loans_table_treeview, tk.END))  # imported from get_table_records.py
    back_to_menu_btn = Button(view_loans_table_window, text="Back to Menu", command=lambda: back_to_menu(view_loans_table_window, menu_window))

    # view_loans_table_window - buttons - geometry
    display_loans_table_btn.grid(row=1, column=0, padx=5, pady=5)
    back_to_menu_btn.grid(row=2, column=0, padx=5, pady=5)

    view_loans_table_window.protocol("WM_DELETE_WINDOW", lambda: closing_using_x(view_loans_table_window, menu_window))  # imported from switch_windows.py
    view_loans_table_window.mainloop()


menu_window = Tk()
menu_window.title("Menu")
menu_window.resizable(width=False, height=False)

# menu_window - buttons - instantiation
add_book_btn = Button(menu_window, text="Add a new book", command=open_add_book_window)
add_member_btn = Button(menu_window, text="Add a new member", command=open_add_member_window)
add_loan_btn = Button(menu_window, text="Add a new loan", command=open_find_member_window)
add_request_btn = Button(menu_window, text="Add a new book request", command=open_add_book_request_window)  #
close_menu_btn = Button(menu_window, text="Close Menu", command=menu_window.destroy)
view_books_table_btn = Button(menu_window, text="View Books table", command=open_view_books_table_window)
view_members_table_btn = Button(menu_window, text="View Members table", command=open_view_members_table_window)
view_loans_table_btn = Button(menu_window, text="View Loans table", command=open_view_loans_table_window)
view_book_requests_table_btn = Button(menu_window, text="View Book Requests table")  #

# menu_window - buttons - geometry
add_book_btn.grid(row=0, column=0, padx=5, pady=5)
add_member_btn.grid(row=0, column=1, padx=5, pady=5)
add_loan_btn.grid(row=0, column=2, padx=5, pady=5)
add_request_btn.grid(row=0, column=3, padx=5, pady=5)
close_menu_btn.grid(row=0, column=4, padx=5, pady=5)
view_books_table_btn.grid(row=1, column=0, padx=5, pady=5)
view_members_table_btn.grid(row=1, column=1, padx=5, pady=5)
view_loans_table_btn.grid(row=1, column=2, padx=5, pady=5)
view_book_requests_table_btn.grid(row=1, column=3, padx=5, pady=5)

menu_window.protocol("WM_DELETE_WINDOW", lambda: closing_using_x(menu_window, menu_window))  # imported from switch_windows.py
menu_window.mainloop()
