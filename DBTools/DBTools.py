import sqlite3 as sql
import hashlib

# Create a class for database operations. It doesn't need to be initialed, but it keeps functions organized
class db:
    
    # Write a function for connecting to the database, as if will be used pretty commonly
    @staticmethod
    def connect():
        # Connect to the database
        conn = sql.connect("notebook.sqlite3")
        cur = conn.cursor()
        
        # Return the cursor
        return cur
    
    # Write a function that checks if a username has already been used
    @staticmethod
    def checkUsername(username):
        
        try:
            # Connect to the database
            cur = db.connect()

            # Place the username in a format that's easier for a paramterized query
            username = [(username)]

            # Write the query to check if the username is already used
            cur.execute("SELECT username FROM tblUsers WHERE username = ?", username)

            # Get the results
            results = cur.fetchall()

            # If there are no results, the username isn't used and the function returns false.
            if len(results) == 0:
                return False
            # If there are any results, the username is used and the function returns true
            else:
                return True
            
        except Exception as e:            
            return e
        
    # Write a function that creates a new username/password
    @staticmethod
    def createUser(username, password):
        
        try:
            # Check to see if the username is already used. If so, terminate the function early
            if db.checkUsername(username):
                return False

            # Connect to the database
            # The pre-written function isn't used because we need to separate the connection and cursor 
            conn = sql.connect("notebook.sqlite3")
            cur = conn.cursor()

            # Since the sqlite database is already on the same machine the end user will use and because this code
            # will be posted on Github as part of a portfolio, security measures don't really go  far.
            # With that said, BLAKE2b encryption will be used to mask the password
            password = hashlib.blake2b(password.encode('utf-8')).hexdigest()

            # Place the username/password 
            new_user = (username, password)

            # Execute a parameterized query
            cur.execute("INSERT INTO tblUsers (username, password) VALUES (?, ?)", new_user)
            conn.commit()

            return True
        
        except Exception as e:
            return e
    
    # Create a function to verify the login information for a user
    @staticmethod
    def verifyLogin(username, password):
        try:
            # Connect to the database
            cur = db.connect()

            # If the username doesn't exist in the database, the login credentials aren't correct, and false is returned
            if not db.checkUsername(username):
                return False

            # Encode the password so it matches the stored password in the database
            password = hashlib.blake2b(password.encode('utf-8')).hexdigest()

            # Get the password for the user
            cur.execute("SELECT password FROM tblUsers WHERE username = ?", [(username)])
            stored_password = cur.fetchall()[0][0]

            # If the passwords match, login is verified, return true. Otherwise return false
            if password == stored_password:
                return True
            else:
                return False   
            
        except Exception as e:
            return e
        
    
    # Given a particular user, return a list of all the notes they've written
    @staticmethod
    def returnUserNotes(username):
        
        try:
            # Connect to the database
            cur = db.connect()

            # Format the username in way that the SQLite can read
            username = [username]

            # Get the user_id from the username
            cur.execute("SELECT user_id FROM tblUsers WHERE username = ?", username)

            # Get the user_id from the query
            user_id = [cur.fetchall()[0][0]]

            # Get the notes and corresponding information from the database
            cur.execute("SELECT * FROM tblNotes WHERE user_id = ?", user_id)
            results = cur.fetchall()

            return results
        except Exception as e:
            return e
    
    # Create a function to add a note
    @staticmethod
    def createNote(user_id, create_date, modify_date, note_title, note_body):
        
        try:
            # Connect to the database
            # The pre-written function isn't used because we need to separate the connection and cursor 
            conn = sql.connect("notebook.sqlite3")
            cur = conn.cursor()

            # Place the data into a format SQLite can read
            notes = [user_id, create_date, modify_date, note_title, note_body]

            # Excute the query
            cur.execute(
                """INSERT INTO tblNOTES (user_id, create_date, modify_date, note_title, note_body) 
                VALUES (?, ?, ?, ?, ?)""", notes
            )
            conn.commit()

            return True
        
        except Exception as e:
            return e
        
    # Create a function to modify an existing note
    @staticmethod
    def modifyNote(note_id, modify_date, note_title, note_body):

        try:
            # Connect to the database
            # The pre-written function isn't used because we need to separate the connection and cursor 
            conn = sql.connect("notebook.sqlite3")
            cur = conn.cursor()

            # Place the data into a format SQLite can read
            notes = [modify_date, note_title, note_body, note_id]

            cur.execute("UPDATE tblNotes SET modify_date = ?, note_title = ?, note_body = ? WHERE note_id = ?", notes)
            conn.commit()

            return True
    
        except Exception as e:
            return e
    
    # Write a function to delete a note
    @staticmethod
    def deleteNote(note_id):
        
        try:
            # Connect to the database
            # The pre-written function isn't used because we need to separate the connection and cursor 
            conn = sql.connect("notebook.sqlite3")
            cur = conn.cursor()
            
            # Place the note id in a format SQLite likes
            note_id = [note_id]
            
            cur.execute("DELETE FROM tblNotes WHERE note_id = ?", note_id)
            conn.commit()
            
            return True
            
        except Exception as e:
            return e
        
    # Write a function to get a user id from a username
    @staticmethod
    def getUserID(username):
        
        try:
            
            # Connect to the database
            cur = db.connect()
            
            # Format the username in way that the SQLite can read
            username = [username]

            # Get the user_id from the username
            cur.execute("SELECT user_id FROM tblUsers WHERE username = ?", username)
            
            return cur.fetchall()[0][0]
        
        except Exception as e:
            return e