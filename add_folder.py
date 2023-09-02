from PyQt5.QtWidgets import QDialog, QFrame, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from additions import alpha, french, english, dark, bright, \
    dark_background, dark_color, dark_entry_border, dark_alert, dark_background_hover, dark_border, \
    bright_background, bright_color, bright_entry_border, dark_alert, bright_background_hover, bright_border


class AddFolder(QDialog):

    def __init__(self, main_self, language, theme):
        super().__init__(None, Qt.WindowCloseButtonHint | Qt.WindowTitleHint)
        ### hide the window
        self.hide()
        ### make the window modal
        self.setWindowModality(Qt.ApplicationModal)
        ### access the main self
        self.main_self = main_self
        self.language = language
        self.theme = theme
        ### build the window
        self.build()

    def build(self):
        ### window
        ## give an icon to the window
        self.setWindowIcon(QIcon('resources/pama.ico'))
        ## set a fix size to the window
        self.setFixedSize(370, 135)
        ## background
        self.background = QFrame(self)
        self.background.setFixedSize(self.width(), self.height())
        self.background.move(0, 0)

        ### New account name
        ## new_accName_label
        self.new_folderLabel = QLabel(self)
        self.new_folderLabel.setFont(QFont('Arial Nova Light', 12))
        self.new_folderLabel.move(10, 10)
        ## QLineEdit Name
        self.new_folder = QLineEdit(self)
        self.new_folder.setFont(QFont('Arial Nova Light', 10))
        self.new_folder.resize(350, self.new_folder.height())
        self.new_folder.move(self.new_folderLabel.geometry().x(), self.new_folderLabel.geometry().y() + 30)
        ## new_accNameError
        self.new_folderError = QLabel(self)
        self.new_folderError.setFont(QFont('Arial Nova Light', 8))
        self.new_folderError.setFixedWidth(300)
        self.new_folderError.move(self.new_folderLabel.geometry().x(), self.new_folder.geometry().y() + 32)

        ### Confirm Button
        self.confirmButton = QPushButton(self)
        self.confirmButton.setFont(QFont("Times", 12))
        self.confirmButton.setFixedSize(100, 20)
        self.confirmButton.clicked.connect(self.addFolder)
        self.confirmButton.move((self.width()-self.confirmButton.width())//2, self.new_folderError.geometry().y()+self.new_folderError.height())

        ### translate
        self.translate(self.language)

        ### setTheme
        self.setTheme(self.theme)

        ### display window
        self.show()

    def addFolder(self):
        if self.theme == dark:
            self.new_folder.setStyleSheet(
                f'background: #{dark_background}; color: #{dark_color}; border: 1px solid #{dark_entry_border}; border-radius: 1px;')
        elif self.theme == bright:
            self.new_folder.setStyleSheet(
                f'background: #{bright_background}; border: 1px solid #{bright_entry_border}; border-radius: 1px;')

        new_folder = self.new_folder.text().replace(' ', '')
        error_list = list(set(i for i in new_folder if not i in alpha))
        if error_list:
            if self.theme == dark:
                self.new_folder.setStyleSheet(
                    f'background: #{dark_background}; color: #{dark_color}; border: 1px solid #{dark_entry_border}; border-radius: 1px; border-bottom-color: #{dark_alert};')
            elif self.theme == bright:
                self.new_folder.setStyleSheet(
                                f'background: #{bright_background}; color: #{bright_color}; border: 1px solid #{bright_entry_border}; border-radius: 1px; border-bottom: 2px solid #{bright_alert};')
            if self.language == french:
                self.new_folderError.setText(
                                f'Vous ne pouvez pas utiliser le{"s" if len(error_list) > 1 else ""} caractère{"s" if len(error_list) > 1 else ""}: {"".join(error_list)}!')
            elif self.language == english:
                self.new_folderError.setText(
                            f'You cannot use the character{"s" if len(error_list) > 1 else ""}: {"".join(error_list)}!')
        elif new_folder.lower() in [i.lower() for i in self.main_self.folderList_copy]:
            if self.theme == dark:
                self.new_folder.setStyleSheet(
                    f'background: #{dark_background}; color: #{dark_color}; border: 1px solid #{dark_entry_border}; border-radius: 1px; border-bottom-color: #{dark_alert};')
            elif self.theme == bright:
                self.new_folder.setStyleSheet(
                                f'background: #{bright_background}; color: #{bright_color}; border: 1px solid #{bright_entry_border}; border-radius: 1px; border-bottom: 2px solid #{bright_alert};')
            if self.language == french:
                self.new_folderError.setText('Le nom est déjà pris...')
            elif self.language == english:
                self.new_folderError.setText('The name is already taken...')
        else:
            self.main_self.folderList_copy.append(new_folder)
            self.main_self.choose_folderComboBox.addItem(new_folder)
            self.close()

    def setTheme(self, theme):
        if theme == dark:
            self.background.setStyleSheet(f'background: #{dark_background};')
            ### account name
            self.new_folderLabel.setStyleSheet(f'color: #{dark_color}')
            self.new_folder.setStyleSheet(
                f'background: #{dark_background}; color: #{dark_color}; border: 1px solid #{dark_entry_border}; border-radius: 1px;')
            self.new_folderError.setStyleSheet(f'color: #{dark_alert}')
            ### confirm button
            self.confirmButton.setStyleSheet(
                'QPushButton{background: #' + dark_background + '; color: #' + dark_color + '; border: 1px solid #' + dark_border + '; border-radius: 2px;}' +
                'QPushButton:hover{background: #' + dark_background_hover + ';}')
        elif theme == bright:
            self.background.setStyleSheet(f'background: #{bright_background};')
            ### account name
            self.new_folderLabel.setStyleSheet(f'color: #{bright_color}')
            self.new_folder.setStyleSheet(
                f'background: #{bright_background}; color: #{bright_color}; border: 1px solid #{bright_entry_border}; border-radius: 1px;')
            self.new_folderError.setStyleSheet(f'color: #{dark_alert}')
            ### confirm button
            self.confirmButton.setStyleSheet(
                'QPushButton{background: #' + bright_background + '; border: 1px solid #' + bright_border + '; border-radius: 2px;}' +
                'QPushButton:hover{background: #' + bright_background_hover + ';}')

    def translate(self, language):
        if language == french:
            self.setWindowTitle('Ajouter un dossier')
            self.new_folderLabel.setText("Choisissez le nom du nouveau dossier")
            self.confirmButton.setText("Confirmer")
        elif language == english:
            self.setWindowTitle('Add a folder')
            self.new_folderLabel.setText("Choose the new folder name")
            self.confirmButton.setText("Confirm")

    def keyPressEvent(self, event):
        if event.modifiers() & Qt.ControlModifier:
            if event.key() == Qt.Key_Q:
                self.quit()
            if event.key() == Qt.Key_S:
                self.addFolder()
        if event.key() == Qt.Key_Return:
            self.addFolder()

    def quit(self):
        self.close()