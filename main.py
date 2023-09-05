import tkinter
import customtkinter
import requests as re
from tkinter import ttk
import loginSql 
import loginSuccessful


class UserFinder:
    def __init__(self, urls_file):
        self.urls_file = urls_file

    def find_usernames(self, usernames):
        with open(self.urls_file, 'r') as file:
            list_urls = file.read().splitlines()

        results = []

        for url in list_urls:
            try:
                if "https://www.youtube.com" in url:
                    url += f"/@{usernames}"
                full_url = f"{url}/{usernames}"
                response = re.get(full_url)

                if response.status_code == 200:
                    results.append((url, full_url))

            except Exception as e:
                print("[-] An exception occurred while trying to access the website:", str(e))

        return results


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        
        self.title("Sherlock")
        self.geometry(f"{1100}x580")
        self.mode = customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
        self.theme = customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


        self.user_finder = UserFinder('urls.txt')

        self.username = tkinter.StringVar()

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(( 1, 2), weight=1)
        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CustomTkinter",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.login_button = customtkinter.CTkButton(self.sidebar_frame,text='Login', command=self.sidebar_button_event)
        self.login_button.grid(row=1, column=0, padx=20, pady=10)
        self.Sign_up_Button = customtkinter.CTkButton(self.sidebar_frame,text= 'Sign-Up', command=self.sidebar_button_event)
        self.Sign_up_Button.grid(row=2, column=0, padx=20, pady=10)

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionmenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                              values=["100%","80%", "90%", "100%", "110%", "120%"],
                                                              command=self.change_scaling_event, button_hover_color= 'red')
        self.scaling_optionmenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry", textvariable=self.username)
        self.entry.grid(row=0, column=1, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="ew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2,
                                      text_color=("gray10", "#DCE4EE"), command=self.search_usernames, text= 'Search')
        self.main_button_1.grid(row=0, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create treeview
        self.treeview = ttk.Treeview(self)
        self.treeview["columns"] = ("Platform", "Link")
        self.treeview.column("#0", width=0, stretch="NO")
        self.treeview.column("Platform", width=200, anchor="w")
        self.treeview.column("Link", width=800, anchor="w")
        self.treeview.heading("#0", text="", anchor="w")
        self.treeview.heading("Platform", text="Platform", anchor="w")
        self.treeview.heading("Link", text="Link", anchor="w")
        self.treeview.grid(row=1, column=1, columnspan=3, padx=(20, 20), pady=(20, 0), sticky="")


    def search_usernames(self):
        usernames = self.username.get()
        results = self.user_finder.find_usernames(usernames)
        self.display_results(results)

    def display_results(self, results):
        self.treeview.delete(*self.treeview.get_children())
        for platform, link in results:
            self.treeview.insert("", "end", text="", values=(platform, link))

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
                
        app = loginSql.App(father = self)
        app.mainloop()

        print("Running before exiting")

        file = open("userdata.txt", "r")
        info = file.readlines()
        file.close()

        if info[1] == "authenticated":
            self.destroy()
            app = loginSuccessful.App()
            app.mainloop()

if __name__ == "__main__":
    app = App()
    app.mainloop()

