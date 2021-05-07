# Py-Notebook

Py Notebook is a fully pledge application dedicated to allowing multiple users write and save notes. All usernames, passwords, and notes are stored in a local SQLite database. The primary purpose of this project was to create a full-stack Python project using only the standard library. The secondary purpose was to prove that tkinter, Python's built-in GUI library that's widely considered ugly or outdated, can create a visually attractive display.

Py Notebook provides the ability for multiple users to hide their notes behind a password. Once logged on, users may: 1) Create new new notes, complete with a title and a body of text, 2) modify saved notes to add on, change, or completely replace their original text, and 3) delete notes.

![image](https://user-images.githubusercontent.com/50125339/117384037-0a95d200-aeb0-11eb-84dc-2782b438eda3.png)

## Py Notebook.py
This file contains all the GUI logic and mostly deals with tkinter and some basic logic. This is the main file to run to actually start and use the application.

## notebook.sqlite3
This is the SQLite database which stores all user information and the note. The main Py Notebook file expects this to be in the same directory and is required for regular functionality.

## SQLite Set Up.py
This file doesn't directly support the application. Instead it preserves the exact SQL used when creating the database. Consequently, this is more of a reference file, which may be useful for any future modifications

## DBTools.py
This is library of tools used primarily to interface with the database. This is kept separately to divide GUI logic and backend logic. All methods are stored as static methods within one object named "db". 

## Future Improvements
While the code written provides a fully functional program, there's room for better error handling. Some error messages will provide the user with a clear cut message of what has gone wrong, but certain, less obvious issues still need to be given a proper error message. Additionally, the added feature of placing notes in order and using a folder system could be a wonderful addition for user customization and organization.

## Known Issues
When the code is interfacing with the database and the program becomes non-responsive or is otherwise interrupted, this can either lock the SQLite file or even corrupt it under certain conditions.
