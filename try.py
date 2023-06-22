# # import tkinter as tk

# # def button_click():
# #     label.config(text="Button Clicked!")

# # window = tk.Tk()
# # window.title("My GUI")

# # label = tk.Label(window, text="Hello, World!")
# # label.pack()

# # button = tk.Button(window, text="Click Me!", command=button_click)
# # button.pack()

# # window.mainloop()


# from tkinter import *
# from tkinter import messagebox

# def login():
#     username = username_entry.get()
#     password = password_entry.get()

#     # Add your authentication logic here
#     if username == "admin" and password == "password":
#         messagebox.showinfo("Login Successful", "Welcome, Admin!")
#     else:
#         messagebox.showerror("Login Failed", "Invalid username or password")

# root = Tk()
# root.title("Login System")
# root.geometry("300x200")

# username_label = Label(root, text="Username:")
# username_label.pack()

# username_entry = Entry(root)
# username_entry.pack()

# password_label = Label(root, text="Password:")
# password_label.pack()

# password_entry = Entry(root, show="*")
# password_entry.pack()

# login_button = Button(root, text="Login", command=login)
# login_button.pack()

# root.mainloop()
import mysql.connector
from tkinter import *
from tkinter import messagebox

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="go_user"
)

cursor = connection.cursor()
root = Tk()
root.title("Login/Signup System")
root.geometry("300x200")

def signup():
    username = username_entry.get()
    password = password_entry.get()
    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    user = cursor.fetchone()
    if user:
        messagebox.showerror("Signup Failed", "Username already exists")
    else:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        connection.commit()
        messagebox.showinfo("Signup Successful", "Account created successfully")

def login():
    username = username_entry.get()
    password = password_entry.get()

    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    if user:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

username_label = Label(root, text="Username:")
username_label.pack()

username_entry = Entry(root)
username_entry.pack()

password_label = Label(root, text="Password:")
password_label.pack()

password_entry = Entry(root, show="*")
password_entry.pack()

signup_button = Button(root, text="Signup", command=signup)
signup_button.pack()

login_button = Button(root, text="Login", command=login)
login_button.pack()

root.mainloop()

connection.close()
