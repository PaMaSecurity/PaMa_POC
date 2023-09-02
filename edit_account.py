# imports:
from imports import tk, messagebox, hashlib, convert_txt_bin, convert_bin_txt


class Edit_account(tk.Frame):
    def __init__(self, master=None, name_list=None, software_to_id=None, software_to_password=None,
                 default_name_list=None):
        super().__init__(master)
        self.root = master
        self.name_list = name_list
        self.software_to_id = software_to_id
        self.software_to_password = software_to_password
        self.default_name_list = default_name_list
        self.root.title("Edit an account")
        self.root.geometry("500x600")
        self.root.resizable(height=False, width=False)
        self.root.config(bg='black')
        self.create_widget()
        self.root.bind('<Return>', self.try_edit_account)

    def create_widget(self):
        try:
            self.root.iconbitmap("resources/password_icon.ico")
        except:
            messagebox.showerror("Error", "An error has occurred, quit the software")
        self.main_label = tk.Label(self.root, text="Enter the name of the account you want to change:", fg="white",
                                   bg="black")
        self.main_label.pack()
        self.website_entry = tk.Entry(self.root, width=61, bg='#5E615E', fg='black')
        self.website_entry.focus_set()
        self.website_entry.pack()
        self.ID_entry = tk.Entry(self.root, width=61, bg='#5E615E', fg='black')
        self.password_entry = tk.Entry(self.root, width=61, bg='#5E615E', fg='black')
        self.button_confirmation = tk.Button(self.root, height=1, width=35, text="confirm account", bg="#5E615E",
                                             fg="white", command=self.try_edit_account)
        self.button_confirmation.pack()
        self.alert = tk.Label(self.root, fg="white", bg="black")
        self.alert.pack()

    def try_edit_account(self, event=None):
        run = False
        self.website = self.website_entry.get().replace(" ", "").lower()
        if self.website == "":
            self.alert.config(text="You have not written anything")
            self.website_entry.delete(0, tk.END)
        else:
            try:
                x = self.name_list[self.website]
                del x
                run = True
            except:
                self.alert.config(text=f"No accounts are registered under this name: {self.website}")
                self.website_entry.delete(0, tk.END)
        if run:
            try:
                x = self.default_name_list[self.website]
                self.alert.config(text="You cannot change a command")
                self.website_entry.delete(0, tk.END)
            except:
                try:
                    # pack_forget:
                    self.button_confirmation.pack_forget()
                    self.alert.pack_forget()
                    # pack
                    self.main_label.config(text=f"Information on the '{self.website}' account")
                    tk.Label(self.root, text="", fg="white", bg="black").pack()
                    if self.website != "main_password":
                        self.ID_entry.pack()
                        tk.Label(self.root, text="", fg="white", bg="black").pack()
                    self.password_entry.pack()
                    self.alert.pack()
                    # other
                    self.website_entry.delete(0, tk.END)
                    self.website_entry.insert(0, self.website)
                    self.ID_entry.delete(0, tk.END)
                    self.ID_entry.insert(0, self.software_to_id[self.website])
                    self.ID = self.software_to_id[self.website]
                    self.password_entry.delete(0, tk.END)
                    if self.website == "main_password":
                        self.password_entry.insert(0, "Enter your new main password")
                    else:
                        self.password_entry.insert(0, self.software_to_password[self.website])
                    self.password = self.software_to_password[self.website]
                    self.alert.config(text="")
                    self.root.bind('<Return>', self.edit_account)
                except:
                    self.alert.config(text="An error has occurred:( Please restart the software. If the error persists, please contact us.")

    def edit_account(self, event=None):
        self.alert.config(text="")
        new_website = self.website_entry.get().replace(" ", "").lower()
        new_ID = self.ID_entry.get().replace(" ", "")
        new_password = self.password_entry.get().replace(" ", "")
        if self.website != new_website and new_website != "":
            try:
                x = self.name_list[new_website]
                nothing = True
                self.alert.config("The name is already taken...")
            except:
                self.edit_website_account(new_website=new_website)
                # nothing
                nothing = False
        else:
            self.website_entry.delete(0, tk.END)
            self.website_entry.insert(0, self.website)
            # nothing
            nothing = True
        if self.ID != new_ID:
            self.edit_ID_account(new_ID=new_ID)
            # nothing
            nothing = False
        else:
            self.ID_entry.delete(0, tk.END)
            self.ID_entry.insert(0, self.ID)
            # nothing
            if nothing:
                nothing = True
        if self.password != new_password and new_password != "":
            if new_password != new_password.replace(";;", "") or \
                    new_password != new_password.replace("::", "") or new_password != new_password.replace("//", ""):
                self.alert.config(text="The password must not contain ';;' , '::' and '//'")
            else:
                self.edit_password_account(new_password=new_password)
                # nothing
                nothing = False
        else:
            if self.website == "main_password":
                pass
            else:
                self.password_entry.delete(0, tk.END)
                self.password_entry.insert(0, self.password)
            # nothing
            if nothing:
                nothing = True
        if nothing:
            self.alert.config(text="You have not changed any information")

    def edit_website_account(self, new_website):
        if self.website == 'main_password':
            self.alert.config(text="You cannot change the name")
        else:
            with open("password.txt", "r") as file:
                liste = list(file)
                file.close()
            for i in range(len(liste)):
                liste[i] = convert_bin_txt(liste[i])
                if liste[i].replace("::", "").replace("\n", "").lstrip().rstrip() == self.website:
                    line = i
            # delete the website or software name, ID and password
            liste[line] = new_website + "::"
            # rewrite the password.txt from list contents/elements:
            with open("password.txt", "w") as file:
                for n in liste:
                    file.write(convert_txt_bin(n) + "\n")
                file.close()
            self.website_entry.delete(0, tk.END)
            self.website_entry.insert(0, new_website)
            del self.name_list[self.website]
            self.name_list[new_website] = None
            self.website = new_website
            self.alert.config(text="Editing done")

    def edit_ID_account(self, new_ID):
        if self.website == 'main_password':
            self.alert.config(text="You cannot change the id")
        else:
            with open("password.txt", "r") as file:
                liste = list(file)
                file.close()
            for i in range(len(liste)):
                liste[i] = convert_bin_txt(liste[i])
                if liste[i].replace("::", "").replace("\n", "").lstrip().rstrip() == self.website:
                    line = i + 1
            # delete the website or software name, ID and password
            print(liste)
            liste[line] = new_ID + "//"
            print(liste)
            # rewrite the password.txt from list contents/elements:
            with open("password.txt", "w") as file:
                for n in liste:
                    file.write(convert_txt_bin(n) + "\n")
                file.close()
            self.ID_entry.delete(0, tk.END)
            self.ID_entry.insert(0, new_ID)
            self.software_to_id[self.website] = new_ID
            self.ID = new_ID
            self.alert.config(text="Editing done")

    def edit_password_account(self, new_password):
        if self.website == 'main_password':
            if new_password == "Enter your new main password":
                self.alert.config(text="You have not changed any information")
            else:
                new_password = new_password.encode()
                new_password = hashlib.sha512(new_password).hexdigest()
                with open("password.txt", "r") as file:
                    liste = list(file)
                    file.close()
                for i in range(len(liste)):
                    liste[i] = convert_bin_txt(liste[i])
                    if liste[i].replace("::", "").replace('\n', '').lstrip().rstrip() == self.website:
                        line = i + 2
                # delete the website or software name, ID and password
                liste[line] = new_password + ";;"
                # rewrite the password.txt from list contents/elements:
                with open("password.txt", "w") as file:
                    for n in liste:
                        file.write(convert_txt_bin(n) + '\n')
                    file.close()
                self.alert.config(text="Editing done")
        else:
            with open("password.txt", "r") as file:
                liste = list(file)
                file.close()
            for i in range(len(liste)):
                liste[i] = convert_bin_txt(liste[i])
                if liste[i].replace("::", "").replace('\n', '').lstrip().rstrip() == self.website:
                    line = i + 2
            # delete the website or software name, ID and password
            liste[line] = new_password + "//"
            # rewrite the password.txt from list contents/elements:
            with open("password.txt", "w") as file:
                for n in liste:
                    file.write(convert_txt_bin(n) + '\n')
                file.close()
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, new_password)
            self.software_to_password[self.website] = new_password
            self.password = new_password
            self.alert.config(text="Editing done")
