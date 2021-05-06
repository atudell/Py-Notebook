# Import from DBTools, a set of database functions I wrote for this project
from DBTools.DBTools import db
from tkinter import messagebox
from datetime import date
import tkinter as tk

# Define some common color variables since they'll be used throughout the program
# Also makes things more readable
white = "#fff"
cyan = "#2cd5db"
green = "#4eed6b"
red = "#ed2828"

# Declare a global variable for the user
user = ""

class loginWindow():
    
    def __init__(self, master):
        self.master = master
        # Gives title
        self.master.title = "Py Notebook"
        # Specifies window size and placement
        self.master.geometry("500x600+100+100")
        # Sets the background color
        self.master.config(bg = white)
        # Turns off resizing option
        self.master.resizable(0,0)
        self.addWidgets()
    
    def addWidgets(self):
        
        # Sets up a frame at the top
        self.TopFrame = tk.Frame(self.master, bg = cyan, width = 500, height = 100)
        self.TopFrame.grid(column = 0, row = 0, ipadx= 10, ipady = 10, columnspan = 8)
        
        # Inserts a label within the top frame
        self.Title = tk.Label(self.master, text = "Py Notebook", font = ("Arial", 35), bg = cyan)
        self.Title.grid(column = 0, row = 0, columnspan = 8)
        
        self.LoginFrame = tk.Frame(self.master, bg =white)
        self.LoginFrame.grid(column = 0, row = 1, columnspan = 8)
        
        # Inserts a label below the frame with a prompt to log in
        self.LoginLabel = tk.Label(self.LoginFrame, text = "Login", font = ("Arial", 24), bg = white)
        self.LoginLabel.grid(column = 0, row = 0, columnspan = 8, pady = 10)
        
         # Inserts a label & Entry box for the username
        self.UsernameLabel = tk.Label(self.LoginFrame, text = "Username:", font = ("Arial", 18), bg = white)
        self.UsernameLabel.grid(column = 2, row = 1, pady = 10) 
        self.UsernameEntry = tk.Entry(self.LoginFrame)
        self.UsernameEntry.grid(column = 3,row = 1) 
                
        # Inserts a label & Entry box for the username
        self.PasswordLabel = tk.Label(self.LoginFrame, text = "Password:", font = ("Arial", 18), bg = white)
        self.PasswordLabel.grid(column = 2, row = 2, pady = 10)
        self.PasswordEntry = tk.Entry(self.LoginFrame, show = "*")
        self.PasswordEntry.grid(column = 3, row = 2)
        
        # Inserts login button
        self.LoginButton = tk.Button(self.LoginFrame, text = "Login", font = ("Arial", 18), bg = cyan, relief = "flat", \
                                    command = self.loginUser)
        self.LoginButton.grid(column = 2, row = 3, pady = 10, columnspan = 2)
        
        # Inserts new user button
        self.NewUserText = tk.Button(self.LoginFrame, text = "new user? click here!", font = ("Arial", 10), bg = white, relief = "flat", \
                                    command = self.showNewUser)
        self.NewUserText.grid(column = 2, row = 4, pady = 10, columnspan = 2)
        
        # Create a new frame for new user registration. Tihs frame will hide under the login frame by default
        self.NewUserFrame = tk.Frame(self.master, bg = white)
        self.NewUserFrame.grid(column = 0, row = 1, columnspan = 8)
        
         # Inserts a label & Entry box for the new username
        self.NewUsernameLabel = tk.Label(self.NewUserFrame, text = "New Username:", font = ("Arial", 18), bg = white)
        self.NewUsernameLabel.grid(column = 2, row = 1, pady = 10) 
        self.NewUsernameEntry = tk.Entry(self.NewUserFrame)
        self.NewUsernameEntry.grid(column = 3,row = 1) 
                
        # Inserts a label & Entry box for the new password
        self.NewPasswordLabel = tk.Label(self.NewUserFrame, text = "New Password:", font = ("Arial", 18), bg = white)
        self.NewPasswordLabel.grid(column = 2, row = 2, pady = 10)
        self.NewPasswordEntry = tk.Entry(self.NewUserFrame, show = "*")
        self.NewPasswordEntry.grid(column = 3, row = 2)   
        
        # Inserts a label & Entry box for confirm password
        self.ConfirmPasswordLabel = tk.Label(self.NewUserFrame, text = "Confirm Password:", font = ("Arial", 18), bg = white)
        self.ConfirmPasswordLabel.grid(column = 2, row = 3, pady = 10)
        self.ConfirmPasswordEntry = tk.Entry(self.NewUserFrame, show = "*")
        self.ConfirmPasswordEntry.grid(column = 3, row = 3) 
        
        # Inserts create button
        self.LoginButton = tk.Button(self.NewUserFrame, text = "Create", font = ("Arial", 18), bg = cyan, relief = "flat", \
                                    command = self.createNewUser)
        self.LoginButton.grid(column = 2, row = 4, pady = 10, columnspan = 2)
        
        # Inserts new user button
        self.CancelButton = tk.Button(self.NewUserFrame, text = "Cancel", font = ("Arial", 10), bg = white, relief = "flat", \
                                    command = self.showLogin)
        self.CancelButton.grid(column = 2, row = 5, pady = 10, columnspan = 2)
        
        # Hide the new user frame until its ready to be used
        self.NewUserFrame.grid_remove()
        
    
    # Define function to hide the login information and show new user information
    def showNewUser(self): 
        
        # Hide the login frame and show the new user frame
        self.LoginFrame.grid_remove()
        self.NewUserFrame.grid()    
    
    # Define function to hide thew new user information and show the login information
    def showLogin(self):
        
        # Hide the new user frame and show the login frame
        self.NewUserFrame.grid_remove()
        self.LoginFrame.grid()
    
    def createNewUser(self):
        
        # Get the values from the form
        username = self.NewUsernameEntry.get()
        password = self.NewPasswordEntry.get()
        confirm_password = self.ConfirmPasswordEntry.get()

        # Check to see if any of the boxes are filled out
        if username == "" or password == "" or confirm_password =="":
            messagebox.showerror("Entry Error", "All fields must be complete. Please provide a username and password.")
            return 0
            
        # Check if the username already exists:
        if db.checkUsername(username):
            messagebox.showerror("Duplicate Entries", "This username already exists. Please try a different username.")
            return 0
        
        # Check that the passwords match
        if not password == confirm_password:
            messagebox.showerror("Passwords Don't Match", "The provided passwords don't match. Please try entering again.")
            return 0
        
        # If everything is complete and matching, proceed to store the values into the database
        db.createUser(username, password)
        
        # For the GUI to render correctly, there must be at least one note in the user's profile
        # This will set up a basic welcome note
        date_str = str(date.today())
        user_id = db.getUserID(username)
        db.createNote(user_id, 
                      date_str, 
                      date_str, 
                      "Welcome to Py Notebook!", 
                      "Type here to edit..."
                     )
        
        # Provide the user with a task complete message
        messagebox.showinfo("New User Registration Complete", "New username and password successfully registered!")
        
        # Return to the login information
        self.showLogin()
    
    # Finally create a function to verify the user and log them in
    def loginUser(self):
        
        # get the values from the form
        username = self.UsernameEntry.get()
        password = self.PasswordEntry.get()
        
        # Check to see if any of the boxes are filled out
        if username == "" or password == "":
            messagebox.showerror("Entry Error", "All fields must be complete. Please provide a username and password.")
            return 0
        
        # Check if the username exists:
        if not db.checkUsername(username):
            messagebox.showerror("Username Does Not Exist", "This username does not exist. Please verify the username is correct or register a new user.")
            return 0
        
        if db.verifyLogin(username, password):
            
            # Assign the username to the global variable for user
            global user
            user = username
            
            # Close the login window and open the notes window
            self.master.destroy()
            self.master = tk.Tk()
            self.app = notesWindow(self.master)
            self.master.mainloop()
            
        else:
            messagebox.showerror("Could Not Log In", "The provided username and password did not match. Please try again")
            
class notesWindow:
    
    def __init__(self, master):
        
        self.master = master
        # Gives title
        self.master.title = "Py Notebook"
        # Specifies window size and placement
        self.master.geometry(str(Width) + "x" + str(Height))
        # Sets the background color
        self.master.config(bg = white)
        self.addWidgets()  
        
    def addWidgets(self):
        
        # Get notes from the user's account
        self.notes = db.returnUserNotes(user)
        
        # The number of lines will determine the height of the text area, which should be proportional to screen height
        lines = int((Height - 100)/33)
        
        # Sets up a frame at the top
        self.TopFrame = tk.Frame(self.master, bg = cyan, width = Width, height = 100)
        self.TopFrame.grid(column = 0, row = 0, ipadx= 10, ipady = 10, columnspan = 15)
        
        # Inserts a label within the top frame
        self.Title = tk.Label(self.master, text = "Py Notebook", font = ("Arial", 35), bg = cyan)
        self.Title.grid(column = 0, row = 0, columnspan = 15)
        
        # Create a listbox of all the notes
        self.NoteList = tk.Listbox(self.master, bg = white, font = ("Arial", 14), relief = "flat")
        self.NoteList.grid(column = 1, row = 1, columnspan = 5, rowspan = 3, sticky = "nsew")
        
        # Fill the list box with note titles and pre-select the first item
        for i in range(len(self.notes)):
            self.NoteList.insert(i, self.notes[i][4])
        self.NoteList.selection_set(0)
        
        # Bind the selectNote function to the list box so the screen updates accordingly
        self.NoteList.bind("<<ListboxSelect>>", self.selectNote)
        
        # Make note list selection persistent
        self.NoteList.config(exportselection = False)
        
        # Set up a scrollbar for the list box
        self.NoteListScroll = tk.Scrollbar(self.NoteList)
        self.NoteListScroll.pack(side = "right", fill = "both")
        self.NoteList.config(yscrollcommand = self.NoteListScroll.set)
        self.NoteListScroll.config(command = self.NoteList.yview)
        
        # Get the current selection from the NoteList to fill in the note data
        self.index = self.NoteList.curselection()[0]
            
        # At the bottom of the list box there will be a new note button
        self.NewNoteButton = tk.Button(self.master, text = "New Note", font = ("Arial", 18), bg = cyan, relief = "flat", \
                                      command = self.createNote)
        self.NewNoteButton.grid(column = 1, row = 4, columnspan = 5, sticky = "new")
        
        # By default, the first note will be selected from the notes to display on the message frame
        self.NoteTitle = tk.Text(self.master, font = ("Arial, 25"), bg = white, height = 1, width = 10)
        self.NoteTitle.grid(column = 6, row = 1, columnspan = 8, sticky = "ew")
        self.NoteTitle.insert(tk.END, self.notes[self.index][4])
        
        # Inserts the actual text area where users can read/modify their notes
        self.Note = tk.Text(self.master, font = ("Arial", 14), bg = white, height = lines, wrap = tk.WORD)
        self.Note.grid(column = 6, row = 2, columnspan = 8, sticky = "ew")
        self.Note.insert(tk.END, self.notes[self.index][5])       
        
        # Include a label for the create date
        self.CreateDate = tk.Label(self.master, text = "Created " + self.notes[self.index][2], font = ("Arial", 10), bg = white)
        self.CreateDate.grid(column = 6, row = 3, columnspan = 4, sticky = "w")
        
        # Include a label for the modified date
        self.ModifyDate = tk.Label(self.master, text = "Modified " + self.notes[self.index][3], font = ("Arial", 10), bg = white)
        self.ModifyDate.grid(column = 10, row = 3, columnspan = 4, sticky = "e")
        
        # Insert a button for saving the note
        self.SaveButton = tk.Button(self.master, text = "Save", font = ("Arial", 18), bg = green, relief = "flat", \
                                   command = self.saveNote)
        self.SaveButton.grid(column = 6, row = 4, columnspan = 4, sticky = "ew")
        
        # Insert a button for deleting the note
        self.DeleteButton = tk.Button(self.master, text = "Delete", font = ("Arial", 18), bg = red, relief = "flat", \
                                     command = self.deleteNote)
        self.DeleteButton.grid(column = 10, row = 4, columnspan = 4, sticky = "ew")
    
    # This function will be called to update the note title, text, and dates whenever a change is made
    def selectNote(self, i):

        # Get the current selection
        self.index = self.NoteList.curselection()[0]
        
        # Delete the text within the tile and insert updated title
        self.NoteTitle.delete(1.0, tk.END)
        self.NoteTitle.insert(tk.END, self.notes[self.index][4])

        # Delete the text within text widget and insert the updated text
        self.Note.delete(1.0, tk.END)
        self.Note.insert(tk.END, self.notes[self.index][5])
        
        # Update the create and modify dates
        self.CreateDate.config(text = "Created " + self.notes[self.index][2])
        self.ModifyDate.config(text = "Modified " + self.notes[self.index][3])
        
    def createNote(self):
        
        # Capture the date
        date_str = str(date.today())
        
        # Because the use is already logged in and there's always at least one note, pull the user_id from the first note
        user_id = self.notes[0][1]
        
        # Actually generate a new note within the database with generic text and re-run the query to return all notes
        db.createNote(user_id, date_str, date_str, "New Note...", "Type here to create new note...")
        self.notes = db.returnUserNotes(user)
        
        # Get the new number of notes in self.notes
        i = len(self.notes)
        
        # Update the listbox
        self.NoteList.insert(i, self.notes[i-1][4])
        
        # update the selection on the new note
        self.NoteList.selection_clear(0, tk.END)
        self.NoteList.selection_set(i-1)
        
        # Finally update the screen
        self.selectNote(i)
        
    def saveNote(self):
        
        # Capture the date
        date_str = str(date.today())
        
        # Get the current selection
        i = self.NoteList.curselection()[0]
        
        # Capture the note_id from the current selection and the notes query
        note_id = self.notes[i][0]
        
        # Get the content of the note
        note_title = self.NoteTitle.get(1.0, tk.END)
        note_body = self.Note.get(1.0, tk.END)
        
        # Update the database
        db.modifyNote(note_id, date_str, note_title, note_body)
        
        # Refresh the query with the latest notes
        self.notes = db.returnUserNotes(user)
        
        # Let the screen update, so the changes persist, even if the user clicks away
        self.selectNote(i)
        
        # Finally, the note title in the list box doesn't update automatically, so it will be changed here
        self.NoteList.delete(i)
        self.NoteList.insert(i, self.notes[i][4])
        self.NoteList.selection_set(i)
        
    def deleteNote(self):
        
        # For the GUI to render correctly, there should always be at least one note
        if not len(self.notes) > 1:
            messagebox.showerror("Number of Records Error", "There must always be one note in the notebook. Please write another note before deleting this one.")
            return False
        
        # Get the current selection
        i = self.NoteList.curselection()[0]
        
        # Capture the note_id from the current selection and the notes query
        note_id = self.notes[i][0]
        
        # Delete the note from the database & refresh the query
        db.deleteNote(note_id)
        self.notes = db.returnUserNotes(user)
        
        # Delete all the items from the list box and refill with the new query
        self.NoteList.delete(0, tk.END)
        for i in range(len(self.notes)):
            self.NoteList.insert(i, self.notes[i][4])
        
        # Select the next note 
        self.NoteList.selection_clear(0, tk.END)
        self.NoteList.selection_set(i - 1)
        
        # Finally, update the screen for whatever the new selection is
        self.selectNote(i)
        
app = tk.Tk()
Width = app.winfo_screenwidth()
Height = app.winfo_screenheight()
loginWindow = loginWindow(app)
app.mainloop()