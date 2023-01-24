import sqlite3

#connects to the SQL database
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

#if view a contatc is selected
def view():
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM address")
    #print(cur.fetchall())
    #^ didnt need that line it was more for troubleshooting.
    rows=cur.fetchall()
    conn.close()
    return rows

#if delete a contact is selected
def delete(id):
    conn = sqlite3.connect("contacts.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM address WHERE id = ?", (id,))
    print("Deleted ID: ", (id,))
    conn.commit()
    conn.close()

#if search a contact is selected
def search(id):
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM address WHERE id = ?",(id,))
    rows=cur.fetchall()
    conn.close()
    return rows

connect()

#when program is ran, shows these options
while True:
    print("Commands:")
    print("1: Add a new Contact")
    print("2: Update a Contact")
    print("3: View all Contacts")
    print("4: Delete a Contact")
    print("5: Search a Contact")
    print("6: Exit")
    #grabs the users choice
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
        #print("4")
        id=input("Enter an ID: ")
        delete(id)
    elif choice == "5":
        id=input("Enter an ID: ")
        rows=search(id)
        for row in rows:
            print(rows)
    elif choice == "6":
        break
    else:
        ("Invalid Choice Entered")