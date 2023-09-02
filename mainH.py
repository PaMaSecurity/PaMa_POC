### imports
try:
    import hashlib
    from sys import exit as sys_exit, argv as sys_argv
    from pickle import dump, load
    from functools import partial
    from webbrowser import open as open_link
    from PyQt5.QtCore import Qt, QTimer
    from PyQt5.QtGui import QCursor, QFont, QIcon, QPixmap, QKeySequence
    from PyQt5.QtWidgets import QAbstractItemView, QAction, QApplication, QFrame, QHeaderView, QLabel, QLineEdit, \
        QListWidget, QMainWindow, QMenu, QMessageBox, QProgressBar, QPushButton, QSizePolicy, QTableWidget, \
        QTableWidgetItem, QDialog, QShortcut
    from additional_classes import QPushButtonRight, convert_bin_txt, convert_txt_bin, create_seed, alpha
    from translate import Translate
    from setTheme import SetTheme, dark_color, dark_background, dark_border, bright_background, bright_border, bright_alert
    from settings import WindowSettings
    from add_account import AddAccount
    from edit_account import EditAccount
except:
    try:
        import PyQt5
    except:
        print('PyQt5 is not installed')
        quit()

"""
1515 lignes le 23/03/2022 à 18h
password : strongpassword
seed     : 758
"""
