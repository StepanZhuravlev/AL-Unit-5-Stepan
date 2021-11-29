import sqlite3


def display_table_records(table_name, treeview, num_of_records):
    """Gets all the records from <table_name> table, and inserts them into a <treeview> Treeview"""
    
    library_database = sqlite3.connect("Library.db")
    library_table_cursor = library_database.cursor()
    library_table_cursor.execute(f"SELECT * FROM {table_name}")
    rows = library_table_cursor.fetchall()  # gets all records in a form of tuples
    
    for row in rows:
        treeview.insert("", num_of_records, values=row)
    
    library_database.close()
    