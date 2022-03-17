def open_add_loan_window():

    # This code has been rewritten and used in open_find_member_window function in Menu.py file.
    # old_get_loan_data_code.py module isn't used anywhere in Menu.py or any other files.


    # Progress:
    # Value of id_or_name_var getting changed successfully on Radiobutton click

    # Current task:
    # Display widgets based on Radiobutton selection
    # Try displaying all initially, then hiding all using the "Default" value of id_or_name_var

    # Tips:
    # grid_remove() - keeps row and column args, widget can be put back by using .grid() (with no args)
    # grid_forget() - forgets row and column args
    # https://xiith.com/python-tkinter-program-for-radiobutton-with-an-event-handling/
    #

    menu_window.withdraw()
    find_member_window = Tk()
    find_member_window.title("Find a member")

    def selection():
        """Shows either (find_by_id_lbl AND find_by_id_ent) | (find_by_fname_lbl AND find_by_lname_lbl AND find_by_fname_ent AND find_by_lname_ent,
        depending on the value of id_or_name_var"""

        if id_or_name_var.get() == "ID":
            # delete fname and lname widgets
            find_by_fname_lbl.grid_remove()
            find_by_lname_lbl.grid_remove()
            find_by_fname_ent.grid_remove()
            find_by_lname_ent.grid_remove()
            # display id widgets
            find_by_id_lbl.grid()
            find_by_id_ent.grid()

        if id_or_name_var.get() == "Name":  # display find_by_fname_lbl, find_by_lname_lbl, find_by_fname_ent, find_by_lname_ent
            # delete id widgets
            find_by_id_lbl.grid_remove()
            find_by_id_ent.grid_remove()
            # display fname and lname widgets
            find_by_fname_lbl.grid()
            find_by_lname_lbl.grid()
            find_by_fname_ent.grid()
            find_by_lname_ent.grid()

        if id_or_name_var.get() == "Default":  # hide all (only active at the beginning)
            # delete all widgets
            find_by_id_lbl.grid_remove()
            find_by_id_ent.grid_remove()
            find_by_fname_lbl.grid_remove()
            find_by_lname_lbl.grid_remove()
            find_by_fname_ent.grid_remove()
            find_by_lname_ent.grid_remove()

    # StringVar used to store the result of selection:
    id_or_name_var = StringVar(find_member_window, value="Default")

    # labels - instantiation
    heading_lbl = Label(find_member_window, text="Find a member by: ")
    or_lbl = Label(find_member_window, text="OR")
    find_by_id_lbl = Label(find_member_window, text="Member ID:")
    find_by_fname_lbl = Label(find_member_window, text="First name:")
    find_by_lname_lbl = Label(find_member_window, text="Last name:")

    # labels - geometry
    heading_lbl.grid(row=0, column=0, padx=5, pady=5)
    or_lbl.grid(row=0, column=2, padx=5, pady=5)
    find_by_id_lbl.grid(row=1, column=0, padx=5, pady=5)
    find_by_fname_lbl.grid(row=1, column=0, padx=5, pady=5)
    find_by_lname_lbl.grid(row=2, column=0, padx=5, pady=5)

    # entry fields - instantiation
    find_by_id_ent_var = StringVar()
    find_by_id_ent = Entry(find_member_window)
    find_by_fname_ent_var = StringVar()
    find_by_fname_ent = Entry(find_member_window)
    find_by_lname_ent_var = StringVar()
    find_by_lname_ent = Entry(find_member_window)

    # entry fields - geometry
    find_by_id_ent.grid(row=1, column=1, padx=5, pady=5)
    find_by_fname_ent.grid(row=1, column=1, padx=5, pady=5)
    find_by_lname_ent.grid(row=2, column=1, padx=5, pady=5)

    # radiobuttons - instantiation
    find_member_id_rbtn = Radiobutton(find_member_window, text="ID", variable=id_or_name_var, value="ID", command=selection)
    find_member_name_rbtn = Radiobutton(find_member_window, text="First name and last name", variable=id_or_name_var, value="Name", command=selection)

    # radiobuttons - geometry
    find_member_id_rbtn.grid(row=0, column=1, padx=5, pady=5)
    find_member_name_rbtn.grid(row=0, column=3, padx=5, pady=5)

    # buttons - instantiation

    # buttons - geometry

    find_member_window.protocol("WM_DELETE_WINDOW", lambda: closing_using_x(find_member_window, menu_window))  # imported from switch_windows.py
    find_member_window.mainloop()