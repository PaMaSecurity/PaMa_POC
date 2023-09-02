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
        QTableWidgetItem, QDialog, QShortcut, QGraphicsView, QGraphicsPixmapItem, QGraphicsScene
    from re import search
    from os import popen
    from additional_classes import QPushButtonRight, convert_bin_txt, convert_txt_bin, create_seed, alpha, easy_password
    from translate import Translate
    from setTheme import SetTheme, dark_color, dark_background, dark_border, bright_background, bright_border, bright_alert, dark_background_hover, bright_background_hover
    from settings import WindowSettings
    from add_account import AddAccount
    from edit_account import EditAccount
except:
    try:
        import PyQt5
    except:
        print('PyQt5 is not installed')
        quit()