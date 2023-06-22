import customtkinter as tk
import mysql.connector

# MySQL connection parameters
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''
DB_NAME = 'go_user'

# Creating a connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="go_user"
)

# Creating a cursor to execute SQL queries
cursor = db.cursor()

# Creating the main application window

# Creating the main application window
window = tk.CTk()

# Function to handle the login process
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Query to check if the username and password exist in the database
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result:
        # Successful login
        message_label.config(text="Login successful!", fg="green")
    else:
        # Invalid login credentials
        message_label.config(text="Invalid username or password!", fg="red")

# Function to handle the signup process
def signup():
    username = username_entry.get()
    password = password_entry.get()

    # Query to insert a new user into the database
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cursor.execute(query, (username, password))
    db.commit()

    message_label.config(text="Signup successful!", fg="green")

# Creating the username label and entry
username_label = tk.Label(window, text="Username:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

# Creating the password label and entry
password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

# Creating the login and signup buttons
login_button = tk.Button(window, text="Login", command=login)
login_button.pack()
signup_button = tk.Button(window, text="Signup", command=signup)
signup_button.pack()

# Creating the message label to display login/signup messages
message_label = tk.Label(window)
message_label.pack()

# Running the main application loop
window.mainloop()

# Closing the database connection when the application is closed
db.close()