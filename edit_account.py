# imports:
from imports import tk, ttk, messagebox, convert_bin_txt, convert_txt_bin, hashlib, alpha


class Edit_account(tk.Frame):
    def __init__(self, master=None, name_list=None, software_to_id=None, software_to_password=None,
                 default_name_list=None, seed=None):
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
        self.seed = seed
        self.account_name_combobox.bind('<<ComboboxSelected>>', self.update_widget)

    def create_widget(self):
        try:
            self.root.iconbitmap("resources/password_icon.ico")
        except:
            messagebox.showerror("Error", "An error has occurred, quit the software")
        # label
        self.label = tk.Label(self.root, text="Select the name of the account you want to change:", fg="white",
                              bg="black")
        self.label.place(y=10, x=25)
        # combobox
        self.account_name_combobox = ttk.Combobox(self.root)
        self.account_name_combobox['values'] = [m for m in self.name_list]
        self.account_name_combobox['state'] = 'readonly'
        self.account_name_combobox.place(y=10, x=305)
        # entry
        self.account_name_entry = tk.Entry(self.root, width=61, bg='#5E615E', fg='black')
        self.ID_entry = tk.Entry(self.root, width=61, bg='#5E615E', fg='black')
        self.password_entry = tk.Entry(self.root, width=61, bg='#5E615E', fg='black')
        # button
        self.button_confirmation = tk.Button(self.root, height=1, width=35, text="confirm account", bg="#5E615E",
                                             fg="white", command=self.try_edit_account)
        # alert
        self.alert_widget = tk.Label(self.root, fg="white", bg="black")
        self.alert(y=35)

    def alert(self, text="", y=175):
        self.alert_widget.config(text=text)
        self.alert_widget.place(y=y, x=self.root.winfo_width() / 2 - (len(self.alert_widget.cget('text') * 3)))

    def update_widget(self, event=None):
        self.account_name = self.account_name_combobox.get()
        if self.account_name == "main_password":
            # pack_forget
            self.account_name_entry.place_forget()
            self.ID_entry.place_forget()
            self.password_entry.place_forget()
            self.button_confirmation.place_forget()
            # pack
            self.label.place(y=10, x=60)
            self.account_name_combobox.place(y=10, x=280)
            self.password_entry.place(y=55, x=self.root.winfo_width() / 2 - self.password_entry.cget('width') * 3)
            self.button_confirmation.place(y=85, x=self.root.winfo_width() / 2 - self.button_confirmation.cget(
                'width') * 3 - len(self.button_confirmation.cget('text')))
            self.alert(text="", y=115)
            # modif
            self.ID_entry.insert(0, "default")
            self.account_name_entry.insert(0, "default")
            self.label.config(text="You change the settings of the account :")
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, "Enter your new main password")
            self.root.bind('<Return>', self.try_edit_account)
        else:
            # pack_forget
            self.alert_widget.pack_forget()
            # pack
            self.label.place(y=10, x=60)
            self.account_name_combobox.place(y=10, x=280)
            self.account_name_entry.place(y=55,
                                          x=self.root.winfo_width() / 2 - self.account_name_entry.cget('width') * 3)
            self.ID_entry.place(y=85, x=self.root.winfo_width() / 2 - self.ID_entry.cget('width') * 3)
            self.password_entry.place(y=115, x=self.root.winfo_width() / 2 - self.password_entry.cget('width') * 3)
            self.button_confirmation.place(y=145, x=self.root.winfo_width() / 2 - self.button_confirmation.cget(
                'width') * 3 - len(self.button_confirmation.cget('text')))
            self.alert(text="", y=175)
            # modif
            self.ID_entry.delete(0, tk.END)
            self.account_name_entry.delete(0, tk.END)
            self.label.config(text="You change the settings of the account :")
            self.account_name_entry.delete(0, tk.END)
            self.account_name_entry.insert(0, self.account_name)
            self.ID_entry.delete(0, tk.END)
            self.ID_entry.insert(0, self.software_to_id[self.account_name])
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, self.software_to_password[self.account_name])
            self.root.bind('<Return>', self.try_edit_account)

    def try_edit_account(self, event=None):
        account_name_ = self.account_name_entry.get().replace(" ", "").lower()
        account_ID_ = self.ID_entry.get().replace(" ", "")
        account_password_ = self.password_entry.get().replace(" ", "")
        # check if there has been a change
        if account_name_ != self.account_name or account_ID_ != self.software_to_id[self.account_name] or account_password_ != self.software_to_password[self.account_name]:
            # Ask if the user really wants to save the changes
            if not messagebox.askokcancel("", f"Do you really want to change the {self.account_name} account?"):
                if self.account_name == "main_password":
                    self.alert(text="Modification interrupted", y=115)
                else:
                    self.alert(text="Modification interrupted")
            else:
                # To know if one of the characters used cannot be encrypted
                run = True
                for i in account_name_ + account_ID_ + account_password_:
                    if not i in alpha:
                        run = False
                if not run:
                    char = ""
                    for i in account_name_ + account_ID_ + account_password_:
                        if not i in alpha:
                            char += i
                    self.alert(text=f"You cannot use the following characters: {char}")
                else:
                    # Call up the account modification function
                    self.edit_account(account_name_, account_ID_, account_password_)
        else:
            if self.account_name == "main_password":
                self.alert(text="You have not made any changes", y=115)
            else:
                self.alert(text="You have not made any changes")

    def edit_account(self, account_name_, account_ID_, account_password_):
        # If account_name_ is different from the registered version
        if account_name_ != self.account_name:
            if account_name_ == "":
                self.alert(text="You have not written anything !")
            else:
                if self.account_name == "main_password":
                    self.alert(text="The name is already taken!")
                else:
                    # test if the name is already taken
                    if account_name_ in self.name_list or account_name_ in self.default_name_list:
                        if account_name_ in self.name_list:
                            self.alert("This name is already taken!")
                        if account_name_ in self.default_name_list:
                            self.alert("You cannot use the name of a command !")
                    else:
                        self.edit_name_account(account_name_)
        # If account_ID_ is different from the registered version
        if account_ID_ != self.software_to_id[self.account_name]:
            if account_name_ == "":
                self.alert(text="You have not written anything !")
            else:
                self.edit_ID_account(account_ID_)
        # If account_password_ is different from the registered version
        if account_password_ != self.software_to_password[self.account_name]:
            if account_name_ == "":
                self.alert(text="You have not written anything !")
            else:
                if self.account_name == "main_password":
                    if account_password_ == "Enteryournewmainpassword":
                        print(account_password_)
                        self.alert(text="You have not changed any information", y=115)
                    else:
                        self.edit_main_password(account_password_)
                else:
                    self.edit_password_account(account_password_)

    def edit_name_account(self, new_website):
        # change of name
        with open("password.txt", "r") as file:
            liste = list(file)
            file.close()
        for i in range(len(liste)):
            liste[i] = convert_bin_txt(liste[i])
            if liste[i].replace("::", "").replace("\n", "").lstrip().rstrip() == self.account_name:
                line = i
        # delete the website or software name, ID and password
        liste[line] = new_website + "::"
        # rewrite the password.txt from list contents/elements:
        with open("password.txt", "w") as file:
            for n in liste:
                file.write(convert_txt_bin(n) + "\n")
            file.close()
        # insert the new account name in the entry
        self.account_name_entry.delete(0, tk.END)
        self.account_name_entry.insert(0, new_website)
        # change the account name in name_list
        del self.name_list[self.account_name]
        self.name_list[new_website] = None
        # change the account name in software_to_id
        self.software_to_id[new_website] = self.software_to_id[self.account_name]
        del self.software_to_id[self.account_name]
        # change the account name in software_to_password
        self.software_to_password[new_website] = self.software_to_password[self.account_name]
        del self.software_to_password[self.account_name]
        # give the account its new name
        self.account_name = new_website
        # change the account name in combobox
        self.account_name_combobox['values'] = [m for m in self.name_list]
        # say that the change is made
        self.alert(text="Editing done")

    def edit_ID_account(self, new_ID):
        with open("password.txt", "r") as file:
            liste = list(file)
            file.close()
        for i in range(len(liste)):
            liste[i] = convert_bin_txt(liste[i])
            if liste[i].replace("::", "").replace("\n", "").lstrip().rstrip() == self.account_name:
                line = i + 1
        # delete the website or software name, ID and password
        liste[line] = new_ID + "//"
        # rewrite the password.txt from list contents/elements:
        with open("password.txt", "w") as file:
            for n in liste:
                file.write(convert_txt_bin(n) + "\n")
            file.close()
        self.ID_entry.delete(0, tk.END)
        self.ID_entry.insert(0, new_ID)
        self.software_to_id[self.account_name] = new_ID
        self.alert(text="Editing done")

    def edit_password_account(self, new_password):
        with open("password.txt", "r") as file:
            liste = list(file)
            file.close()
        for i in range(len(liste)):
            liste[i] = convert_bin_txt(liste[i])
            if liste[i].replace("::", "").replace('\n', '').lstrip().rstrip() == self.account_name:
                line = i + 2
        # delete the website or software name, ID and password
        liste[line] = new_password + ";;"
        # rewrite the password.txt from list contents/elements:
        with open("password.txt", "w") as file:
            for n in liste:
                file.write(convert_txt_bin(n) + '\n')
            file.close()
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, new_password)
        self.software_to_password[self.account_name] = new_password
        self.alert(text="Editing done")

    def edit_main_password(self, new_password):
        new_password = new_password.encode()
        new_password = hashlib.sha512(new_password).hexdigest()
        with open("password.txt", "r") as file:
            liste = list(file)
            file.close()
        for i in range(len(liste)):
            liste[i] = convert_bin_txt(liste[i])
            if liste[i].replace("::", "").replace('\n', '').lstrip().rstrip() == self.account_name:
                line = i + 2
        # delete the website or software name, ID and password
        liste[line] = new_password + ";;"
        # rewrite the password.txt from list contents/elements:
        with open("password.txt", "w") as file:
            for n in liste:
                file.write(convert_txt_bin(n) + '\n')
            file.close()
        self.alert(text="Editing done", y=115)

    def quit_window(self):
        self.root.quit()