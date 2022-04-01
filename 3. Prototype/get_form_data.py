import tkinter
from tkinter import ttk

def get_form_data_func(list_of_ent_fields, insert_form_data_func):
    """Gets the inputs from all the entry fields in a form and adds them to a list, then inserts the list's elements into a database table"""
    list_of_values = []  # stores the values of all the StringVars from list_of_ent_fields
    for field_input in list_of_ent_fields:
        if isinstance(field_input, tkinter.Entry) or isinstance(field_input, tkinter.ttk.Combobox):
            print("Eureka!")
        if isinstance(field_input, int):
            # get value of integer variable
        list_of_values.append(field_input.get())
    # print(list_of_values)  # for testing purposes
    insert_form_data_func(list_of_values)  # insert_form_data_func can be any data insertion function from library_database.py
