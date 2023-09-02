try:
    import hashlib
    import tkinter as tk
    from tkinter import messagebox
    import tkinter.ttk as ttk
    from convert import convert_txt_bin, convert_bin_txt
    import random
except:
    try:
        from tkinter import messagebox
        messagebox.showerror("Error", "An error has occurred. Restart the software, if the error persists, contact us\nError code: 1")
    except:
        print("An error has occurred. Restart the software, if the error persists, contact us\nError code: 1")
    quit()