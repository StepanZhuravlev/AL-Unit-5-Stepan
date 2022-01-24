def open_add_loan_window():
    """"""

    def widget_selection(var):
        # if var.get() == "ID":
        # display find_id_lbl, find_id_ent

        # if var.get() == "Name":
        # display find_first_name_lbl, find_last_name_lbl, find_first_name_ent, find_last_name_ent
        pass

    menu_window.withdraw()
    find_member_window = Tk()
    find_member_window.title("Find a member")

    # Let the user enter member details (e.g. ID or first name + last name)
    # If a matching record is found in the database, create new record in Loans with the details of student added to it.
    # LoanID - generate automatically on record creation
    # LoanDate - Today / Enter value
    # LoanDuration - Default (how many days?) / Enter value
    # DueForReturn - Calculate using LoanDate and LoanDuration
    # IsDamaged, IsLost - not known at the moment of record creation, need a separate form for adding those values
    # ISBN (FK) - take from the chosen book record
    # MemberID (FK) - take from the matching database record
    # User inputs: LoanDate, LoanDuration, Find book by name/isbn/author

    # grid_remove() - keeps row and column args, widget can be put back by using .grid() (with no args)
    # grid_forget() - forgets row and column args
    # https://xiith.com/python-tkinter-program-for-radiobutton-with-an-event-handling/

    # value = "You selected the option " + str(self.radio.get())
    # self.var.set(value)

    # labels - instantiation
    find_member_lbl = Label(find_member_window, text="Find a member using: ")
    find_id_lbl = Label(find_member_window, text="Member ID: ")
    find_first_name_lbl = Label(find_member_window, text="First name: ")
    find_last_name_lbl = Label(find_member_window, text="Last name: ")

    # entry fields and StringVars - instantiation
    find_id_ent = Entry(find_member_window)  # make visible when find_member_id_rbtn is selected
    find_member_var = StringVar()
    find_first_name_ent = Entry(find_member_window)  # make visible when find_member_name is selected
    find_last_name_ent = Entry(find_member_window)  # make visible when find_member_name is selected

    # buttons - instantiation
    find_member_id_rbtn = Radiobutton(find_member_window, text="ID", variable=find_member_var, value="ID")
    find_member_name_rbtn = Radiobutton(find_member_window, text="First name and last name", variable=find_member_var,
                                        value="Name")
    find_member_btn = Button(find_member_window, text="Find a member")  # command = search algorithm
    back_to_menu_btn = Button(find_member_window, text="Back to Menu",
                              command=lambda: back_to_menu(find_member_window, menu_window))

    # labels - geometry
    find_member_lbl.grid(row=0, column=0, padx=5, pady=5)
    find_id_lbl.grid(row=1, column=0, padx=5, pady=5)
    find_first_name_lbl.grid(row=1, column=1, padx=5, pady=5)
    find_last_name_lbl.grid(row=2, column=1, padx=5, pady=5)

    # entry fields and StringVars - geometry

    # buttons - geometry
    find_member_id_rbtn.grid(row=0, column=1, padx=5, pady=5)
    find_member_name_rbtn.grid(row=0, column=2, padx=5, pady=5)
    find_member_btn.grid(row=3, column=0, padx=5, pady=5)
    back_to_menu_btn.grid(row=3, column=1, padx=5, pady=5)

    find_member_window.protocol("WM_DELETE_WINDOW", lambda: closing_using_x(find_member_window,
                                                                            menu_window))  # imported from switch_windows.py
    find_member_window.mainloop()