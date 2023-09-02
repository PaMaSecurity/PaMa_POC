from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QFrame, QListWidget, QComboBox, QMessageBox, QSpinBox
from PyQt5.QtGui import QPixmap, QIcon, QFont
from setTheme import *
from pickle import dump


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
                             ['timer', 'minuteur', 'minuterie', 'time', 'temps']]
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

        ### translate
        self.translate(self.main_self.language, False)

        ### setTheme
        self.setTheme(self.main_self.theme, False)

        self.searchResultsAction(item=self)
        ### display window
        self.show()

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
            self.timer_area.hide()
            self.theme_area.hide()
            self.translate_area.show()
        elif item == self.command_list[1] or item in self.keyword_list[1]:  # display theme
            self.translate_area.hide()
            self.timer_area.hide()
            self.theme_area.show()
        elif item == self.command_list[2] or item in self.keyword_list[2]:
            self.theme_area.hide()
            self.translate_area.hide()
            self.timer_area.show()
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
            self.command_list = ['Langue', 'Thème', 'Minuteur']

        elif language == 'english':
            self.setWindowTitle('Settings')
            self.searchBar.setPlaceholderText('Search')
            self.select_languageLabel.setText('Select language:')
            self.select_themeLabel.setText('Choose the theme of the software:')
            self.select_timeLabel.setText('Choose the timer time:')
            self.command_list = ['Language', 'Theme', 'Timer']

        ### update
        self.search()
        if update:
            self.main_self.language = language
            self.main_self.data_in_table(self.main_self)
            self.main_self.translate(self.main_self.language)
            self.main_self.search()
            self.themeComboBoxList()

    def keyPressEvent(self, event):
        if event.modifiers() & Qt.ControlModifier:
            if event.key() == Qt.Key_Q:
                self.close()