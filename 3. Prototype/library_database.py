import sqlite3
import tkinter
from tkinter import messagebox


# BOOKS TABLE:
def create_book_table():
    """Creates a table for storing book details"""
    library_database = sqlite3.connect("Library.db")
    book_table_cursor = library_database.cursor()  # creating a cursor
    book_table_cursor.execute("""CREATE TABLE IF NOT EXISTS Books(
                                 ISBN VARCHAR(14) PRIMARY KEY,
                                 BookTitle VARCHAR(150),
                                 Series VARCHAR(100),
                                 Author VARCHAR(50),
                                 Genre VARCHAR(50),
                                 Publisher VARCHAR(100),
                                 PublicationDate DATE,
                                 Price CURRENCY,
                                 Summary VARCHAR(1000),
                                 Keywords VARCHAR(300),
                                 CoverType VARCHAR(9),
                                 ChargeIfLost CURRENCY,
                                 ChargeIfDamaged CURRENCY,
                                 CopiesOwned INTEGER,
                                 CopiesAvailable INTEGER,
                                 DateAdded DATE)
                                 """)
    library_database.commit()
    library_database.close()


def insert_book_data(new_book_data):
    """Adds the details entered by the user to Books table in Library.db database"""
    library_database = sqlite3.connect("Library.db")
    book_table_cursor = library_database.cursor()
    book_table_cursor.execute("""INSERT INTO Books(ISBN, BookTitle, Series, Author, Genre, Publisher, PublicationDate,
    Price, Summary, Keywords, CoverType, ChargeIfLost, ChargeIfDamaged, CopiesOwned, CopiesAvailable, DateAdded)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (new_book_data[0], new_book_data[1], new_book_data[2], new_book_data[3],
                                                  new_book_data[4], new_book_data[5], new_book_data[6], new_book_data[7],
                                                  new_book_data[8], new_book_data[9], new_book_data[10], new_book_data[11],
                                                  new_book_data[12], new_book_data[13], new_book_data[14], new_book_data[15])
                                 )
    messagebox.showinfo("", "New data saved successfully.")
    library_database.commit()
    library_database.close()


# MEMBERS TABLE:
def create_members_table():
    """Creates a table for storing member details"""
    library_database = sqlite3.connect("Library.db")
    members_table_cursor = library_database.cursor()
    members_table_cursor.execute("""CREATE TABLE IF NOT EXISTS Members(
                                    MemberID INTEGER PRIMARY KEY,
                                    MemberTitle VARCHAR(10),
                                    FirstName VARCHAR(50),
                                    LastName VARCHAR(50),
                                    DateOfBirth DATE,
                                    Email VARCHAR(50),
                                    SchoolYear INTEGER,
                                    MemberType VARCHAR(10))
                                    """)
    library_database.commit()
    library_database.close()
    
    
def insert_member_data(new_member_data):
    """Adds the details entered by the user to Members table in Library.db database"""
    library_database = sqlite3.connect("Library.db")
    members_table_cursor = library_database.cursor()
    members_table_cursor.execute("""INSERT INTO Members(MemberTitle, FirstName, LastName, DateOfBirth, Email, SchoolYear, MemberType)
    VALUES (?,?,?,?,?,?,?)""", (new_member_data[0], new_member_data[1], new_member_data[2], new_member_data[3],
                                new_member_data[4], new_member_data[5], new_member_data[6]))
    messagebox.showinfo("", "New data saved successfully.")
    library_database.commit()
    library_database.close()
    

# LOANS TABLE:
def create_loans_table():
    """Creates a table for storing loan details"""  # foreign keys bug
    library_database = sqlite3.connect("Library.db")
    loans_table_cursor = library_database.cursor()
    loans_table_cursor.execute("""CREATE TABLE IF NOT EXISTS Loans(
                                  LoanID VARCHAR(5) PRIMARY KEY,
                                  LoanDate DATE,
                                  LoanDuration INTEGER,
                                  DueForReturn DATE,
                                  IsDamaged BOOLEAN,
                                  IsLost BOOLEAN,
                                  ISBN VARCHAR(14),
                                  MemberID INTEGER
                                  )
                                  """)
    #FOREIGN KEY(ISBN) REFERENCES Books(ISBN),
                                  #FOREIGN KEY(MemberID) REFERENCES Members(MemberID)
    library_database.commit()
    library_database.close()
    

def insert_loan_data(new_loan_data):
    """Adds the details entered by the user to Loans table in Library.db database"""
    library_database = sqlite3.connect("Library.db")
    loans_table_cursor = library_database.cursor()
    loans_table_cursor.execute("""INSERT INTO Loans(LoanID, LoanDate, LoanDuration, DueForReturn, IsDamaged, IsLost, ISBN, MemberID)
    VALUES (?,?,?,?,?,?,?,?)""", (new_loan_data[0], new_loan_data[1], new_loan_data[2], new_loan_data[3], new_loan_data[4], new_loan_data[5], new_loan_data[6], new_loan_data[7])
                               )
    print("New loan data inserted successfully.")
    library_database.commit()
    library_database.close()
    

create_book_table()
create_members_table()
create_loans_table()
