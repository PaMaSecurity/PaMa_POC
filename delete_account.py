# imports:
from imports import tk, ttk, messagebox, convert_txt_bin, convert_bin_txt


class Delete_account(tk.Frame):
    def __init__(self, master=None, name_list=None, software_to_id=None, software_to_password=None, default_name_list=None):
        super().__init__(master)
        self.root = master
        self.name_list = name_list
        self.software_to_id = software_to_id
        self.software_to_password = software_to_password
        self.default_name_list = default_name_list
        self.root.title("Delete a password")
        self.root.geometry('500x600')
        self.root.resizable(height=False, width=False)
        self.root.config(bg='black')
        self.root.bind('<Return>', self.try_delete_account)
        self.create_widget()

    def create_widget(self):
        try:
            self.root.iconbitmap("resources/password_icon.ico")
        except:
            messagebox.showerror("Error", "An error has occurred, quit the software")
        tk.Label(self.root, text="Write the name of the website or software you want to delete:", fg="white", bg="black").pack()
        self.entry_website = ttk.Combobox(self.root)
        liste = [m for m in self.name_list if m != "main_password"]
        if not liste:
            self.entry_website['values'] = [" "]
        else:
            self.entry_website['values'] = liste
        self.entry_website['state'] = 'readonly'
        self.entry_website.pack()
        self.entry_website.focus_set()
        tk.Button(self.root, height=1, width=35, text="Delete password", bg="#5E615E", fg="white", command=self.try_delete_account).pack()
        self.alert = tk.Label(self.root, fg="white", bg="black")
        self.alert.pack()

    def try_delete_account(self, event=None):
        running = None
        website = self.entry_website.get()
        website = website.lstrip().rstrip().replace(" ", "")
        if website == "":
            self.alert.config(text="You have not selected anything")
            self.entry_website.delete(0, tk.END)
        else:
            for i in self.name_list:
                if website == i and website != "main_password":
                    running = True
                    break
                else:
                    running = False
            try:
                x = self.default_name_list[website]
                del x
                self.alert.config(text="You cannot delete commands !")
            except:
                if not running:
                    self.alert.config(text=f'The account you want to delete is not registered under this name: "{website}"')
                    self.entry_website.delete(0, tk.END)
                else:
                    if not messagebox.askokcancel("Delete", "Do you want to delete your account?"):
                        self.alert.config(text="Deletion interrupted")
                    else:
                        try:
                            self.delete_account(website)
                        except:
                            self.alert.config(text="An error has occurred. Restart the software and if the error persists, contact us")
                            self.delete_account(website)

    def delete_account(self, website):
        with open("password.txt", "r") as file:
            liste = list(file)
            file.close()
        for i in range(len(liste)):
            liste[i] = convert_bin_txt(liste[i])
            if liste[i].replace("::", "").replace("\n", "").lstrip().rstrip() == website:
                del_line = i
        # delete the website or software name, ID and password
        for i in range(3):
            del liste[del_line]
        # rewrite the password.txt from list contents/elements:
        with open("password.txt", "w") as file:
            for n in liste:
                file.write(convert_txt_bin(n) + '\n')
            file.close()
        self.alert.config(text="Successful deletion !")
        self.entry_website.delete(0, tk.END)
        del self.name_list[website]
        liste = [m for m in self.name_list if m != "main_password"]
        if not liste:
            self.entry_website['values'] = [" "]
        else:
            self.entry_website['values'] = liste

    def quit_window(self):
        self.root.quit()