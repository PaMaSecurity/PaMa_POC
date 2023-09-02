### imports
try:
    import hashlib
    from sys import exit as sys_exit, argv as sys_argv
    from pickle import dump, load
    from functools import partial
    from PyQt5.QtCore import Qt, QTimer, pyqtSlot, QModelIndex, QSize
    from PyQt5.QtGui import QCursor, QFont, QIcon, QPixmap, QKeySequence, QKeyEvent, QWheelEvent
    from PyQt5.QtWidgets import QAbstractItemView, QAction, QApplication, QFrame, QHeaderView, QLabel, QLineEdit, \
        QListWidget, QMainWindow, QMenu, QMessageBox, QProgressBar, QPushButton, QSizePolicy, QTreeWidget, \
        QTableWidgetItem, QDialog, QShortcut, QGraphicsView, QGraphicsPixmapItem, QGraphicsScene, QListWidgetItem, \
        QTreeWidgetItem, QScrollBar
    from re import search
    from os import popen, path
    from additions import *
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
        from PyQt5.QtCore import Qt, QTimer, pyqtSlot, QModelIndex, QSize
    except:
        print("error code 1: QtCore")
    try:
        from PyQt5.QtGui import QCursor, QFont, QIcon, QPixmap, QKeySequence, QKeyEvent, QWheelEvent
    except:
        print("error code 1: QtGui")
    try:
        from PyQt5.QtWidgets import QAbstractItemView, QAction, QApplication, QFrame, QHeaderView, QLabel, QLineEdit, \
            QListWidget, QMainWindow, QMenu, QMessageBox, QProgressBar, QPushButton, QSizePolicy, QTreeWidget, \
            QTableWidgetItem, QDialog, QShortcut, QGraphicsView, QGraphicsPixmapItem, QGraphicsScene, QListWidgetItem, \
            QTreeWidgetItem
    except:
        print("error code 1: QtWidgets")
    try:
        from re import search
    except:
        print("error code 1: re")
    try:
        from os import popen, path
    except:
        print("error code 1: os")
    try:
        from additions import *
    except:
        print("error code 1: additions")
    try:
        from translate import Translate
    except:
        print("error code 1: translate")
    try:
        from setTheme import SetTheme
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