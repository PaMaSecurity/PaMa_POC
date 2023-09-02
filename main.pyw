# imports:
from imports import tk, messagebox, hashlib, convert_txt_bin, convert_bin_txt, create_seed
from functions import App


# functions:
class Main(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.root = master
        self.root.title("Command invite")
        self.root.geometry("500x500")
        self.root.resizable(height=False, width=False)
        self.create_widget()
        self.root.bind('<Return>', self.confirm_password)

    def create_widget(self):
        try:
            self.root.iconbitmap("resources/password_icon.ico")
        except:
            messagebox.showerror("Error", "An error has occurred, quit the software")
            root.destroy()
        self.label_1 = tk.Label(self.root, text="Enter the password")
        self.label_1.pack()
        self.entry_1 = tk.Entry(self.root, width=51, show="•")
        self.entry_1.pack()
        self.entry_1.focus_set()
        self.button_1 = tk.Button(self.root, height=1, width=35, text="Confirm", command=self.confirm_password)
        self.button_1.pack()

    def confirm_password(self, event=None):
        password = self.entry_1.get()
        password = password.encode()
        password = hashlib.sha512(password).hexdigest()
        if password == self.main_password():
            self.label_1.pack_forget()
            self.entry_1.pack_forget()
            self.button_1.pack_forget()
            self.root = App(master=self.root, seed=create_seed(self.entry_1.get()))
            self.root.destroy()
        else:
            self.root.destroy()

    @staticmethod
    def main_password():
        default_password = "164621c4160e4bfb955f481a650f42ff8603b11f25f1b1476c8e46785be7f1eb920b93ec7081b3b514f54e20c77b28c57d9d3fd9aeaa95ff3c7ec4409cd676ed"
        try:
            open("password.txt").close()
        except:
            open("password.txt", "x").close()
            with open("password.txt", "a+") as file:
                file.write(convert_txt_bin(text="main_password::") + "\n")
                file.write(convert_txt_bin(text="//") + "\n")
                file.write(convert_txt_bin(text=default_password + ";;") + "\n")
                file.close()
        with open("password.txt", "r+") as file:
            f = file.readlines()
            for i in range(len(f)):
                f[i] = convert_bin_txt(text=f[i])
            file.close()
        try:
            for i in range(len(f)):
                if f[i].replace("::", "").lstrip().rstrip() == "main_password":
                    line = i
                    break
            x = f[line]
        except:
            with open("password.txt", "a+") as file:
                file.write(convert_txt_bin(text="main_password::") + "\n")
                file.write(convert_txt_bin(text="//") + "\n")
                file.write(convert_txt_bin(text=default_password + ";;") + "\n")
                file.close()
                f = [None, None, default_password]
            line = 0
        password = f[line + 2].replace(";;", "").replace("\n", "")
        return password


# program loop
root = tk.Tk()
root = Main(root)
root.mainloop()