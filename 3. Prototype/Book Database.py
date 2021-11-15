# create a list of all the keywords and make it possible for the user to add new words to the list
import sqlite3


def create_database():
    """<Description>"""
    book_database = sqlite3.connect("Book.db")
    book_database_cursor = book_database.cursor()  # creating a cursor
    book_database_cursor.execute("""CREATE TABLE IF NOT EXISTS Book(
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
    book_database.commit()
    book_database.close()


def insert_book_data(new_book_data):
    """<Description>"""
    book_database = sqlite3.connect("Book.db")
    book_database_cursor = book_database.cursor()
    book_database_cursor.execute("""INSERT INTO Book(ISBN, BookTitle, Series, Author, Genre, Publisher, PublicationDate,
    Price, Summary, Keywords, CoverType, ChargeIfLost, ChargeIfDamaged, CopiesOwned, CopiesAvailable, DateAdded)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (new_book_data[0], new_book_data[1], new_book_data[2], new_book_data[3],
                                                  new_book_data[4], new_book_data[5], new_book_data[6], new_book_data[7],
                                                  new_book_data[8], new_book_data[9], new_book_data[10], new_book_data[11],
                                                  new_book_data[12], new_book_data[13], new_book_data[14], new_book_data[15])
                                 )
    print(f"{new_book_data} inserted")
    book_database.commit()
    book_database.close()


create_database()
insert_book_data(["978-1108412728", "A/AS Level Computer Science for WJEC/Eduqas Student Book", "N/A",
                  "Mark Thomas, Alistair Surrall, Adam Hamflett", "Non-fiction", "Cambridge University Press",
                  "05/10/2017", "32.50", "Written for the WJEC/Eduqas A/AS Level Computer Science specifications for first teaching from 2015, this print student book helps students build their knowledge and master underlying computing principles and concepts. The student book develops computational thinking, programming and problem-solving skills. Suitable for all abilities, it puts computing into context and gives students a real-life view on professional applications of computing skills. Answers to end-of-chapter questions are located in the free online teacher's resource. A Cambridge Elevate enhanced edition is also available.",
                  "Computer Science, A Level, Textbook, WJEC, Student Book", "Paperback", "30.00", "0.00",
                  "10", "6", "14/11/2021"])

# http://sqlitebrowser.org/
