# imports:
from imports import tk, messagebox, random, convert_txt_bin


class Add_account(tk.Frame):
    def __init__(self, master=None, name_list=None, software_to_id=None, software_to_password=None, default_name_list=None):
        super().__init__(master)
        self.root = master
        self.name_list = name_list
        self.software_to_id = software_to_id
        self.software_to_password = software_to_password
        self.default_name_list = default_name_list
        self.root.title("Add a password")
        self.root.geometry('500x600')
        self.root.resizable(height=False, width=False)
        self.root.config(bg='black')
        self.root.bind('<Return>', self.try_add_account)
        self.create_widget()

    def create_widget(self):
        try:
            self.root.iconbitmap("resources/password_icon.ico")
        except:
            messagebox.showerror("Error", "An error has occurred, quit the software")
        tk.Label(self.root, text="Write the name of the account:", fg="white",
                 bg="black").pack()
        self.website = tk.Entry(self.root, width=61, bg='#5E615E', fg='black')
        self.website.pack()
        self.website.focus_set()
        tk.Label(self.root, text="Write your ID:", fg="white", bg="black").pack()
        self.ID = tk.Entry(self.root, width=61, bg='#5E615E', fg='black')
        self.ID.pack()
        tk.Label(self.root, text="Write your password:", fg="white", bg="black").pack()
        self.password = tk.Entry(self.root, width=61, bg='#5E615E', fg='black', show="•")
        self.password.pack()
        tk.Button(self.root, height=1, width=35, text="generate password",
                  bg="#5E615E", fg="white",
                  command=self.generate_random_password).pack()
        tk.Button(self.root, height=1, width=35, text="Add account", bg="#5E615E",
                  fg="white", command=self.try_add_account).pack()
        self.alert = tk.Label(self.root, fg="white", bg="black")
        self.alert.pack()

    def generate_random_password(self):
        characters = list("1" + "2" + "3" + "4" + "5" + "6" + "7" + "8" + "9" + "!" + "@" + "#" + "$" + "%" + "^" + "&" + "*" + "(" + ")" + '"' + "a" + "z" + "e" + "r" + "t" + "y" + "u" + "i" + "o" + "p" + "q" + "s" + "d" + "f" + "g" + "h" + "j" + "k" + "m" + "w" + "x" + "c" + "v" + "b" + "n" + "A" + "Z" + "E" + "R" + "T" + "Y" + "U" + "P" + "Q" + "S" + "D" + "F" + "G" + "H" + "J" + "K" + "L" + "M" + "W" + "X" + "C" + "V" + "B" + "N")
        random.shuffle(characters)
        password_ = ""
        for i in range(30):
            var = random.choice(characters)
            password_ = password_ + var
        self.root.clipboard_clear()
        self.root.clipboard_append(password_)
        self.root.update()
        self.password.delete(0, tk.END)
        self.password.insert(0, password_)
        self.alert.config(text="The password has been generated and copied to the clipboard")

    def try_add_account(self, event=None):
        website_ = self.website.get().replace(" ", "").lower()
        id_ = self.ID.get()
        password_ = self.password.get().replace(" ", "")
        if website_ == "":
            self.alert.config(text="Please enter the name of the website or software")
        elif website_ in self.name_list:
            self.alert.config(text="The name is already taken!")
        elif website_ in self.default_name_list:
            self.alert.config(text="The name is already taken by a command")
        else:
            try:
                x = self.name_list[website_]
                del x
                self.alert.config(text="The website or software account is already registered")
            except:
                if password_ == "":
                    self.alert.config(text="Please enter your password")
                elif password_ != password_.replace(";;", "") or password_ != password_.replace("::", "") or password_ != password_.replace("//", ""):
                    self.alert.config(text="The password must not contain ';;' , '::' and '//'")
                else:
                    self.add_account(website_, id_, password_)

    def add_account(self, website_, id_, password_):
        with open("password.txt", "a+") as file:
            file.write(convert_txt_bin(website_ + "::") + "\n")
            file.write(convert_txt_bin(id_ + "//") + "\n")
            file.write(convert_txt_bin(password_ + ";;") + "\n")
            file.close()
        # delete the entries
        self.website.delete(0, tk.END)
        self.ID.delete(0, tk.END)
        self.password.delete(0, tk.END)
        # add the password, ID and website to the dictionary
        self.name_list[website_] = None
        self.software_to_id[website_] = id_
        self.software_to_password[website_] = password_
        self.alert.config(text="The account has been saved")
