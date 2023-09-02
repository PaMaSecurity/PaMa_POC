from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QFrame, QListWidget, QComboBox, QMessageBox, QSpinBox, QPushButton
from PyQt5.QtGui import QPixmap, QIcon, QFont
from setTheme import *
from pickle import dump
from additional_classes import alpha, convert_bin_txt, convert_txt_bin, create_seed, easy_password
from re import search
from hashlib import sha3_512


class WindowSettings(QDialog):
    def __init__(self, main_self):
        super().__init__(None, Qt.WindowCloseButtonHint | Qt.WindowTitleHint)
        ### hide the window
        self.hide()
        ### make the window modal
        self.setWindowModality(Qt.ApplicationModal)
        ### access the main self
        self.main_self = main_self
        ### create the list of keyword for search
        self.command_list = []
        self.keyword_list = [['language', 'langue', 'translate', 'traduire', 'français', 'french', 'english', 'anglais'],
                             ['theme', 'thème', 'bright', 'lumineux', 'dark', 'sombre', 'white', 'blanc', 'black', 'noir', 'light', 'clair'],
                             ['timer', 'minuteur', 'minuterie', 'time', 'temps'],
                             ['mot', 'de', 'passe', 'mot de', 'mot de passe', 'mots', 'mots de', 'mots de passe', 'mots de passes', 'mot de passes', 'password', 'main', 'principal']]
        ### build the window
        self.build()

    def build(self):
        ### window
        ## give an icon to the window
        self.setWindowIcon(QIcon('resources/settings_icon.svg'))
        ## set a fix size to the window
        self.setFixedSize(1000, 700)
        ## background
        self.background = QFrame(self)
        self.background.setFixedSize(self.width(), self.height())
        self.background.move(0, 0)

        ### Search bar
        ## search result
        self.searchResults = QListWidget(self)
        self.searchResults.setGeometry(0, 70, 200, self.width() - 51)
        self.searchResults.itemClicked.connect(self.searchResultsAction)
        ## first background
        self.searchFirstBackground = QFrame(self)
        self.searchFirstBackground.setFixedSize(self.searchResults.width(), 55)
        self.searchFirstBackground.move(self.searchResults.x(), self.searchResults.y() - self.searchFirstBackground.height())
        ## background
        self.searchBackground = QFrame(self)
        self.searchBackground.setFixedSize(180, 36)
        self.searchBackground.move(8, 24)
        ## search bar icon
        self.searchBarIcon = QLabel(self)
        searchIcon = QPixmap('resources/search_icon.svg')
        self.searchBarIcon.setPixmap(searchIcon)
        self.searchBarIcon.setGeometry(16, 34, searchIcon.width(), searchIcon.height())
        ## search bar QLineEdit
        self.searchBar = QLineEdit(self)
        self.searchBar.setFixedSize(140, 25)
        self.searchBar.textChanged.connect(self.search)
        self.searchBar.move(40, 30)
        ## show all possibilities
        self.search()

        ### translate QFrame
        self.translate_area = QFrame(self)
        self.translate_area.setFixedSize(self.width() - self.searchResults.width(), self.height())
        self.translate_area.move(self.searchResults.width(), 0)
        self.translate_area.setStyleSheet('background: #ffffff;')
        self.translate_area.hide()
        ## label
        self.select_languageLabel = QLabel(self.translate_area)
        self.select_languageLabel.setFont(QFont('Arial', 15))
        self.select_languageLabel.setFixedSize(250, self.select_languageLabel.height())
        self.select_languageLabel.move(20, 20)
        ## language QComboBox
        self.languageComboBox = QComboBox(self.translate_area)
        self.languageComboBox.setFixedSize(100, 25)
        self.languageComboBox.move(40, 50)
        self.languageComboBoxList()
        self.languageComboBox.currentTextChanged.connect(self.changeLanguage)

        ### display_theme QFrame
        self.theme_area = QFrame(self)
        self.theme_area.setFixedSize(self.width() - self.searchResults.width(), self.height())
        self.theme_area.move(self.searchResults.width(), 0)
        self.theme_area.setStyleSheet('background: #ffffff;')
        self.theme_area.hide()
        ## label
        self.select_themeLabel = QLabel(self.theme_area)
        self.select_themeLabel.setFont(QFont('Arial', 15))
        self.select_themeLabel.setFixedSize(380, self.select_themeLabel.height())
        self.select_themeLabel.move(20, 20)
        ## display QComboBox
        self.themeComboBox = QComboBox(self.theme_area)
        self.themeComboBox.setFixedSize(100, 25)
        self.themeComboBox.move(40, 50)
        self.themeComboBoxList()
        self.themeComboBox.currentTextChanged.connect(self.changeTheme)

        ### timer QFrame
        self.timer_area = QFrame(self)
        self.timer_area.setFixedSize(self.width() - self.searchResults.width(), self.height())
        self.timer_area.move(self.searchResults.width(), 0)
        self.timer_area.setStyleSheet('background: #ffffff;')
        self.timer_area.hide()
        ## label
        self.select_timeLabel = QLabel(self.timer_area)
        self.select_timeLabel.setFont(QFont('Arial', 15))
        self.select_timeLabel.setFixedSize(380, self.select_timeLabel.height())
        self.select_timeLabel.move(20, 20)
        ## spin
        self.time_spin = QSpinBox(self.timer_area)
        self.time_spin.valueChanged.connect(self.update_timer)
        self.time_spin.setValue(self.main_self.time//10)
        self.time_spin.setRange(1, 120)
        self.time_spin.setSuffix(' s')
        self.time_spin.setFixedSize(60, self.time_spin.height())
        self.time_spin.move(40, 50)

        ### main_password QFrame
        self.mainPassword_area = QFrame(self)
        self.mainPassword_area.setFixedSize(self.width() - self.searchResults.width(), self.height())
        self.mainPassword_area.move(self.searchResults.width(), 0)
        self.mainPassword_area.setStyleSheet('background: #ffffff')
        self.mainPassword_area.hide()
        ## label
        self.change_passwordLabel = QLabel(self.mainPassword_area)
        self.change_passwordLabel.setFont(QFont('Arial', 15))
        self.change_passwordLabel.setFixedSize(570, self.change_passwordLabel.height())
        self.change_passwordLabel.move(20, 20)
        ## QLineEdit
        self.change_passwordEntry = QLineEdit(self.mainPassword_area)
        self.change_passwordEntry.setFixedSize(300, self.change_passwordEntry.height())
        self.change_passwordEntry.move(20, 60)
        ## see / not see
        self.change_passwordEntry.setEchoMode(QLineEdit.Password)
        self.password_isVisible = False
        self.is_visible = QPushButton(self.change_passwordEntry)
        self.is_visible.setCursor(Qt.ArrowCursor)
        if self.main_self.theme == 'dark':
            self.is_visible.setIcon(QIcon('resources/dark_open_eye.png'))
        elif self.main_self.theme == 'bright':
            self.is_visible.setIcon(QIcon('resources/open_eye.svg'))
        self.is_visible.setStyleSheet('border: 0px;')
        self.is_visible.clicked.connect(self.visible)
        self.is_visible.move(self.change_passwordEntry.width() - 30, 5)
        ## QLineEdit Alert
        self.change_passwordAlert = QLabel(self.mainPassword_area)
        self.change_passwordAlert.setFont(QFont('Arial Nova Light', 8))
        self.change_passwordAlert.setFixedSize(350, self.change_passwordAlert.height())
        self.change_passwordAlert.move(self.change_passwordEntry.geometry().x(), self.change_passwordEntry.geometry().y()+self.change_passwordAlert.height())
        ## QPushButton
        self.confirm_passwordButton = QPushButton(self.mainPassword_area)
        self.confirm_passwordButton.setFixedSize(100, self.change_passwordEntry.height()-10)
        self.confirm_passwordButton.move(self.change_passwordEntry.geometry().x()+self.change_passwordEntry.width()+10, self.change_passwordEntry.geometry().y()+5)
        self.confirm_passwordButton.clicked.connect(self.changePassword)

        ### translate
        self.translate(self.main_self.language, False)

        ### setTheme
        self.setTheme(self.main_self.theme, False)

        self.searchResultsAction(item=self)
        ### display window
        self.show()

    def visible(self):
        if not self.password_isVisible:
            self.change_passwordEntry.setEchoMode(QLineEdit.Normal)
            if self.main_self.theme == 'dark':
                self.is_visible.setIcon(QIcon('resources/dark_close_eye.png'))
            elif self.main_self.theme == 'bright':
                self.is_visible.setIcon(QIcon('resources/close_eye.svg'))
            self.password_isVisible = True
        else:
            self.change_passwordEntry.setEchoMode(QLineEdit.Password)
            if self.main_self.theme == 'dark':
                self.is_visible.setIcon(QIcon('resources/dark_open_eye.png'))
            elif self.main_self.theme == 'bright':
                self.is_visible.setIcon(QIcon('resources/open_eye.svg'))
            self.password_isVisible = False

    def changePassword(self):
        password = self.change_passwordEntry.text().replace(' ', '')

        error_list = list(set(i for i in password if not i in alpha))

        # reset change_passwordAlert and the correct StyleSheet on all entries
        self.change_passwordAlert.setText("")

        if error_list:
            if self.main_self.language == 'french':
                self.change_passwordAlert.setText(f"Vous ne pouvez pas utilisez le{'s' if len(error_list) != 1 else ''} caractère{'s' if len(error_list) != 1 else ''} suivant: '" + "', '".join(error_list)+"'")
            elif self.main_self.language == 'english':
                self.change_passwordAlert.setText(f"You cannot use the following character{'s' if len(error_list) != 1 else ''}: '" + "', '".join(error_list)+"'")
        elif password in easy_password or search(r'(\d+([/\-|\\])\d+([/\-|\\])\d+)', password) is not None:
            if self.main_self.language == 'french':
                self.change_passwordAlert.setText("Votre mot de passe est trop facile")
            elif self.main_self.language == 'english':
                self.change_passwordAlert.setText("Your password is too easy")
        elif len(password) <= 4:
            if self.main_self.language == 'french':
                self.change_passwordAlert.setText("Votre mot de passe doit contenir au moins 5 caractères")
            elif self.main_self.language == 'english':
                self.change_passwordAlert.setText("Your password must contain at least 5 characters")
        elif search(r'(\d+)', password) is None:
            if self.main_self.language == 'french':
                self.change_passwordAlert.setText("Votre mot de passe doit contenir au moins un chiffre")
            elif self.main_self.language == 'english':
                self.change_passwordAlert.setText("Your password must contain at least one digit")
        elif search(r'([A-Z])', password) is None:
            if self.main_self.language == 'french':
                self.change_passwordAlert.setText("Votre mot de passe doit contenir au moins une majuscule")
            elif self.main_self.language == 'english':
                self.change_passwordAlert.setText("Your password must contain at least one capital letter")
        elif search(r'([a-z])', password) is None:
            if self.main_self.language == 'french':
                self.change_passwordAlert.setText("Votre mot de passe doit contenir au moins une minuscule")
            elif self.main_self.language == 'english':
                self.change_passwordAlert.setText("Your password must contain at least one lower case letter")
        else:
            confirmPassword = QMessageBox()
            confirmPassword.setIcon(QMessageBox.Critical)
            confirmPassword.setWindowIcon(QIcon('resources/pama.ico'))
            if self.main_self.language == 'french':
                confirmPassword.setWindowTitle('Enregistrer')
                confirmPassword.setText(
                    "Voulez vous valider votre mot de passe sachant qu'il sera irrécupérable si vous l'oublier ?")
                confirmPassword.addButton("&Oui", QMessageBox.YesRole)
                confirmPassword.addButton("&Non", QMessageBox.NoRole)
            elif self.main_self.language == 'english':
                confirmPassword.setWindowTitle('Save')
                confirmPassword.setText(
                    "Do you want to validate your password knowing that it will be unrecoverable if you forget it?")
                confirmPassword.addButton("&Yes", QMessageBox.YesRole)
                confirmPassword.addButton("&No", QMessageBox.NoRole)
            confirmPassword.exec_()
            if confirmPassword.clickedButton().text() == '&Yes' or confirmPassword.clickedButton().text() == '&Oui':
                with open('files/password.txt', 'r') as f:
                    file = f.readlines()
                    f.close()
                tranFile = []
                for i in file:
                    tranFile.append(convert_bin_txt(i, self.main_self.seed))
                cipher_password = sha3_512(password.encode()).hexdigest()
                self.main_self.seed = create_seed(password)
                tranFile[0] = cipher_password
                file = []
                for i in tranFile:
                    file.append(convert_txt_bin(i, self.main_self.seed))
                with open('files/password.txt', 'w') as f:
                    for i in file:
                        f.write(i + '\n')
                self.change_passwordEntry.clear()

    def update_timer(self):
        self.main_self.time = self.time_spin.value() * 10
        variables = {'language': self.main_self.language, 'time': self.main_self.time, 'theme': self.main_self.theme}
        file = open('resources/variables.txt', "wb")
        dump(variables, file)
        file.close()

    def text(self):
        return self.command_list[0]

    def search(self):
        research = self.searchBar.text().lower()
        self.searchResults.clear()
        for i in range(len(self.command_list)):
            for j in self.keyword_list[i]:
                if research in j:
                    self.searchResults.addItem(self.command_list[i])
                    break

    def searchResultsAction(self, item):
        item = item.text()

        if item == self.command_list[0] or item in self.keyword_list[0]:  # translate
            self.translate_area.show()
            self.theme_area.hide()
            self.timer_area.hide()
            self.mainPassword_area.hide()
        elif item == self.command_list[1] or item in self.keyword_list[1]:  # display theme
            self.translate_area.hide()
            self.theme_area.show()
            self.timer_area.hide()
            self.mainPassword_area.hide()
        elif item == self.command_list[2] or item in self.keyword_list[2]:  # timer
            self.translate_area.hide()
            self.theme_area.hide()
            self.timer_area.show()
            self.mainPassword_area.hide()
        elif item == self.command_list[3] or item in self.keyword_list[3]:  # main password
            self.translate_area.hide()
            self.theme_area.hide()
            self.timer_area.hide()
            self.mainPassword_area.show()

        ### update
        self.time_spin.setValue(self.main_self.time // 10)

    def changeTheme(self):
        currentText = self.themeComboBox.currentText()
        if currentText == 'Sombre' or currentText == 'Dark':
            self.setTheme(theme='dark', update=True)
        elif currentText == 'Bright' or currentText == 'Lumineux':
            self.setTheme(theme='bright', update=True)

    def changeLanguage(self):
        currentText = self.languageComboBox.currentText()
        if currentText == 'Français':
            self.translate(language='french', update=True)
        elif currentText == 'English':
            self.translate(language='english', update=True)

    def themeComboBoxList(self):
        self.themeComboBox.clear()
        if self.main_self.language == 'french':
            self.themeComboBox.addItems(['Lumineux', 'Sombre'])
        elif self.main_self.language == 'english':
            self.themeComboBox.addItems(['Bright', 'Dark'])

        if self.main_self.theme == 'dark':
            self.themeComboBox.setCurrentIndex(1)
        elif self.main_self.theme == 'bright':
            self.themeComboBox.setCurrentIndex(0)

    def languageComboBoxList(self):
        self.languageComboBox.clear()
        self.languageComboBox.addItems(['English', 'Français'])
        if self.main_self.language == 'french':
            self.languageComboBox.setCurrentIndex(1)
        elif self.main_self.language == 'english':
            self.languageComboBox.setCurrentIndex(0)

    def setTheme(self, theme, update=False):
        if theme == 'dark':
            self.background.setStyleSheet(f'background: #{dark_background};')
            self.searchBackground.setStyleSheet(
                f'color: #{dark_color_entry}; background: #{dark_background_entry}; border-radius: 4px;')
            self.searchBar.setStyleSheet(
                f'color: #{dark_color_entry}; background: #{dark_background_entry}; border: 0px; selection-background-color: #{selection_color}; selection-color: #000000;')
            self.searchResults.setStyleSheet(
                f'color: #{dark_color}; background: #{dark_background}; border-top: 0px solid #{dark_border};'
                f'border-bottom: 0px solid #{dark_border}; border-right: 1px solid #{dark_border}; border-left: 0px solid #{dark_border};')
            self.searchFirstBackground.setStyleSheet(
                f'color: #{dark_color}; background: #{dark_background}; border-top: 1px solid #{dark_border};'
                f'border-bottom: 0px solid #{dark_border}; border-right: 1px solid #{dark_border}; border-left: 0px solid #{dark_border};')
            self.translate_area.setStyleSheet(f'background: #{dark_background};')
            self.select_languageLabel.setStyleSheet(f'color: #{dark_color};')
            self.languageComboBox.setStyleSheet(f'color: #{dark_color};')
            self.theme_area.setStyleSheet(f'background: #{dark_background};')
            self.select_themeLabel.setStyleSheet(f'color: #{dark_color};')
            self.themeComboBox.setStyleSheet(f'color: #{dark_color};')
            self.timer_area.setStyleSheet(f'background: #{dark_background};')
            self.select_timeLabel.setStyleSheet(f'color: #{dark_color};')
            self.time_spin.setStyleSheet(f'color: #{dark_color}')
            self.mainPassword_area.setStyleSheet(f'background: #{dark_background};')
            self.change_passwordLabel.setStyleSheet(f'color: #{dark_color};')
            self.change_passwordEntry.setStyleSheet(
                f'background: #{dark_background}; color: #{dark_color}; border: 1px solid #{dark_entry_border}; border-radius: 1px;')
            self.confirm_passwordButton.setStyleSheet(
                'QPushButton{background: #' + dark_background + '; color: #' + dark_color + '; border: 1px solid #' + dark_border + '; border-radius: 2px;}' +
                'QPushButton:hover{background: #' + dark_background_hover + ';}')
            self.change_passwordAlert.setStyleSheet(f'color: #{dark_alert}')

        elif theme == 'bright':
            self.background.setStyleSheet(f'background: #{bright_background};')
            self.searchBackground.setStyleSheet(
                f'background: #{bright_background_entry}; border-radius: 4px;')
            self.searchBar.setStyleSheet(
                f'background: #{bright_background_entry}; border: 0px;')
            self.searchResults.setStyleSheet(
                f'background: #{bright_background}; border-top: 0px solid #{bright_border}; border-bottom: 0px solid #{bright_border};'
                f'border-right: 1px solid #{bright_border}; border-left: 0px solid #{bright_border};')
            self.searchFirstBackground.setStyleSheet(
                f'background: #{bright_background}; border-top: 1px solid #{bright_border}; border-bottom: 0px solid #{bright_border};'
                f'border-right: 1px solid #{bright_border}; border-left: 0px solid #{bright_border};')
            self.translate_area.setStyleSheet(f'background: #{bright_background};')
            self.select_languageLabel.setStyleSheet('')
            self.languageComboBox.setStyleSheet('')
            self.theme_area.setStyleSheet(f'background: #{bright_background};')
            self.select_themeLabel.setStyleSheet('')
            self.themeComboBox.setStyleSheet('')
            self.timer_area.setStyleSheet(f'background: #{bright_background};')
            self.select_timeLabel.setStyleSheet('')
            self.time_spin.setStyleSheet('')
            self.mainPassword_area.setStyleSheet(f'background: #{bright_background};')
            self.change_passwordLabel.setStyleSheet('')
            self.change_passwordEntry.setStyleSheet(
                f'background: #{bright_background}; border: 1px solid #{bright_entry_border}; border-radius: 1px;')
            self.confirm_passwordButton.setStyleSheet(
                'QPushButton{background: #' + bright_background + '; border: 1px solid #' + bright_border + '; border-radius: 2px;}' +
                'QPushButton:hover{background: #' + bright_background_hover + ';}')
            self.change_passwordAlert.setStyleSheet(f'color: #{bright_alert}')

        ### update
        if update:
            self.main_self.theme = theme
            self.main_self.setTheme(self.main_self.theme)
            self.main_self.data_in_table(self.main_self)
            self.main_self.translate(self.main_self.language)

    def translate(self, language, update=False):
        if language == 'french':
            self.setWindowTitle('Paramètres')
            self.searchBar.setPlaceholderText('Recherche')
            self.select_languageLabel.setText('Sélectionner la langue:')
            self.select_themeLabel.setText('Choisissez le thème du logiciel:')
            self.select_timeLabel.setText('Choisissez le temps du minuteur:')
            self.change_passwordLabel.setText('Choisissez le nouveau mot de passe pour déverrouiller le logiciel:')
            self.confirm_passwordButton.setText('Confirmer')
            self.command_list = ['Langue', 'Thème', 'Minuteur', 'Mot de passe principal']

        elif language == 'english':
            self.setWindowTitle('Settings')
            self.searchBar.setPlaceholderText('Search')
            self.select_languageLabel.setText('Select language:')
            self.select_themeLabel.setText('Choose the theme of the software:')
            self.select_timeLabel.setText('Choose the timer time:')
            self.change_passwordLabel.setText('Choose the new password to unlock the software')
            self.confirm_passwordButton.setText('Confirm')
            self.command_list = ['Language', 'Theme', 'Timer', 'Main password']

        ### update
        self.search()
        if update:
            self.main_self.language = language
            self.main_self.translate(self.main_self.language)

    def keyPressEvent(self, event):
        if event.modifiers() & Qt.ControlModifier:
            if event.key() == Qt.Key_Q:
                self.close()