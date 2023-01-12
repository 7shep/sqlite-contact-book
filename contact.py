import sqlite3
import tkinter

def connect():
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS address (id INTEGER PRIMARY KEY, name text, number INTEGER, email text)")
    conn.commit()
    conn.close()

def insert(name, number, email):
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO address (name, number, email) VALUES (?,?,?)", (name,number,email))    
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM address")
    #print(cur.fetchall())
    rows=cur.fetchall()
    conn.close()
    return rows

connect()

while True:
    print("Commands:")
    print("1: Add a new Contact")
    print("2: Update a Contact")
    print("3: View all Contacts")
    print("4: Delete a Contact")
    print("5: Exit")
    choice=input("Enter your choice: ")
    if choice == "1":
        #print("1")
        name = input("Enter a Name: ")
        number = input("Enter a Phone Number: ")
        email = input("Enter an Email: ")
        insert(name,number,email)
    elif choice == "2":
        #print("2")
        id=input("Enter an ID: ")
        name=input("Enter a Name ")
        number=input("Enter a Phone Number: ")
        email=input("Enter an Email: ")
        update(id,name,number,email)
    elif choice == "3":
        #print("3")
        rows=view()
        for row in rows:
            print(row)
    elif choice == "4":
        print("4")
    elif choice == "5":
        break
    else:
        ("Invalid")