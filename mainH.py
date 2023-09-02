### imports
try:
    import hashlib
    from sys import exit as sys_exit, argv as sys_argv
    from pickle import dump, load
    from functools import partial
    from PyQt5.QtCore import Qt, QTimer
    from PyQt5.QtGui import QCursor, QFont, QIcon, QPixmap, QKeySequence
    from PyQt5.QtWidgets import QAbstractItemView, QAction, QApplication, QFrame, QHeaderView, QLabel, QLineEdit, \
        QListWidget, QMainWindow, QMenu, QMessageBox, QProgressBar, QPushButton, QSizePolicy, QTableWidget, \
        QTableWidgetItem, QDialog, QShortcut, QGraphicsView, QGraphicsPixmapItem, QGraphicsScene, QListWidgetItem
    from os import popen
    from additions import QPushButtonRight, convert_bin_txt, convert_txt_bin, create_seed, alpha, easy_password, \
        default_folder_name, french, english, dark, bright, dark_color, dark_background, dark_border, \
        bright_background, bright_border, bright_alert, dark_background_hover, bright_background_hover
    from translate import Translate
    from setTheme import SetTheme
    from settings import WindowSettings
    from add_account import AddAccount
    from edit_account import EditAccount
    from re import search as search_reg_exp
except:
    try:
        import hashlib
    except:
        print("error code 1: hashlib")
    try:
        from sys import exit as sys_exit, argv as sys_argv
    except:
        print("error code 1: sys")
    try:
        from pickle import dump, load
    except:
        print("error code 1: pickle")
    try:
        from functools import partial
    except:
        print("error code 1: functools")
    try:
        from PyQt5.QtCore import Qt, QTimer
    except:
        print("error code 1: PyQt5.QtCore")
    try:
        from PyQt5.QtGui import QCursor, QFont, QIcon, QPixmap, QKeySequence
    except:
        print("error code 1: PyQt5.QtGui")
    try:
        from PyQt5.QtWidgets import QAbstractItemView, QAction, QApplication, QFrame, QHeaderView, QLabel, QLineEdit, \
            QListWidget, QMainWindow, QMenu, QMessageBox, QProgressBar, QPushButton, QSizePolicy, QTableWidget, \
            QTableWidgetItem, QDialog, QShortcut, QGraphicsView, QGraphicsPixmapItem, QGraphicsScene, QListWidgetItem
    except:
        print("error code 1: PyQt5.QtWidgets")
    try:
        from re import search
    except:
        print("error code 1: re")
    try:
        from os import popen
    except:
        print("error code 1: os")
    try:
        from additions import QPushButtonRight, convert_bin_txt, convert_txt_bin, create_seed, alpha, easy_password, \
            default_folder_name, french, english, dark, bright, dark_color, dark_background, dark_border, \
            bright_background, bright_border, bright_alert, dark_background_hover, bright_background_hover
    except:
        print("error code 1: additions")
    try:
        from translate import Translate
    except:
        print("error code 1: translate")
    try:
        from setTheme import SetTheme, dark_color, dark_background, dark_border, bright_background, bright_border, \
            bright_alert, dark_background_hover, bright_background_hover
    except:
        print("error code 1: setTheme")
    try:
        from settings import WindowSettings
    except:
        print("error code 1: settings")
    try:
        from add_account import AddAccount
    except:
        print("error code 1: add_account")
    try:
        from edit_account import EditAccount
    except:
        print("error code 1: edit_account")
    try:
        from re import search as search_reg_exp
    except:
        print("error code 1: re")
    quit()