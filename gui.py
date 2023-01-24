import sqlite3
from tkinter import *
from tkinter import ttk

#connects to the sql database
def connect():
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS address (id INTEGER PRIMARY KEY, name text, number INTEGER, email text)")
    conn.commit()
    conn.close()

#if add a contact is selected
def insert(name, number, email):
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO address (name, number, email) VALUES (?,?,?)", (name,number,email))    
    conn.commit()
    conn.close()

#if view a contact is selected
def view():
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM address")
    rows=cur.fetchall()
    conn.close()
    return rows

#if delete a contact is selected
def delete(id):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE id = ?", (id,))
    conn.commit()
    conn.close()

#if search a comment is selected
def search(id):
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM address WHERE id = ?",(id,))
    rows=cur.fetchall()
    conn.close()
    return rows

connect()
#if exit is selected
def exit_program():
    exit()

#makes the window
root = Tk()
root.title("Contacts")

#adds the text that shows commands
label = Label(root, text="Commands:")
label.pack()

#all the buttons
#"command" runs the commands defined above!
add_button = Button(root, text="1: Add a new Contact", command=insert)
add_button.pack()

view_button = Button(root, text="2: View all Contacts", command=view)
view_button.pack()

delete_button = Button(root, text="3: Delete a Contact", command=delete)
delete_button.pack()

search_button = Button(root, text="4: Search a Contact", command=search)
search_button.pack()

exit_button = Button(root, text="5: Exit", command=exit_program)
exit_button.pack()

root.mainloop()
