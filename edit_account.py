from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QFrame, QLabel, QLineEdit, QPushButton, QMessageBox, QApplication, QCompleter
from PyQt5.QtGui import QIcon, QFont
import random
from additions.cryptography import *
from additions.constants import *


class EditAccount(QDialog):
    def __init__(self, main_self, index):
        super().__init__(None, Qt.WindowCloseButtonHint | Qt.WindowTitleHint)
        ### hide the window
        self.hide()
        ### make the window modal
        self.setWindowModality(Qt.ApplicationModal)
        ### access the main self
        self.main_self = main_self
        part: list[str] = self.main_self.liste[index]
        self.accName = part[0]
        self.accAlias = part[1]
        self.accID = part[2]
        self.accEmail = part[3]
        self.accPassword = part[4]
        ### build the window
        self.build()

    def build(self):
        ### différentes polices:
        self.fontLabel = QFont('Arial Nova Light', 12)
        self.fontEntry = QFont('Arial Nova Light', 10)
        self.fontError = QFont('Arial Nova Light', 8)

        ### window
        ## give an icon to the window
        self.setWindowIcon(QIcon('resources/pama.ico'))
        ## set a fix size to the window
        self.setFixedSize(700, 550)
        ## background
        self.background = QFrame(self)
        self.background.setStyleSheet('background: #ffffff;')
        self.background.setFixedSize(self.width(), self.height())
        self.background.move(0, 0)

        # ### Folder
        # ## choose_folderLabel
        # self.choose_folderLabel = QLabel(self)
        # self.choose_folderLabel.setFont(self.fontLabel)
        # self.choose_folderLabel.move(10, 10)
        # ## choose_folderComboBox
        # self.choose_folderComboBox = QComboBox(self.background)
        # self.choose_folderComboBox.activated.connect(lambda: self.choose_folderComboBox.clearFocus())
        # self.choose_folderComboBox.setFixedSize(100, 25)
        # self.choose_folderComboBox.move(self.choose_folderLabel.geometry().x(), self.choose_folderLabel.geometry().y() + 30)
        # self.choose_folderComboBox.addItems(self.folderList_copy)
        # if self.accFolder != default_folder_name:
        #     self.choose_folderComboBox.setCurrentIndex(self.folderList_copy.index(self.accFolder))
        # else:
        #     self.choose_folderComboBox.setCurrentIndex(0)
        # # self.choose_folderComboBox.setPlaceholderText("Choisissez le dossier")
        # ## add_folderButton
        # self.add_folderButton = QPushButton(self)
        # self.add_folderButton.setFont(self.fontEntry)
        # self.add_folderButton.setFixedSize(120, 25)
        # self.add_folderButton.clicked.connect(self.add_folder)
        # self.add_folderButton.move(self.choose_folderComboBox.width() + self.choose_folderComboBox.geometry().x() + 10,
        #                            self.choose_folderLabel.geometry().y() + 30)
        # ## choose_folderError
        # self.choose_folderError = QLabel(self)
        # self.choose_folderError.setFont(self.fontError)
        # self.choose_folderError.setFixedWidth(300)
        # self.choose_folderError.move(self.choose_folderLabel.geometry().x(), self.add_folderButton.geometry().y() + 28)

        ### New account name
        ## new_accName_label
        self.new_accName_label = QLabel(self)
        self.new_accName_label.setFont(self.fontLabel)
        self.new_accName_label.move(10, 10)
        ## QLineEdit Name
        self.new_accName = QLineEdit(self)
        self.new_accName.setFont(self.fontEntry)
        self.new_accName.resize(350, self.new_accName.height())
        self.new_accName.move(self.new_accName_label.geometry().x(), self.new_accName_label.geometry().y() + 30)
        self.new_accName.insert(self.accName)
        ## new_accNameError
        self.new_accNameError = QLabel(self)
        self.new_accNameError.setFont(self.fontError)
        self.new_accNameError.setFixedWidth(300)
        self.new_accNameError.move(self.new_accName_label.geometry().x(), self.new_accName.geometry().y() + 32)

        ### New account alias
        ## new_accAlias_label
        self.new_accAlias_label = QLabel(self)
        self.new_accAlias_label.setFont(self.fontLabel)
        self.new_accAlias_label.move(self.new_accName_label.geometry().x(), self.new_accNameError.geometry().y() + 20)
        ## QLineEdit Alias
        self.new_accAlias = QLineEdit(self)
        self.new_accAlias.setFont(self.fontEntry)
        self.new_accAlias.resize(350, self.new_accAlias.height())
        self.new_accAlias.move(self.new_accAlias_label.geometry().x(), self.new_accAlias_label.geometry().y() + 30)
        self.new_accAlias.insert("".join(self.accAlias))
        ## new_accAliasError
        self.new_accAliasError = QLabel(self)
        self.new_accAliasError.setFont(self.fontError)
        self.new_accAliasError.setFixedWidth(300)
        self.new_accAliasError.move(self.new_accAlias_label.geometry().x(), self.new_accAlias.geometry().y() + 32)

        ### New account id
        ## new_accID_label
        self.new_accID_label = QLabel(self)
        self.new_accID_label.setFont(self.fontLabel)
        self.new_accID_label.move(self.new_accName_label.geometry().x(), self.new_accAliasError.geometry().y() + 20)
        ## QLineEdit ID
        self.new_accID = QLineEdit(self)
        self.new_accID.setFont(self.fontEntry)
        self.new_accID.resize(350, self.new_accID.height())
        self.new_accID.move(self.new_accID_label.geometry().x(), self.new_accID_label.geometry().y() + 30)
        self.new_accID.insert(self.accID)
        ## new_accIDError
        self.new_accIDError = QLabel(self)
        self.new_accIDError.setFont(self.fontError)
        self.new_accIDError.setFixedWidth(300)
        self.new_accIDError.move(self.new_accID_label.geometry().x(), self.new_accID.geometry().y() + 32)

        ### New account email
        ## new_accEmail_label
        self.new_accEmail_label = QLabel(self)
        self.new_accEmail_label.setFont(self.fontLabel)
        self.new_accEmail_label.move(self.new_accName_label.geometry().x(), self.new_accIDError.geometry().y() + 20)
        ## QLineEdit Email
        self.new_accEmail = QLineEdit(self)
        self.new_accEmail.setFont(self.fontEntry)
        self.new_accEmail.resize(350, self.new_accEmail.height())
        self.new_accEmail.move(self.new_accEmail_label.geometry().x(), self.new_accEmail_label.geometry().y() + 30)
        self.new_accEmail.insert(self.accEmail)
        self.addressesList = [i for i in list(set(self.main_self.email_list)) if i != '']
        self.addressesCompleter = QCompleter(self.addressesList, self)
        self.addressesCompleter.setCaseSensitivity(Qt.CaseInsensitive)
        self.popupAddressesCompleter = self.addressesCompleter.popup()
        self.new_accEmail.setCompleter(self.addressesCompleter)
        ## new_accEmailError
        self.new_accEmailError = QLabel(self)
        self.new_accEmailError.setFont(self.fontError)
        self.new_accEmailError.setFixedWidth(300)
        self.new_accEmailError.move(self.new_accEmail_label.geometry().x(), self.new_accEmail.geometry().y() + 32)

        ### New account password
        ## new_accPassword_label
        self.new_accPassword_label = QLabel(self)
        self.new_accPassword_label.setFont(self.fontLabel)
        self.new_accPassword_label.move(self.new_accName_label.geometry().x(), self.new_accEmailError.geometry().y() + 20)
        ## QLineEdit password
        self.new_accPassword = QLineEdit(self)
        self.new_accPassword.setFont(self.fontEntry)
        self.new_accPassword.resize(350, self.new_accPassword.height())
        self.new_accPassword.move(self.new_accPassword_label.geometry().x(), self.new_accPassword_label.geometry().y() + 30)
        self.new_accPassword.insert(self.accPassword)
        ## new_accPasswordError
        self.new_accPasswordError = QLabel(self)
        self.new_accPasswordError.setFont(self.fontError)
        self.new_accPasswordError.setFixedWidth(300)
        self.new_accPasswordError.move(self.new_accPassword_label.geometry().x(),
                                       self.new_accPassword.geometry().y() + 32)
        # see / not to see
        self.new_accPassword.setEchoMode(QLineEdit.Password)
        self.password_isVisible = False
        self.is_visible = QPushButton(self.new_accPassword)
        self.is_visible.setCursor(Qt.ArrowCursor)
        if self.main_self.theme == dark:
            self.is_visible.setIcon(QIcon('resources/dark_open_eye.svg'))
        elif self.main_self.theme == bright:
            self.is_visible.setIcon(QIcon('resources/open_eye.svg'))
        self.is_visible.setStyleSheet('border: 0px;')
        self.is_visible.clicked.connect(self.visible)
        self.is_visible.move(self.new_accPassword.width() - 30, 5)
        ## generate password
        self.generatePassword_Button = QPushButton(self)
        self.generatePassword_Button.setFont(QFont('Arial Nova Light', 10))
        self.generatePassword_Button.clicked.connect(self.generatePassword)
        self.generatePassword_Button.move(self.new_accPassword_label.geometry().x(), self.new_accPasswordError.geometry().y() + 20)

        ### confirmButton
        self.confirmButton = QPushButton(self)
        self.confirmButton.setFont(QFont('Times', 17))
        self.confirmButton.setFixedSize(130, 30)
        self.confirmButton.move(self.width() - self.confirmButton.width() - 30,
                                self.height() - self.confirmButton.height() - 30)
        self.confirmButton.pressed.connect(self.try_save_accountInformations)

        ### translate
        self.translate(self.main_self.language)

        ### setTheme
        self.setTheme(self.main_self.theme)

        ### display window
        self.show()

        ### focus on new_accName
        self.new_accName.setFocus()

    def try_save_accountInformations(self):
        new_acc_list = [self.new_accName, self.new_accAlias, self.new_accID, self.new_accEmail, self.new_accPassword]
        new_acc_error_list = [self.new_accNameError, self.new_accAliasError, self.new_accIDError, self.new_accEmailError,
                            self.new_accPasswordError]

        # reset the correct StyleSheet on all entries
        if self.main_self.theme == dark:
            for i in new_acc_list:
                i.setStyleSheet(
                    f'background: #{dark_background}; color: #{dark_color}; border: 1px solid #{dark_entry_border}; border-radius: 1px;')

        elif self.main_self.theme == bright:
            for i in new_acc_list:
                i.setStyleSheet(
                    f'background: #{bright_background}; border: 1px solid #{bright_entry_border}; border-radius: 1px;')

        # reset error messages
        for i in new_acc_error_list:
            i.setText('')

        # retrieve keystrokes and put them in variables
        new_name = self.new_accName.text()
        new_alias = self.new_accAlias.text()
        new_id = self.new_accID.text()
        new_email = self.new_accEmail.text().replace(' ', '')
        new_password = self.new_accPassword.text().replace(' ', '')

        new_list = [new_name, new_alias, new_id, new_email, new_password]
        new_list_plus = [new_name, new_alias, new_id, new_email, new_password]
        list_plus = [self.accName, self.accAlias, self.accID, self.accEmail, self.accPassword]
        run = False
        for i in range(len(new_list_plus)):
            if new_list_plus[i] != list_plus[i]:
                run = True

        if run:
            # create error_list that contains all non-encrypt-able characters and delete duplicates with set()
            error_list = list(set(i for i in "".join(new_list) if i not in alpha))
            # create a list for each QLineEdit
            new_error_list = [[], [], [], [], []]

            if error_list:
                for i in error_list:
                    for j in range(len(new_list)):
                        if i in new_list[j]:
                            if self.main_self.theme == dark:
                                new_acc_list[j].setStyleSheet(
                                    f'background: #{dark_background}; color: #{dark_color}; border: 1px solid #{dark_entry_border}; border-radius: 1px; border-bottom-color: #{dark_alert};')
                            elif self.main_self.theme == bright:
                                new_acc_list[j].setStyleSheet(
                                    f'background: #{bright_background}; border: 1px solid #{bright_entry_border}; border-radius: 1px; border-bottom: 2px solid #{bright_alert};')
                            new_error_list[j].append(i)
                # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                if self.main_self.language == french:
                    for i in range(len(new_error_list)):
                        if new_error_list[i]:
                            new_acc_error_list[i].setText(
                                f'Vous ne pouvez pas utiliser le{"s" if len(new_error_list[i]) > 1 else ""} caractère{"s" if len(new_error_list[i]) > 1 else ""}: {"".join(new_error_list[i])}!')
                elif self.main_self.language == english:
                    for i in range(len(new_error_list)):
                        if new_error_list[i]:
                            new_acc_error_list[i].setText(
                                f'You cannot use the character{"s" if len(new_error_list[i]) > 1 else ""}: {"".join(new_error_list[i])}!')
            # //////////////////////////////////////////////////////////////////////////////////////////////////////////
            elif '--' in new_name or '--' in new_alias or '--' in new_id or '--' in new_email or '--' in new_password or \
                    '::' in new_name or '::' in new_alias or '::' in new_id or '::' in new_email or '::' in new_password or \
                    '//' in new_name or '//' in new_alias or '//' in new_id or '//' in new_email or '//' in new_password or \
                    '%%' in new_name or '%%' in new_alias or '%%' in new_id or '%%' in new_email or '%%' in new_password or \
                    ';;' in new_name or ';;' in new_alias or ';;' in new_id or ';;' in new_email or ';;' in new_password:
                if self.main_self.language == french:
                    message = "Vous ne pouvez pas utiliser '::', '//', '%%' ni ';;'."
                elif self.main_self.language == english:
                    message = "You cannot use '::', '//', '%%' or ';;'."
                # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                for i in range(len(new_list)):
                    if '--' in new_list[i] or '::' in new_list[i] or '//' in new_list[i] or '%%' in new_list[i] or ';;' in new_list[i]:
                        if self.main_self.theme == dark:
                            new_acc_list[i].setStyleSheet(
                                f'background: #{dark_background}; color: #{dark_color}; border: 1px solid #{dark_entry_border}; border-radius: 1px; border-bottom-color: #{dark_alert};')
                            new_acc_error_list[i].setText(message)
                        elif self.main_self.theme == bright:
                            new_acc_list[i].setStyleSheet(
                                f'background: #{bright_background}; border: 1px solid #{bright_entry_border}; border-radius: 1px; border-bottom: 2px solid #{bright_alert};')
                            new_acc_error_list[i].setText(message)
            # //////////////////////////////////////////////////////////////////////////////////////////////////////////
            elif new_name == '' or new_password == '':
                if not new_name:
                    if self.main_self.theme == dark:
                        self.new_accName.setStyleSheet(
                            f'background: #{dark_background}; color: #{dark_color}; border: 1px solid #{dark_entry_border}; border-radius: 1px; border-bottom-color: #{dark_alert};')
                    elif self.main_self.theme == bright:
                        self.new_accName.setStyleSheet(
                            f'background: #{bright_background}; border: 1px solid #{bright_entry_border}; border-radius: 1px; border-bottom: 2px solid #{bright_alert};')
                    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                    if self.main_self.language == french:
                        self.new_accNameError.setText('Ce champ de texte est obligatoire')
                    elif self.main_self.language == english:
                        self.new_accNameError.setText('This text field is mandatory')
                # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                if not new_password:
                    if self.main_self.theme == dark:
                        self.new_accPassword.setStyleSheet(
                            f'background: #{dark_background}; color: #{dark_color}; border: 1px solid #{dark_entry_border}; border-radius: 1px; border-bottom-color: #{dark_alert};')
                    elif self.main_self.theme == bright:
                        self.new_accPassword.setStyleSheet(
                            f'background: #{bright_background}; border: 1px solid #{bright_entry_border}; border-radius: 1px; border-bottom: 2px solid #{bright_alert};')
                    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                    if self.main_self.language == french:
                        self.new_accPasswordError.setText('Ce champ de texte est obligatoire')
                    elif self.main_self.language == english:
                        self.new_accPasswordError.setText('This text field is mandatory')
            # //////////////////////////////////////////////////////////////////////////////////////////////////////////
            elif new_name in [i for i in self.main_self.name_list if i != self.accName]:
                if self.main_self.theme == dark:
                    self.new_accName.setStyleSheet(
                        f'background: #{dark_background}; color: #{dark_color}; border: 1px solid #{dark_entry_border}; border-radius: 1px; border-bottom-color: #{dark_alert};')
                elif self.main_self.theme == bright:
                    self.new_accName.setStyleSheet(
                        f'background: #{bright_background}; border: 1px solid #{bright_entry_border}; border-radius: 1px; border-bottom: 2px solid #{bright_alert};')
                # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                if self.main_self.language == french:
                    self.new_accNameError.setText('Le nom est déjà pris...')
                elif self.main_self.language == english:
                    self.new_accNameError.setText('The name is already taken...')
            # //////////////////////////////////////////////////////////////////////////////////////////////////////////
            elif new_alias in [i for i in self.main_self.name_list if i != self.accName] or new_alias in [i for i in self.main_self.alias_list if i != '' and i != self.accAlias] or new_alias == new_name:
                if self.main_self.theme == dark:
                    self.new_accAlias.setStyleSheet(
                        f'background: #{dark_background}; color: #{dark_color}; border: 1px solid #{dark_entry_border}; border-radius: 1px; border-bottom-color: #{dark_alert};')
                elif self.main_self.theme == bright:
                    self.new_accAlias.setStyleSheet(
                        f'background: #{bright_background}; border: 1px solid #{bright_entry_border}; border-radius: 1px; border-bottom: 2px solid #{bright_alert};')
                # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                if self.main_self.language == french:
                    self.new_accAliasError.setText('Le nom est déjà pris...')
                elif self.main_self.language == english:
                    self.new_accAliasError.setText('The name is already taken...')
            else:
                exitMessage = QMessageBox()
                exitMessage.setIcon(QMessageBox.Question)
                exitMessage.setWindowIcon(QIcon('resources/pama.ico'))
                if self.main_self.language == french:
                    exitMessage.setWindowTitle('Enregistrer')
                    exitMessage.setText('Voulez-vous vraiment enregistrer les modifications ?')
                    exitMessage.addButton("&Oui", QMessageBox.YesRole)
                    exitMessage.addButton("&Non", QMessageBox.NoRole)
                elif self.main_self.language == english:
                    exitMessage.setWindowTitle('Save')
                    exitMessage.setText('Do you really want to save the changes ?')
                    exitMessage.addButton("&Yes", QMessageBox.YesRole)
                    exitMessage.addButton("&No", QMessageBox.NoRole)
                exitMessage.exec_()
                if exitMessage.clickedButton().text() == '&Yes' or exitMessage.clickedButton().text() == '&Oui':
                    with open('files/password.txt', 'r') as f:
                        file = f.readlines()
                        f.close()
                    file = [convert_bin_txt(i, self.main_self.seed) for i in file]

                    line: int = 0
                    end_line: int = 0

                    for i in range(len(file)):
                        if file[i] == self.accName + '--' or file[i] == self.accName + '::':
                            line = i
                            for j in range(i, len(file)):
                                if ';;' in file[j]:
                                    end_line = j + 1
                                    break
                    for i in range(line, end_line):
                        del file[line]
                    with open('files/password.txt', 'w') as f:
                        [f.write(convert_txt_bin(i, self.main_self.seed) + '\n') for i in file]
                        f.close()
                    with open('files/password.txt', 'a') as f:
                        f.write(convert_txt_bin(new_alias + '--', self.main_self.seed) + '\n')
                        f.write(convert_txt_bin(new_name + '::', self.main_self.seed) + '\n')
                        f.write(convert_txt_bin(new_id + '//', self.main_self.seed) + '\n')
                        f.write(convert_txt_bin(new_email + '%%', self.main_self.seed) + '\n')
                        f.write(convert_txt_bin(new_password + ';;', self.main_self.seed) + '\n')
                        f.close()

                    self.main_self.name_list.remove(self.accName)
                    self.main_self.alias_list.remove(self.accAlias)
                    self.main_self.email_list.remove(self.accEmail)
                    self.main_self.liste.remove([self.accName, self.accAlias, self.accID, self.accEmail, self.accPassword])

                    self.main_self.name_list.append(new_name)
                    self.main_self.alias_list.append(new_alias)
                    self.main_self.email_list.append(new_email)
                    self.main_self.liste.append([new_name, new_alias, new_id, new_email, new_password])

                    ### update
                    self.main_self.data_in_table(self.main_self)
                    self.main_self.search()
                    self.close()
            # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        else:
            self.close()

    def generatePassword(self):
        characters = list(alpha)
        random.seed()
        random.shuffle(characters)
        password_ = ""
        for i in range(30):
            password_ += random.choice(characters)
        if '--' in password_ or '::' in password_ or '//' in password_ or '%%' in password_ or ';;' in password_:
            password_ = ""
            self.generatePassword()
        self.new_accPassword.clear()
        self.new_accPassword.insert(password_)
        QApplication.clipboard().setText(password_)

    def setTheme(self, theme):
        if theme == dark:
            self.background.setStyleSheet(f'background: #{dark_background};')
            ### account name
            self.new_accName_label.setStyleSheet(f'color: #{dark_color}')
            self.new_accName.setStyleSheet(
                f'background: #{dark_background}; color: #{dark_color}; border: 1px solid #{dark_entry_border}; border-radius: 1px;')
            self.new_accNameError.setStyleSheet(f'color: #{dark_alert}')
            ### account alias
            self.new_accAlias_label.setStyleSheet(f'color: #{dark_color}')
            self.new_accAlias.setStyleSheet(
                f'background: #{dark_background}; color: #{dark_color}; border: 1px solid #{dark_entry_border}; border-radius: 1px;')
            self.new_accAliasError.setStyleSheet(f'color: #{dark_alert}')
            ### account id
            self.new_accID_label.setStyleSheet(f'color: #{dark_color}')
            self.new_accID.setStyleSheet(
                f'background: #{dark_background}; color: #{dark_color}; border: 1px solid #{dark_entry_border}; border-radius: 1px;')
            self.new_accIDError.setStyleSheet(f'color: #{dark_alert}')
            ### account email
            self.new_accEmail_label.setStyleSheet(f'color: #{dark_color}')
            self.new_accEmail.setStyleSheet(
                f'background: #{dark_background}; color: #{dark_color}; border: 1px solid #{dark_entry_border}; border-radius: 1px;')
            self.popupAddressesCompleter.setStyleSheet(f'background: #{dark_background}; color: #{dark_color};')
            self.new_accEmailError.setStyleSheet(f'color: #{dark_alert}')
            ### account password
            self.new_accPassword_label.setStyleSheet(f'color: #{dark_color}')
            self.new_accPassword.setStyleSheet(
                f'background: #{dark_background}; color: #{dark_color}; border: 1px solid #{dark_entry_border}; border-radius: 1px;')
            self.new_accPasswordError.setStyleSheet(f'color: #{dark_alert}')
            ### generate password button
            self.generatePassword_Button.setStyleSheet(
                'QPushButton{background: #' + dark_background + '; color: #' + dark_color + '; border: 1px solid #' + dark_border + '; border-radius: 2px;}' +
                'QPushButton:hover{background: #' + dark_background_hover + ';}')
            ### confirm button
            self.confirmButton.setStyleSheet(
                'QPushButton{background: #' + dark_background + '; color: #' + dark_color + '; border: 1px solid #' + dark_border + '; border-radius: 2px;}' +
                'QPushButton:hover{background: #' + dark_background_hover + ';}')

        elif theme == bright:
            self.background.setStyleSheet(f'background: #{bright_background};')
            ### account name
            self.new_accName.setStyleSheet(
                f'background: #{bright_background}; border: 1px solid #{bright_entry_border}; border-radius: 1px;')
            self.new_accNameError.setStyleSheet(f'color: #{bright_alert}')
            ### account alias
            self.new_accAlias.setStyleSheet(
                f'background: #{bright_background}; border: 1px solid #{bright_entry_border}; border-radius: 1px;')
            self.new_accAliasError.setStyleSheet(f'color: #{bright_alert}')
            ### account id
            self.new_accID.setStyleSheet(
                f'background: #{bright_background}; border: 1px solid #{bright_entry_border}; border-radius: 1px;')
            self.new_accIDError.setStyleSheet(f'color: #{bright_alert}')
            ### account email
            self.new_accEmail.setStyleSheet(
                f'background: #{bright_background}; border: 1px solid #{bright_entry_border}; border-radius: 1px;')
            self.popupAddressesCompleter.setStyleSheet(f'background: #{bright_background}; color: #{bright_color};')
            self.new_accEmailError.setStyleSheet(f'color: #{bright_alert}')
            ### account password
            self.new_accPassword.setStyleSheet(
                f'background: #{bright_background}; border: 1px solid #{bright_entry_border}; border-radius: 1px;')
            self.new_accPasswordError.setStyleSheet(f'color: #{bright_alert}')
            ### generate password button
            self.generatePassword_Button.setStyleSheet(
                'QPushButton{background: #' + bright_background + '; border: 1px solid #' + bright_border + '; border-radius: 2px;}' +
                'QPushButton:hover{background: #' + bright_background_hover + ';}')
            ### confirm button
            self.confirmButton.setStyleSheet(
                'QPushButton{background: #' + bright_background + '; border: 1px solid #' + bright_border + '; border-radius: 2px;}' +
                'QPushButton:hover{background: #' + bright_background_hover + ';}')

    def translate(self, language):
        if language == french:
            self.setWindowTitle('Modifier le compte')
            # self.choose_folderLabel.setText('Dossier (facultatif):')
            # self.add_folderButton.setText("Ajouter un dossier")
            self.new_accName_label.setText('Nom du compte:')
            self.new_accAlias_label.setText('Alias (facultatif):')
            self.new_accID_label.setText('Identifiant (facultatif):')
            self.new_accEmail_label.setText('Email (facultatif):')
            self.new_accPassword_label.setText('Mot de passe:')
            self.generatePassword_Button.setText('Générer un mot de passe')
            self.generatePassword_Button.setFixedSize(195, 25)
            self.confirmButton.setText('Sauvegarder')

        elif language == english:
            self.setWindowTitle('Edit the account')
            # self.choose_folderLabel.setText('Folder (optional):')
            # self.add_folderButton.setText("Add a folder")
            self.new_accName_label.setText('Account name:')
            self.new_accAlias_label.setText('Alias (optional):')
            self.new_accID_label.setText('Identifier (optional):')
            self.new_accEmail_label.setText('Email (optional):')
            self.new_accPassword_label.setText('Password:')
            self.generatePassword_Button.setText('Generate a password')
            self.generatePassword_Button.setFixedSize(165, 25)
            self.confirmButton.setText('Save')

    def visible(self):
        if not self.password_isVisible:
            self.new_accPassword.setEchoMode(QLineEdit.Normal)
            if self.main_self.theme == dark:
                self.is_visible.setIcon(QIcon('resources/dark_close_eye.svg'))
            elif self.main_self.theme == bright:
                self.is_visible.setIcon(QIcon('resources/close_eye.svg'))
            self.password_isVisible = True
        else:
            self.new_accPassword.setEchoMode(QLineEdit.Password)
            if self.main_self.theme == dark:
                self.is_visible.setIcon(QIcon('resources/dark_open_eye.svg'))
            elif self.main_self.theme == bright:
                self.is_visible.setIcon(QIcon('resources/open_eye.svg'))
            self.password_isVisible = False

    def keyPressEvent(self, event):
        if event.modifiers() & Qt.ControlModifier:
            if event.key() == Qt.Key_Q:
                self.quit()
            if event.key() == Qt.Key_S:
                self.try_save_accountInformations()
        if event.key() == Qt.Key_Return:
            self.try_save_accountInformations()

    def quit(self):
        if self.new_accName.text().replace(' ', '') != self.accName or self.new_accAlias.text().replace(' ', '') != "".join(self.accAlias) or \
                self.new_accID.text().replace(' ', '') != self.accID or self.new_accEmail.text().replace(' ', '') != self.accEmail or \
                self.new_accPassword.text().replace(' ', '') != self.accPassword:
            exitMessage = QMessageBox()
            exitMessage.setIcon(QMessageBox.Question)
            exitMessage.setWindowIcon(QIcon('resources/pama.ico'))
            if self.main_self.language == french:
                exitMessage.setWindowTitle('Quitter')
                exitMessage.setText('Voulez-vous vraiment fermer la fenêtre ?')
                exitMessage.addButton("&Oui", QMessageBox.YesRole)
                exitMessage.addButton("&Non", QMessageBox.NoRole)
            elif self.main_self.language == english:
                exitMessage.setWindowTitle('Exit')
                exitMessage.setText('Do you really want to close the window ?')
                exitMessage.addButton("&Yes", QMessageBox.YesRole)
                exitMessage.addButton("&No", QMessageBox.NoRole)
            exitMessage.exec_()
            if exitMessage.clickedButton().text() == '&Yes' or exitMessage.clickedButton().text() == '&Oui':
                self.close()
        else:
            self.close()
