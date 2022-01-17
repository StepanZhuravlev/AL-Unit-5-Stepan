def get_loan_data():
        list_of_ent_fields = [loan_id_ent, loan_date_ent, loan_duration_ent, due_for_return_ent, is_damaged_ent, is_lost_ent, isbn_ent, member_id_ent]  # add names of stringvars
        get_form_data_func(list_of_ent_fields, insert_loan_data)  # imported from get_form_data.py

    menu_window.withdraw()
    add_loan_window = Tk()
    add_loan_window.title("Loan data capture window")
    
    # add_loan_window - labels - instantiation
    loan_id_lbl = Label(add_loan_window, text="Loan ID:")
    loan_date_lbl = Label(add_loan_window, text="Loan date:")
    loan_duration_lbl = Label(add_loan_window, text="Loan duration:")
    due_for_return_lbl = Label(add_loan_window, text="Due for return:")
    is_damaged_lbl = Label(add_loan_window, text="Is damaged:")
    is_lost_lbl = Label(add_loan_window, text="Is lost:")
    isbn_lbl = Label(add_loan_window, text="ISBN:")
    member_id_lbl = Label(add_loan_window, text="Member ID:")
    
    # add_loan_window - labels - geometry
    loan_id_lbl.grid(row=0, column=0, padx=5, pady=5)
    loan_date_lbl.grid(row=1, column=0, padx=5, pady=5)
    loan_duration_lbl.grid(row=2, column=0, padx=5, pady=5)
    due_for_return_lbl.grid(row=3, column=0, padx=5, pady=5)
    is_damaged_lbl.grid(row=4, column=0, padx=5, pady=5)
    is_lost_lbl.grid(row=5, column=0, padx=5, pady=5)
    isbn_lbl.grid(row=6, column=0, padx=5, pady=5)
    member_id_lbl.grid(row=7, column=0, padx=5, pady=5)
    
    # add_loan_window - entry fields - instantiation and StringVars
    loan_id_ent_var = StringVar()
    loan_id_ent = Entry(add_loan_window, textvariable=loan_id_ent_var)
    loan_date_ent_var = StringVar()
    loan_date_ent = Entry(add_loan_window, textvariable=loan_date_ent_var)
    loan_duration_ent_var = StringVar()
    loan_duration_ent = Entry(add_loan_window, textvariable=loan_duration_ent_var)
    due_for_return_ent_var = StringVar()
    due_for_return_ent = Entry(add_loan_window, textvariable=due_for_return_ent_var)
    is_damaged_ent_var = StringVar()
    is_damaged_ent = Entry(add_loan_window, textvariable=is_damaged_ent_var)
    is_lost_ent_var = StringVar()
    is_lost_ent = Entry(add_loan_window, textvariable=is_lost_ent_var)
    isbn_ent_var = StringVar()
    isbn_ent = Entry(add_loan_window, textvariable=isbn_ent_var)
    member_id_ent_var = StringVar()
    member_id_ent = Entry(add_loan_window, textvariable=member_id_ent_var)
    
    # add_loan_window - entry fields - geometry
    loan_id_ent.grid(row=0, column=1, padx=5, pady=5)
    loan_date_ent.grid(row=1, column=1, padx=5, pady=5)
    loan_duration_ent.grid(row=2, column=1, padx=5, pady=5)
    due_for_return_ent.grid(row=3, column=1, padx=5, pady=5)
    is_damaged_ent.grid(row=4, column=1, padx=5, pady=5)
    is_lost_ent.grid(row=5, column=1, padx=5, pady=5)
    isbn_ent.grid(row=6, column=1, padx=5, pady=5)
    member_id_ent.grid(row=7, column=1, padx=5, pady=5)
    
    # add_loan_window - buttons - instantiation
    loan_insert_btn = Button(add_loan_window, text="Save to the database", command=get_loan_data)
    back_to_menu_btn = Button(add_loan_window, text="Back to Menu", command=lambda: back_to_menu(add_loan_window, menu_window))  # imported from switch_windows.py
    
    
    # add_loan_window - buttons - geometry
    loan_insert_btn.grid(row=8, column=0, padx=5, pady=5)
    back_to_menu_btn.grid(row=8, column=1, padx=5, pady=5)
    
    add_loan_window.protocol("WM_DELETE_WINDOW", lambda: closing_using_x(add_loan_window, menu_window))  # imported from switch_windows.py
    add_loan_window.mainloop()