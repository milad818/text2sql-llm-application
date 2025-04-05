import sqlite3
import os


# connect to SQLite database
connection = sqlite3.connect("student.db")

# create a cursor object to execute SQL commands
cursor = connection.cursor()

if not os.path.exists("./student.db"):

    # create the table
    table_info = """
    CREATE TABLE STUDENT (NAME VARCHAR(25),
                            CLASS VARCHAR(25),
                            SECTION VARCHAR(25));
    """

    # create table
    cursor.execute(table_info)

    # insert some records
    cursor.execute("""INSERT INTO STUDENT VALUES ('Milad', 'Data Science', 'A')""")
    cursor.execute("""INSERT INTO STUDENT VALUES ('Francesco', 'Data Science', 'B')""")
    cursor.execute("""INSERT INTO STUDENT VALUES ('Hassan', 'Computer Science', 'A')""")
    cursor.execute("""INSERT INTO STUDENT VALUES ('Nina', 'Computer Science', 'A')""")
    cursor.execute("""INSERT INTO STUDENT VALUES ('Asma', 'Database Technology', 'B')""")
    cursor.execute("""INSERT INTO STUDENT VALUES ('Mark', 'Database Technology', 'A')""")

    # ALTERNATIVELY you can
    # insert multiple records
    # students_list = [
    #     ('Milad', 'Data Science', 'A'),
    #     ('Francesco', 'Data Science', 'B'),
    #     ('Hassan', 'Computer Science', 'A'),
    #     ('Nina', 'Computer Science', 'A'),
    #     ('Asma', 'Database Technology', 'B'),
    #     ('Mark', 'Database Technology', 'A')
    # ]
    # cursor.executemany('''
    # INSERT INTO student (name, class, section) VALUES (?, ?, ?)
    # ''', students_list)

    # save (commit) the changes
    connection.commit()

    # close connection
    connection.close()

    # display the inserted entries
    print("The inserted entries are: ")
    table_data = cursor.execute("""SELECT * FROM STUDENT""")
    for row in table_data:
        print(row)

else:
    print("The database student.db has already been created!")