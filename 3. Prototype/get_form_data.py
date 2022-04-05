import tkinter
from tkinter import ttk


def get_form_data_func(list_of_ent_fields, insert_form_data_func):
    """Gets the inputs from all the entry fields in a form and adds them to a list, then inserts the list's elements into a database table"""
    list_of_values = []  # stores the values of all the StringVars from list_of_ent_fields
    for field_input in list_of_ent_fields:
        #if field_input == "True":
        #    list_of_values.append(True)
        #if field_input == "False":
        #    list_of_values.append(False)
        if isinstance(field_input, tkinter.Entry) or isinstance(field_input, tkinter.StringVar):
            list_of_values.append(field_input.get())
        if isinstance(field_input, int):
            list_of_values.append(field_input)
        if isinstance(field_input, ttk.OptionMenu):
            pass  # pass StringVars of OptionMenus instead of the OptionMenus themselves
    insert_form_data_func(list_of_values)  # insert_form_data_func can be any data insertion function from library_database.py
