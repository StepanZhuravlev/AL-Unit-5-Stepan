import sqlite3


def get_table_records(table_name):  # prints the records successfully, doesn't add them to a Treeview
    """"""
    library_database = sqlite3.connect("Library.db")
    library_table_cursor = library_database.cursor()
    library_table_cursor.execute(f"SELECT * FROM {table_name}")
    rows = library_table_cursor.fetchall()  # gets all records in a form of tuples
    
    for row in rows:
        print(row)
        #tree.insert("", "END", values=row)
    
    library_database.close()
    

get_table_records("Book")