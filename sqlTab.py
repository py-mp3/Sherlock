import tkinter 
from customtkinter import *
import mysql.connector
import tkinter.messagebox as msg


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="go_user"
)


cursor = connection.cursor()

 
class App(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        def signup():

            username = user_entry.get()
            password = pass_entry.get()

            cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
            user = cursor.fetchone()

            if user:
                msg.showerror("Signup Failed", "Username already exists")
            else:
                cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
                connection.commit()
                msg.showinfo("Signup Successful", "Account created successfully")
                # root2.destroy()  # Close the window after signup

        def login():    
            username = user_entry.get()
            password = pass_entry.get()

            cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
            user = cursor.fetchone()

            if user:
                if password == user[2]:
                    msg.showinfo("Login Successful", "Logged in successfully")
                    # root2.destroy()  # Close the window after login
                else:
                    msg.showerror("Login Failed", "Invalid password")
            else:
                msg.showerror("Login Failed", "Username does not exist")
 
        main_frame = CTkFrame(self, fg_color=self.cget("bg"))
        main_frame.grid(row=0, column=0, padx=10, pady=10)
 
        # Login Window title
        title = CTkLabel(master=main_frame, text="Login Window")
        title.grid(row=0, column=0, pady=(0, 20))
 
        # Username label and entry box
        user_label = CTkLabel(master=main_frame, 
                                            text="Username:")
        user_label.grid(row=1, column=0, sticky="w", pady=(0, 10))
        user_entry = CTkEntry(master=main_frame)
        user_entry.grid(row=1, column=1, pady=(0, 10), padx=10)
 
        # Password label and entry box
        pass_label = CTkLabel(master=main_frame, text="Password:")
        pass_label.grid(row=2, column=0, sticky="w", pady=(0, 10))
        pass_entry = CTkEntry(master=main_frame, show="*")
        pass_entry.grid(row=2, column=1, pady=(0, 10), padx=10)
 
        # Remember Me check button
        remember_me = CTkCheckBox(master=main_frame, text="Remember Me")
        remember_me.grid(row=3, column=1, pady=(0, 10))
 
        # Login button
        login_button = CTkButton(master=main_frame, text="Login", command=login)
        login_button.grid(row=4, column=1, pady=(0, 20), sticky="e")
        signup_button = CTkButton(master=main_frame, text="Sign-up", command=signup)
        signup_button.grid(row=5, column=1, pady=(0, 20), sticky="e")
        
 
    
    
app = App()
app.mainloop()