# This file doesn't affect the final product
# Instead it shows how the SQLite database was set up as both a demonstration and reference

import sqlite3 as sql

# Create the database and connect to it
conn = sql.connect("notebook.sqlite3")
cur = conn.cursor()

# Create the username/password table
# All table names will be stylized as "tblName" and fields will be "field_name" to keep things consistent

# Write the SQL for a very basic user table. The user_id will be the primary key and the username and password
# cannot be left blank
user_sql= """
    CREATE TABLE tblUsers (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
"""

cur.execute(user_sql)

# Write SQL for a notes table. The note_id will be the primary key. user_id is the primary key on tblUsers
# Neither the note title nor the note body may be left blank
notes_sql = """
    CREATE TABLE tblNotes (
        note_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        create_date TEXT NOT NULL,
        modify_date TEXT NOT NULL,
        note_title TEXT NOT NULL,
        note_body TEXT NOT NULL, 
        FOREIGN KEY (user_id) REFERENCES tblUsers(user_id)
    )
"""

cur.execute(notes_sql)