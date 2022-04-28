# Calculations
# E.g. for search: how many books are worth over [user input cost] pounds? how many members are in [user input year] or higher? how many students are [user input age] or older?
# copy all column values into array, sort the array using insertion (quicksort if enough time), count number of items above the [user input]

# input book price, sort all the books' prices in asc order, find how many books are = or above that price
# insertion sort on array of prices, then binary search on sorted array of prices, then simple calculation to produce result

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from library_database import insert_book_data, insert_member_data, insert_loan_data
from get_table_records import display_table_records
from switch_windows import back_to_menu, close_all_on_x
from get_form_data import get_form_data_func
import sqlite3
import Validations as val
import re


def open_add_book_window():
    """Opens the add_book_window and closes the menu_window"""

    def validate_book_data():

        # presence checks
        val.presence_check(isbn_ent.get(), "ISBN")
        val.presence_check(book_title_ent.get(), "Book Title")
        val.presence_check(series_ent.get(), "Series")
        val.presence_check(author_ent.get(), "Author")
        val.presence_check(genre_ent.get(), "Genre")
        val.presence_check(publisher_ent.get(), "Publisher")
        val.presence_check(publication_date_ent.get(), "Publication date")
        val.presence_check(price_ent.get(), "Price")
        val.presence_check(summary_ent.get(), "Summary")
        val.presence_check(keywords_ent.get(), "Keywords")
        val.presence_check(cover_type_optmenu_var.get(), "Cover type")
        val.presence_check(charge_if_lost_ent.get(), "Charge if lost")
        val.presence_check(charge_if_damaged_ent.get(), "Charge if damaged")
        val.presence_check(copies_owned_ent.get(), "Copies owned")
        val.presence_check(copies_available_ent.get(), "Copies available")
        val.presence_check(date_added_ent.get(), "Date added")

        # ISBN checks: length
        val.length_check(isbn_ent.get(), 20, "ISBN")

        # Price checks: float type, format, range
        try:
            val.type_check_float(float(price_ent.get()), "Price")
        except ValueError:
            messagebox.showerror("Invalid value!", "Price must be a number!")
        val.format_check_currency(float(price_ent.get()), "Price")
        if val.not_negative(float(price_ent.get()), "Price") is not True:
            return False

        # Charge if lost checks: float type, format, range
        try:
            val.type_check_float(float(charge_if_lost_ent.get()), "Charge if lost")
        except ValueError:
            messagebox.showerror("Invalid value!", "Charge if lost must be a number!")
        val.format_check_currency(float(charge_if_lost_ent.get()), "Charge if lost")
        if val.not_negative(float(charge_if_lost_ent.get()), "Charge if lost") is not True:
            return False

        # Charge if damaged checks: float type, format, range
        try:
            val.type_check_float(float(charge_if_lost_ent.get()), "Charge if damaged")
        except ValueError:
            messagebox.showerror("Invalid value!", "Charge if damaged must be a number!")
        val.format_check_currency(float(charge_if_damaged_ent.get()), "Charge if damaged")
        if val.not_negative(float(charge_if_damaged_ent.get()), "Charge if damaged") is not True:
            return False

        # Copies owned checks: int type, range
        try:  # type
            val.type_check_int(int(copies_owned_ent.get()), "Copies owned")
        except ValueError:
            messagebox.showerror("Invalid value!", "Copies owned must be a number!")
        #if val.not_negative(int(copies_owned_ent.get()), "Copies owned") is not True:
            #return False
        if val.range_check(int(copies_owned_ent.get()), 0, 1000, "Copies owned") is not True:
            return False

        # Copies available checks: int type, range
        try:
            val.type_check_int(int(copies_available_ent.get()), "Copies available")
        except ValueError:
            messagebox.showerror("Invalid value!", "Copies available must be a number!")
        #if val.not_negative(int(copies_available_ent.get()), "Copies available") is not True:
            #return False
        if val.range_check(int(copies_available_ent.get()), 0, 1000, "Copies available") is not True:
            return False

        # Publication date: format
        val.format_check_date(publication_date_ent.get(), "Publication date")

        # Date added: format
        val.format_check_date(date_added_ent.get(), "Date added")

    def get_book_data():
        """Saves the field inputs to the database if none of the validation functions return False"""
        list_of_ent_fields = [isbn_ent, book_title_ent, series_ent, author_ent, genre_ent, publisher_ent,
                              publication_date_ent, price_ent, summary_ent, keywords_ent, cover_type_optmenu_var,
                              charge_if_lost_ent, charge_if_damaged_ent, copies_owned_ent, copies_available_ent,
                              date_added_ent]
        print(validate_book_data())
        if validate_book_data() is None:  # validate_book_data() returns None if no errors have been raised
            get_form_data_func(list_of_ent_fields, insert_book_data)  # imported from get_form_data.py
        else:
            pass

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

    # add_book_window - labels - geometry
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

    # add_book_window - entry fields - instantiation & StringVars
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
    cover_type_optmenu_var = StringVar()
    cover_type_optmenu = ttk.OptionMenu(add_book_window, cover_type_optmenu_var, "Choose value:", "Paperback", "Hardback")
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
    cover_type_optmenu.grid(row=10, column=1, padx=5, pady=5)
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

    add_book_window.protocol("WM_DELETE_WINDOW", lambda: close_all_on_x(add_book_window, menu_window))  # imported from switch_windows.py
    add_book_window.mainloop()
    
    
def open_add_member_window():
    """Opens the add_member_window and closes the menu_window"""

    def validate_member_data():
        # presence checks
        val.presence_check(member_id_ent.get(), "Member ID")
        if member_title_optmenu_var.get() == "Choose value:":
            messagebox.showerror("Invalid input!", "Member title can't be left blank!")
            return False
        val.presence_check(first_name_ent.get(), "First name")
        val.presence_check(last_name_ent.get(), "Last name")
        val.presence_check(date_of_birth_ent.get(), "Date of birth")
        val.presence_check(email_ent.get(), "Email")
        if school_year_optmenu_var.get() == "Choose value:":
            messagebox.showerror("Invalid input!", "School year can't be left blank!")
            return False
        if member_type_optmenu_var.get() == "Choose value:":
            messagebox.showerror("Invalid input!", "Member type can't be left blank!")
            return False

        # MemberID checks: type int, range
        try:
            val.type_check_int(int(member_id_ent.get()), "MemberID")
        except ValueError:
            messagebox.showerror("Invalid input!", "MemberID can only be an integer!")
            return False
        if val.not_negative(int(member_id_ent.get()), "MemberID") is not True:
            return False

        # First name: type string, length
        val.type_check_string(first_name_ent.get(), "First name")
        if val.length_check(first_name_ent.get(), 50, "First name") is not True:
            return False

        # Last name: type string, length
        val.type_check_string(last_name_ent.get(), "Last name")
        if val.length_check(last_name_ent.get(), 50, "Last name") is not True:
            return False

        # Date of birth: date format
        if val.format_check_date(date_of_birth_ent.get(), "Date of birth") is not True:
            return False

        # Email: email format, length
        if val.length_check(email_ent.get(), 50, "Email") is not True:
            return False
        if val.format_check_email(email_ent.get(), "Email") is not True:
            return False

    def get_member_data():
        """Saves the field inputs to the database if none of the validation functions return False"""
        list_of_ent_fields = [member_id_ent, member_title_optmenu_var, first_name_ent, last_name_ent, date_of_birth_ent,
                              email_ent, school_year_optmenu_var, member_type_optmenu_var]
        print(validate_member_data())
        if validate_member_data() is None:  # validate_member_data() returns None if no errors have been raised
            get_form_data_func(list_of_ent_fields, insert_member_data)  # imported from get_form_data.py
        else:
            pass

    menu_window.withdraw()
    add_member_window = Tk()
    add_member_window.title("Member data capture window")
    
    # add_member_window - labels - instantiation
    member_id_lbl = Label(add_member_window, text="Member ID:")
    member_title_lbl = Label(add_member_window, text="Member title:")
    first_name_lbl = Label(add_member_window, text="First name:")
    last_name_lbl = Label(add_member_window, text="Last name:")
    date_of_birth_lbl = Label(add_member_window, text="Date of birth:")
    email_lbl = Label(add_member_window, text="Email:")
    school_year_lbl = Label(add_member_window, text="School year (if applicable):")
    member_type_lbl = Label(add_member_window, text="Member type:")
    
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
    member_title_optmenu_var = StringVar()
    member_title_optmenu = ttk.OptionMenu(add_member_window, member_title_optmenu_var, "Choose value:", "Mr", "Miss", "Mrs", "Ms", "Dr")
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
    email_ent_var = StringVar()
    email_ent = Entry(add_member_window, textvariable=email_ent_var)
    # 7.
    school_year_optmenu_var = StringVar()
    school_year_optmenu = ttk.OptionMenu(add_member_window, school_year_optmenu_var, "Choose value:", "n/a", "8", "9", "10", "11", "12", "13", "14")
    # 8.
    member_type_optmenu_var = StringVar()
    member_type_optmenu = ttk.OptionMenu(add_member_window, member_type_optmenu_var, "Choose value:", "Student", "Teacher", "Teaching Assistant", "Staff (other)")
    
    # add_member_window - entry fields - geometry
    member_id_ent.grid(row=0, column=1, padx=5, pady=5)
    member_title_optmenu.grid(row=1, column=1, padx=5, pady=5)
    first_name_ent.grid(row=2, column=1, padx=5, pady=5)
    last_name_ent.grid(row=3, column=1, padx=5, pady=5)
    date_of_birth_ent.grid(row=4, column=1, padx=5, pady=5)
    email_ent.grid(row=5, column=1, padx=5, pady=5)
    school_year_optmenu.grid(row=6, column=1, padx=5, pady=5)
    member_type_optmenu.grid(row=7, column=1, padx=5, pady=5)
    
    # add_member_window - buttons - instantiation
    member_insert_btn = Button(add_member_window, text="Save to the database", command=get_member_data)
    back_to_menu_btn = Button(add_member_window, text="Back to Menu", command=lambda: back_to_menu(add_member_window, menu_window))  # imported from switch_windows.py
    
    # add_member_window - buttons - geometry
    member_insert_btn.grid(row=8, column=0, padx=5, pady=5)
    back_to_menu_btn.grid(row=8, column=1, padx=5, pady=5)

    add_member_window.protocol("WM_DELETE_WINDOW", lambda: close_all_on_x(add_member_window, menu_window))  # imported from switch_windows.py
    add_member_window.mainloop()
    
    
def open_find_member_window():
    """"""
    # Write ID to list that will be added to Loans table
    menu_window.withdraw()
    global find_member_window
    find_member_window = Tk()
    find_member_window.title("Find a member")

    def selection():
        """Shows either (find_by_id_lbl AND find_by_id_ent) or (find_by_fname_lbl AND find_by_lname_lbl AND find_by_fname_ent AND find_by_lname_ent,
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
        """Gets the matching records from the database and adds them to an OptionMenu"""
        if id_or_name_var.get() == "ID":
            db_connect = sqlite3.connect("Library.db")
            # Store matching records in records_optlist:
            db_cursor = db_connect.execute(f"SELECT MemberID, MemberTitle, FirstName, LastName, SchoolYear, MemberType FROM Members WHERE MemberID={member_id}")  # DOB and Email can be omitted
            records_optlist = db_cursor.fetchall()
            db_connect.close()
            # Set up another records_optlist
            another_records_optlist = [("Choose a record:")]
            # Copy all tuples (records) for old option list into new option list
            for record in records_optlist:
                another_records_optlist.append(record)
            # Create OptionMenu containing the new option list
            matches_found_optmenu = ttk.OptionMenu(find_member_window, chosen_record_var, *another_records_optlist)
            matches_found_optmenu.grid(row=3, column=1, padx=5, pady=5)

        if id_or_name_var.get() == "Name":
            db_connect = sqlite3.connect("Library.db")
            # Store matching records in records_optlist:
            db_cursor = db_connect.execute("SELECT MemberID, MemberTitle, FirstName, LastName, SchoolYear, MemberType FROM Members WHERE FirstName=? AND LastName=?", (fname, lname))  # DOB and Email can be omitted
            records_optlist = db_cursor.fetchall()
            db_connect.close()
            # Set up another records_optlist
            another_records_optlist = [("Choose a record:")]
            # Copy all tuples (records) for old option list into new option list
            for record in records_optlist:
                another_records_optlist.append(record)
            # Create OptionMenu containing the new option list
            matches_found_optmenu = ttk.OptionMenu(find_member_window, chosen_record_var, *another_records_optlist)
            matches_found_optmenu.grid(row=3, column=1, padx=5, pady=5)

    def confirm_user_selection():
        """Asks the user to confirm their choice, saves the MemberID of the chosen record, opens the Add new loan window"""
        if messagebox.askyesno("Confirm record selection", "Do you want to confirm your choice?") == True:  # ask to confirm choice
            disallowed_characters = "()'"
            chosen_record_string = chosen_record_var.get()
            for char in disallowed_characters:
                chosen_record_string = chosen_record_string.replace(char,"")  # delete brackets and single quotes to get a clean string
            chosen_record_list = chosen_record_string.split(", ")  # create a list containing values of fields of the chosen record
            global chosen_record_id
            chosen_record_id = int(chosen_record_list[0])  # save MemberID
            # Open Add new loan window:
            open_add_loan_window()

    # Variables
    id_or_name_var = StringVar(find_member_window, value="Default")  # used to store the result of selection
    chosen_record_var = StringVar(find_member_window)  # used to store the selected record (matches_found_optmenu)
    #output_var = StringVar(find_member_window)

    # OptionMenu - instantiation
    #matches_found_optmenu = ttk.OptionMenu(find_member_window, chosen_record_var, *records_optlist)

    # OptionMenu - Geometry
    #matches_found_optmenu.grid(row=3, column=1, padx=5, pady=5)

    # labels - instantiation
    heading_lbl = Label(find_member_window, text="Find a member by: ")
    or_lbl = Label(find_member_window, text="OR")
    find_by_id_lbl = Label(find_member_window, text="Member ID:")
    find_by_fname_lbl = Label(find_member_window, text="First name:")
    find_by_lname_lbl = Label(find_member_window, text="Last name:")
    #output_lbl = Label(find_member_window, textvariable=output_var)  # Contains the found record

    # labels - geometry
    heading_lbl.grid(row=0, column=0, padx=5, pady=5)
    or_lbl.grid(row=0, column=2, padx=5, pady=5)
    #output_lbl.grid(row=3, column=0, padx=5, pady=5)
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
    confirm_selection_btn = Button(find_member_window, text="Confirm selection", command=lambda: confirm_user_selection())

    # buttons - geometry
    find_member_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
    back_to_menu_btn.grid(row=4, column=2, columnspan=2, padx=5, pady=5)
    confirm_selection_btn.grid(row=5, column=0, padx=5, pady=5)

    find_member_window.protocol("WM_DELETE_WINDOW", lambda: close_all_on_x(find_member_window, menu_window))  # imported from switch_windows.py
    find_member_window.mainloop()
    print(find_member_window)


def open_add_loan_window():
    """Hides menu_window, opens add_loan_window"""
    # add islost and isdamaged to the form, the user should set those to True once a loan is created
    # the values of islost and isdamaged can be changed by the user later on if needed

    def get_loan_data():
        """Saves the field inputs to the database"""
        list_of_ent_fields = [loan_id_ent, loan_date_ent, loan_duration_ent, due_for_return_ent,
                              is_damaged_optmenu_var, is_lost_optmenu_var, isbn_ent, chosen_record_id]  # add 8th item - chosen_record_id from confirm_user_selection function
        get_form_data_func(list_of_ent_fields, insert_loan_data)  # imported from get_form_data.py

    menu_window.withdraw()
    find_member_window.withdraw()
    add_loan_window = Tk()
    add_loan_window.title("Add a New Loan")

    # labels - instantiation
    loan_id_lbl = Label(add_loan_window, text="Loan ID:")
    loan_date_lbl = Label(add_loan_window, text="Loan date:")
    loan_duration_lbl = Label(add_loan_window, text="Loan duration:")
    due_for_return_lbl = Label(add_loan_window, text="Due for return:")
    is_damaged_lbl = Label(add_loan_window, text="Damaged?")
    is_lost_lbl = Label(add_loan_window, text="Lost?")
    isbn_lbl = Label(add_loan_window, text="ISBN:")

    # labels - geometry
    loan_id_lbl.grid(row=0, column=0, padx=5, pady=5)
    loan_date_lbl.grid(row=1, column=0, padx=5, pady=5)
    loan_duration_lbl.grid(row=2, column=0, padx=5, pady=5)
    due_for_return_lbl.grid(row=3, column=0, padx=5, pady=5)
    is_damaged_lbl.grid(row=4, column=0, padx=5, pady=5)
    is_lost_lbl.grid(row=5, column=0, padx=5, pady=5)
    isbn_lbl.grid(row=6, column=0, padx=5, pady=5)

    # variables
    loan_id_ent_var = StringVar()
    loan_date_ent_var = StringVar()
    loan_duration_ent_var = StringVar()
    due_for_return_ent_var = StringVar()
    is_damaged_optmenu_var = StringVar()
    is_lost_optmenu_var = StringVar()
    isbn_ent_var = StringVar()
    optmenu_values = ["n/a", "True", "False"]

    # entry fields - instantiation
    loan_id_ent = Entry(add_loan_window, textvariable=loan_id_ent_var)
    loan_date_ent = Entry(add_loan_window, textvariable=loan_date_ent_var)
    loan_duration_ent = Entry(add_loan_window, textvariable=loan_duration_ent_var)
    due_for_return_ent = Entry(add_loan_window, textvariable=due_for_return_ent_var)
    is_damaged_optmenu = ttk.OptionMenu(add_loan_window, is_damaged_optmenu_var, *optmenu_values)
    is_lost_optmenu = ttk.OptionMenu(add_loan_window, is_lost_optmenu_var, *optmenu_values)
    isbn_ent = Entry(add_loan_window, textvariable=isbn_ent_var)

    # entry fields - geometry
    loan_id_ent.grid(row=0, column=1, padx=5, pady=5)
    loan_date_ent.grid(row=1, column=1, padx=5, pady=5)
    loan_duration_ent.grid(row=2, column=1, padx=5, pady=5)
    due_for_return_ent.grid(row=3, column=1, padx=5, pady=5)
    is_damaged_optmenu.grid(row=4, column=1, padx=5, pady=5)
    is_lost_optmenu.grid(row=5, column=1, padx=5, pady=5)
    isbn_ent.grid(row=6, column=1, padx=5, pady=5)

    # buttons - instantiation
    loan_insert_btn = Button(add_loan_window, text="Save to the database", command=get_loan_data)
    back_to_menu_btn = Button(add_loan_window, text="Back to the previous window", command=lambda: back_to_menu(add_loan_window, find_member_window))  # imported from switch_windows.py

    # buttons - geometry
    loan_insert_btn.grid(row=7, column=0, padx=5, pady=5)
    back_to_menu_btn.grid(row=7, column=1, padx=5, pady=5)

    add_loan_window.protocol("WM_DELETE_WINDOW", lambda: close_all_on_x(add_loan_window, menu_window, find_member_window))  # imported from switch_windows.py
    add_loan_window.mainloop()


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

    view_books_table_window.protocol("WM_DELETE_WINDOW", lambda: close_all_on_x(view_books_table_window, menu_window))  # imported from switch_windows.py
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

    view_members_table_window.protocol("WM_DELETE_WINDOW", lambda: close_all_on_x(view_members_table_window, menu_window))  # imported from switch_windows.py
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

    view_loans_table_window.protocol("WM_DELETE_WINDOW", lambda: close_all_on_x(view_loans_table_window, menu_window))  # imported from switch_windows.py
    view_loans_table_window.mainloop()


def open_calculations_window():

    def validate_price():
        """Checks the presence, the range, and the type of user input"""
        val.presence_check(enter_price_ent.get(), "Minimum price")  # presence
        try:  # type
            val.type_check_float(float(enter_price_ent.get()), "Minimum price")
        except ValueError:
            messagebox.showerror("Invalid value!", "Price must be a number!")
        if val.not_negative(enter_price_ent.get(), "Minimum price") is not True:  # range
            return False

    def calculation(user_price, total_price_output, total_books_output):

        if validate_price() is None:  # validate_price returns None if no errors have been raised
            db_connect = sqlite3.connect("Library.db")
            db_cursor_prices = db_connect.execute(f"SELECT Price, CopiesOwned FROM Books WHERE Price>={user_price}")
            prices_numbers_list = db_cursor_prices.fetchall()

            prices_sum = 0
            books_nums_sum = 0

            for tup in prices_numbers_list:
                prices_sum += (tup[0] * tup[1])
                books_nums_sum += tup[1]
            total_price_output.set(str(prices_sum))
            total_books_output.set(str(books_nums_sum))
        else:
            pass

    menu_window.withdraw()

    calculations_window = Tk()
    calculations_window.title("Calculations")

    # variables
    enter_price_ent_var = StringVar(calculations_window)
    tot_books_num_var = StringVar(calculations_window)
    tot_books_price_var = StringVar(calculations_window)

    # labels - inst
    explanation_lbl = Label(calculations_window, text="""This window allows to calculate the number, 
    \nand the total cost of books whose price is 
    \nat least equal to the one entered in the field below""")
    enter_price_lbl = Label(calculations_window, text="Enter the price:")
    tot_books_num = Label(calculations_window, text="Total number of books:")
    tot_books_price = Label(calculations_window, text="Total price of books:")
    tot_books_num_val_lbl = Label(calculations_window, textvariable=tot_books_num_var)
    tot_books_price_val_lbl = Label(calculations_window, textvariable=tot_books_price_var)

    # labels - geometry
    explanation_lbl.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    enter_price_lbl.grid(row=1, column=0, padx=5, pady=5)
    tot_books_num.grid(row=2, column=0, padx=5, pady=5)
    tot_books_price.grid(row=3, column=0, padx=5, pady=5)
    tot_books_num_val_lbl.grid(row=2, column=1, padx=5, pady=5)
    tot_books_price_val_lbl.grid(row=3, column=1, padx=5, pady=5)

    # entry fields - inst
    enter_price_ent = Entry(calculations_window, textvariable=enter_price_ent_var)

    # entry fields - geometry
    enter_price_ent.grid(row=1, column=2, padx=5, pady=5)

    # buttons - inst
    confirm_btn = Button(calculations_window, text="Confirm input", command=lambda: calculation(enter_price_ent_var.get(), tot_books_price_var, tot_books_num_var))
    back_to_menu_btn = Button(calculations_window, text="Back to Menu", command=lambda: back_to_menu(calculations_window, menu_window))

    # buttons - geometry
    confirm_btn.grid(row=4, column=0, padx=5, pady=5)
    back_to_menu_btn.grid(row=4, column=1, padx=5, pady=5)

    calculations_window.protocol("WM_DELETE_WINDOW", lambda: close_all_on_x(calculations_window, menu_window))
    calculations_window.mainloop()


menu_window = Tk()
menu_window.title("Menu")
menu_window.resizable(width=False, height=False)

# menu_window - buttons - instantiation
add_book_btn = Button(menu_window, text="Add a new book", command=open_add_book_window)
add_member_btn = Button(menu_window, text="Add a new member", command=open_add_member_window)
add_loan_btn = Button(menu_window, text="Add a new loan", command=open_find_member_window)
add_request_btn = Button(menu_window, text="Add a new book request")
close_menu_btn = Button(menu_window, text="Close Menu", command=menu_window.destroy)
view_books_table_btn = Button(menu_window, text="View Books table", command=open_view_books_table_window)
view_members_table_btn = Button(menu_window, text="View Members table", command=open_view_members_table_window)
view_loans_table_btn = Button(menu_window, text="View Loans table", command=open_view_loans_table_window)
calculations_btn = Button(menu_window, text="Calculations", command=open_calculations_window)
view_book_requests_table_btn = Button(menu_window, text="View Book Requests table")

# menu_window - buttons - geometry
add_book_btn.grid(row=0, column=0, padx=5, pady=5)
add_member_btn.grid(row=0, column=1, padx=5, pady=5)
add_loan_btn.grid(row=0, column=2, padx=5, pady=5)
add_request_btn.grid(row=0, column=3, padx=5, pady=5)
close_menu_btn.grid(row=0, column=5, padx=5, pady=5)
view_books_table_btn.grid(row=1, column=0, padx=5, pady=5)
view_members_table_btn.grid(row=1, column=1, padx=5, pady=5)
view_loans_table_btn.grid(row=1, column=2, padx=5, pady=5)
calculations_btn.grid(row=0, column=4, padx=5, pady=5)
view_book_requests_table_btn.grid(row=1, column=3, padx=5, pady=5)

menu_window.protocol("WM_DELETE_WINDOW", lambda: close_all_on_x(menu_window))  # imported from switch_windows.py
menu_window.mainloop()
