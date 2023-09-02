# imports:
from mainH import *


class Window(QMainWindow):

    def __init__(self, application):
        super().__init__()
        application.aboutToQuit.connect(lambda: self.close_window(cross=True))
        GetPassword(self)

        ## create dictionary
        self.row_to_name = {}
        self.name_to_row = {}
        self.name_list = []
        self.name_to_alias = {}
        self.name_to_ID = {}
        self.name_to_email = {}
        self.name_to_password = {}

    def build(self):
        ### Window
        ## set a fixed size to the window
        self.setFixedSize(1366, 768)
        ## move the window
        self.move((self.screen().geometry().width() - self.width()) // 2,
                  (self.screen().geometry().height() - self.height()) // 2 - 100)
        ## background
        self.background = QFrame(self)
        self.background.setFixedSize(self.width(), self.height())
        self.background.move(0, 0)

        ### Menu
        ## fileMenu
        self.fileMenu = self.menuBar().addMenu('File')
        # fileMenu/file/settings
        self.settingsButton = QAction(self)
        self.settingsButton.setIcon(QIcon('resources/settings_icon.svg'))
        self.settingsButton.setShortcut('Ctrl+P')
        self.settingsButton.triggered.connect(self.settings)
        self.fileMenu.addAction(self.settingsButton)
        # fileMenu/file/exit
        self.exitButton = QAction(self)
        self.exitButton.setShortcut('Ctrl+Q')
        self.exitButton.triggered.connect(self.close_window)
        self.fileMenu.addAction(self.exitButton)
        ## AddAccountMenu
        self.addAccountMenu = self.menuBar().addMenu('Add an account')
        # add an account
        self.addAccountButton = QAction(self)
        self.addAccountButton.setShortcut('Ctrl++')
        self.addAccountButton.triggered.connect(self.addAccount)
        self.addAccountMenu.addAction(self.addAccountButton)
        ## helpMenu
        self.helpMenu = self.menuBar().addMenu('Help')
        # helpMenu
        self.helpButton = QAction(self)
        self.helpButton.setShortcut('F1')
        self.helpButton.triggered.connect(self.help)
        self.helpMenu.addAction(self.helpButton)

        ### Search bar
        ## search result
        self.searchResults = QListWidget(self)
        self.searchResults.setGeometry(0, 100, 200, self.width() - 51)
        self.searchResults.itemDoubleClicked.connect(self.searchResultAction)
        ## first background
        self.searchFirstBackground = QFrame(self)
        self.searchFirstBackground.setFixedSize(self.searchResults.width(), 55)
        self.searchFirstBackground.move(self.searchResults.x(), self.searchResults.y()-self.searchFirstBackground.height())
        ## background
        self.searchBackground = QFrame(self)
        self.searchBackground.setFixedSize(180, 36)
        self.searchBackground.move(8, 54)
        ## search bar icon
        self.searchBarIcon = QLabel(self)
        searchIcon = QPixmap('resources/search_icon.svg')
        self.searchBarIcon.setPixmap(searchIcon)
        self.searchBarIcon.setGeometry(16, 64, searchIcon.width(), searchIcon.height())
        ## search bar QLineEdit
        self.searchBar = QLineEdit(self)
        self.searchBar.setFixedSize(140, 25)
        self.searchBar.textChanged.connect(self.search)
        self.searchBar.setPlaceholderText('Search')
        self.searchBar.move(40, 60)
        ## show all possibilities
        self.search()

        ### Table
        ## create tables
        self.table = QTableWidget(self)
        ## position
        self.table_move_height = 50
        self.table.move(self.searchResults.width(), self.table_move_height)
        # define the number of columns
        self.table.setColumnCount(6)  # colonne
        # Hide headers
        self.table.horizontalHeader().setVisible(False)
        self.table.verticalHeader().setVisible(False)
        ## add the data to the table
        self.data_in_table(self)
        # set the horizontal scrollbar policy to off
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # remove the modification of widgets/cells
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # remove the Focus Policy
        self.table.setFocusPolicy(0)
        # remove the selection of cells
        self.table.setSelectionMode(0)
        # define the minimum size policy
        self.table.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        # set a fixed size
        self.table.setFont(QFont('Arial', 12))
        ### https://stackoverflow.com/questions/52035966/pyqt-group-cells-in-qtablewidget
        self.table.setColumnWidth(0, 63)   # 0, 63
        self.table.setColumnWidth(1, 190)  # 1, 190
        self.table.setColumnWidth(2, 188)  # 2, 188
        self.table.setColumnWidth(3, 200)  # 3, 200
        self.table.setColumnWidth(4, 335)  # 4, 335
        self.table.setColumnWidth(5, 170)  # 5, 170

        ### Translate
        self.translate(self.language)

        ### setTheme
        self.setTheme(self.theme)

        ### credis
        credis = QLabel(self)
        credis.setFont(QFont('Arial', 7))
        credis.setFixedSize(105, 20)
        credis.setText('PaMa 2.2 Elie Ruggiero')
        credis.move(self.width()-credis.width(), credis.height())

        ### display window
        self.show()

        ### Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_time)

        ### Progress Bar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(self.window().width() - 215, self.window().height() - 30, 230, 30)
        self.progress_bar.setValue(100)
        '''                          en secondes️'''
        self.progress_bar.setFormat('')  # %p -> pourcentage, %v -> valeur, %m -> nombre d'étapes
        self.progress_bar.setVisible(0)

    def edit_account(self, row):
        EditAccount(self, self.row_to_name[row]).exec_()

    def addAccount(self):
        AddAccount(self).exec_()

    def settings(self):
        WindowSettings(self).exec_()

    def delete(self, accountName):
        if self.language == 'french':
            title = 'Supprimer'
            message = f'Voulez-vous vraiment supprimer le compte {accountName}?'
        elif self.language == 'english':
            title = 'Delete'
            message = f'Do you really want to delete the {accountName} account?'
        if QMessageBox.question(self, title, message, QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes) == QMessageBox.Yes:
            with open('files/password.txt', 'r') as f:
                file = f.readlines()
                f.close()
            file = [convert_bin_txt(i, self.seed) for i in file]
            for i in range(len(file)):
                if file[i] == accountName + '::' or file[i] == accountName + '--':
                    line = i
                    for j in range(i, len(file)):
                        if ';;' in file[j]:
                            end_line = j + 1
                            break
            for i in range(line, end_line):
                del file[line]
            with open('files/password.txt', 'w') as f:
                [f.write(convert_txt_bin(i, self.seed)+'\n') for i in file]
            del self.row_to_name[self.name_to_row[accountName]]
            del self.name_to_row[accountName]
            self.name_list.remove(accountName)
            del self.name_to_alias[accountName]
            del self.name_to_ID[accountName]
            del self.name_to_email[accountName]
            del self.name_to_password[accountName]
            self.data_in_table(self)
            self.search()

    def rightClickAction(self, row):
        self.rightClickMenu = QMenu()
        deleteMenu = QAction(self)
        if self.language == 'french':
            deleteMenu.setText('Supprimer')
        elif self.language == 'english':
            deleteMenu.setText('Delete')
        if self.theme == 'dark':
            self.rightClickMenu.setStyleSheet(
                'QMenu{background-color: #' + dark_background + '; border: 1px solid #' + dark_border + '; border-radius: 3px;}'
                'QMenu::item{background-color: #' + dark_background + '; color: #' + dark_color + ';}'
                'QMenu::item:selected{background-color: #' + dark_background_hover + ';}')
        elif self.theme == 'bright':
            self.rightClickMenu.setStyleSheet(
                'QMenu{background-color: #' + bright_background + '; border: 1px solid #' + bright_border + '; border-radius: 3px;}'
                'QMenu::item{background-color: #' + bright_background + '; color: #000000;}'
                'QMenu::item:selected{background-color: #' + bright_background_hover + ';}')
        deleteMenu.triggered.connect(lambda: self.delete(self.row_to_name[row]))
        self.rightClickMenu.addAction(deleteMenu)
        self.rightClickMenu.popup(QCursor.pos())

    def searchResultAction(self, item):
        item = item.text()
        if item == 'See all' or item == 'Tout voir':
            [self.table.showRow(i) for i in range(self.table.rowCount())]
        else:
            try:
                [self.table.showRow(i) for i in range(self.table.rowCount())]
                [self.table.hideRow(i) for i in [j for j in range(self.table.rowCount()) if j != self.name_to_row[item] and j != 0]]
            except:
                for key, value in self.name_to_alias.items():
                    if item == "".join(value):
                        [self.table.showRow(i) for i in range(self.table.rowCount())]
                        [self.table.hideRow(i) for i in [j for j in range(self.table.rowCount()) if j != self.name_to_row[key] and j != 0]]
                        break

    def search(self):
        self.name_list.sort()
        research = self.searchBar.text().lower().replace(' ', '')
        self.searchResults.clear()
        if self.language == 'french':
            seeAll = 'Tout voir'
        elif self.language == 'english':
            seeAll = 'See all'
        self.searchResults.addItem(seeAll)
        self.searchResults.item(0).setFont(QFont("Times", 13))
        keyword = []
        keyword.extend(self.name_list)
        if research == '':
            for i in keyword:
                if research in i.lower():
                    self.searchResults.addItem(i)
        else:
            keyword.extend([''.join(i) for i in self.name_to_alias.values() if i != ['']])
            for i in keyword:
                if research in i.lower():
                    self.searchResults.addItem(i)

    @staticmethod
    def help():
        popen(r"web_page\index.html")

    def setTheme(self, theme):
        if theme == 'dark':
            SetTheme(self).dark()
        elif theme == 'bright':
            SetTheme(self).bright()

    def translate(self, language):
        if language == 'french':
            Translate(self).french()
        elif language == 'english':
            Translate(self).english()

    def get_password(self, row):
        QApplication.clipboard().setText(self.name_to_password[self.row_to_name[row]])
        self.count = self.time
        self.timer.start(100)
        self.start = True
        self.progress_bar.setVisible(1)

    def show_time(self):
        if self.start:
            self.count -= 1
            self.progress_bar.setValue(int(self.count * 100 / self.time))
            if self.count == 1:
                self.timer.stop()
                self.start = False
                self.progress_bar.setVisible(0)
                QApplication.clipboard().clear()

    @staticmethod
    def data_in_table(main_self):
        ### define the number of lines
        main_self.table.clearContents()
        main_self.table.setRowCount(1)  # lignes
        main_self.table.setSpan(0, 0, 1, 2)

        ### naming the columns
        ## account name
        main_self.item_AccountName = QTableWidgetItem()
        main_self.item_AccountName.setText('Account Name')
        main_self.item_AccountName.setFont(QFont('Arial', 15))
        main_self.item_AccountName.setTextAlignment(Qt.AlignHCenter)
        main_self.table.setItem(0, 0, main_self.item_AccountName)
        ## alias
        main_self.item_AccountAlias = QTableWidgetItem()
        main_self.item_AccountAlias.setText('Alias')
        main_self.item_AccountAlias.setFont(QFont('Arial', 15))
        main_self.item_AccountAlias.setTextAlignment(Qt.AlignHCenter)
        main_self.table.setItem(0, 2, main_self.item_AccountAlias)
        ## identifier
        main_self.item_AccountID = QTableWidgetItem()
        main_self.item_AccountID.setText('identifier')
        main_self.item_AccountID.setFont(QFont('Arial', 15))
        main_self.item_AccountID.setTextAlignment(Qt.AlignHCenter)
        main_self.table.setItem(0, 3, main_self.item_AccountID)
        ## email
        main_self.item_AccountEmail = QTableWidgetItem()
        main_self.item_AccountEmail.setText('Email')
        main_self.item_AccountEmail.setFont(QFont('Arial', 15))
        main_self.item_AccountEmail.setTextAlignment(Qt.AlignHCenter)
        main_self.table.setItem(0, 4, main_self.item_AccountEmail)
        ## password
        main_self.item_AccountPassword = QTableWidgetItem()
        main_self.item_AccountPassword.setText('Password')
        main_self.item_AccountPassword.setFont(QFont('Arial', 15))
        main_self.item_AccountPassword.setTextAlignment(Qt.AlignHCenter)
        main_self.table.setItem(0, 5, main_self.item_AccountPassword)

        ### sort name_list in alphabetical order
        main_self.name_list.sort()

        ### fill in the table
        for j in [[None, i, main_self.name_to_alias[i], main_self.name_to_ID[i], main_self.name_to_email[i],
                   main_self.name_to_password[i]] for i in main_self.name_list]:
            row = main_self.table.rowCount()
            main_self.table.setRowCount(row + 1)
            col = 0
            for item in j:
                if col == 0:
                    btn = QPushButtonRight(main_self.table)
                    btn.setText('...')
                    if main_self.language == 'french':
                        btn.setToolTip('Modifier les paramètres du compte')
                    elif main_self.language == 'english':
                        btn.setToolTip('Change account settings')
                    if main_self.theme == 'dark':
                        btn.setStyleSheet('QPushButtonRight{background: #' + dark_background + '; border: 0px; color: #' + dark_color + ';}' +
                                          'QPushButtonRight:hover{background: #' + dark_background_hover + ';}')
                    elif main_self.theme == 'bright':
                        btn.setStyleSheet('QPushButtonRight{background: #' + bright_background + '; border: 0px;}' +
                                          'QPushButtonRight:hover{background: #' + bright_background_hover + ';}')
                    # btn.setFixedSize(25, 25)
                    btn.adjustSize()
                    btn.rightClick.connect(partial(main_self.rightClickAction, row))
                    btn.clicked.connect(partial(main_self.edit_account, row))
                    main_self.table.setCellWidget(row, col, btn)
                elif col != 5:
                    cell = QTableWidgetItem(str(item))
                    main_self.table.setItem(row, col, cell)
                else:
                    btn = QPushButton(main_self.table)
                    btn.setText('********')
                    btn.setFont(QFont('Times', 10))
                    if main_self.theme == 'dark':
                        btn.setStyleSheet('QPushButton{background: #' + dark_background + '; border: 0px; color: #' + dark_color + ';}' +
                                          'QPushButton:hover{background: #' + dark_background_hover + ';}')
                    elif main_self.theme == 'bright':
                        btn.setStyleSheet('QPushButton{background: #' + bright_background + '; border: 0px;}' +
                                          'QPushButton:hover{background: #' + bright_background_hover + ';}')
                    btn.pressed.connect(partial(main_self.get_password, row))
                    main_self.row_to_name[row] = j[1]
                    main_self.name_to_row[j[1]] = row
                    main_self.table.setCellWidget(row, col, btn)
                col += 1

        ### fix the size of the table
        if (
                main_self.table.verticalHeader().length() + main_self.table.horizontalHeader().height() + 2) + main_self.table_move_height >= main_self.height():
            main_self.table.setFixedSize(main_self.width() - main_self.searchResults.width(),
                                         main_self.height() - main_self.table_move_height)
        else:
            main_self.table.setFixedSize(main_self.width() - main_self.searchResults.width() - 20,
                                         main_self.table.verticalHeader().length() + 2)

    def read_txt(self):
        with open('files/password.txt', 'r') as f:
            file = []
            for i in f.readlines():
                file.append(convert_bin_txt(i, self.seed))
        f = "".join(file[1:]).replace('\n', '').split(';;')[:-1]

        for i in f:
            element = i.split('::')
            name = element[0]
            alias = name.split('--')
            name = alias[0]
            try:
                alias = alias[1]
            except:
                alias = ''
            element = element[1].split("//")
            identifiant = element[0]
            element = element[1].split('%%')
            email = element[0]
            password = element[1]

            self.name_list.append(name)
            self.name_to_alias[name] = alias
            self.name_to_ID[name] = identifiant
            self.name_to_email[name] = email
            self.name_to_password[name] = password

    def close_window(self, cross=False):
        if not cross:
            exitMessage = QMessageBox()
            exitMessage.setIcon(QMessageBox.Question)
            exitMessage.setWindowIcon(QIcon('resources/pama.ico'))
            if self.language == 'french':
                exitMessage.setWindowTitle('Quitter')
                exitMessage.setText('Voulez-vous vraiment fermer la fenêtre ?')
                exitMessage.addButton("&Oui", QMessageBox.YesRole)
                exitMessage.addButton("&Non", QMessageBox.NoRole)
            elif self.language == 'english':
                exitMessage.setWindowTitle('Exit')
                exitMessage.setText('Do you really want to close the window ?')
                exitMessage.addButton("&Yes", QMessageBox.YesRole)
                exitMessage.addButton("&No", QMessageBox.NoRole)
            exitMessage.exec_()
            if exitMessage.clickedButton().text() == '&Yes' or exitMessage.clickedButton().text() == '&Oui':
                self.hide()
                variables = {'language': self.language, 'time': self.time, 'theme': self.theme}
                file = open('resources/variables.txt', "wb")
                dump(variables, file)
                file.close()
                self.close()
                quit()
        else:
            self.hide()
            variables = {'language': self.language, 'time': self.time, 'theme': self.theme}
            file = open('resources/variables.txt', "wb")
            dump(variables, file)
            file.close()
            self.close()
            quit()


class GetPassword:

    def __init__(self, main_self):
        self.self = main_self
        ### set language
        self.tried = 0
        ### load variables
        self.load_variables()
        ### create window
        self.build()

    def build(self):
        ### Window
        ## give a size to the window
        self.self.setFixedSize(700, 600)
        ## add an icon to the window
        self.self.setWindowIcon(QIcon('resources/pama.ico'))

        ### label
        self.label = QLabel(self.self)
        self.label.setFixedSize(175, 25)
        self.label.move((self.self.width() - self.label.width())//2, 100)
        self.label.setFont(QFont('Arial', 9))

        ### password entry
        self.passwordEntry = QLineEdit(self.self)
        self.passwordEntry.setFocus()
        self.passwordEntry.setFixedSize(200, 30)
        self.passwordEntry.move((self.self.width() - self.passwordEntry.width())//2, 150)
        self.passwordEntry.setEchoMode(QLineEdit.Password)
        self.passwordEntry.setStyleSheet(f'border: 1px solid #{bright_border};')
        self.password_isVisible = False
        ## see / not to see
        self.is_visible = QPushButton(self.passwordEntry)
        self.is_visible.setIcon(QIcon('resources/open_eye.svg'))
        self.is_visible.setCursor(Qt.ArrowCursor)
        self.is_visible.setStyleSheet('border: 0px;')
        self.is_visible.clicked.connect(self.visible)
        self.is_visible.move(self.passwordEntry.width() - 30, self.passwordEntry.height()//4)
        ## alert label
        self.alert = QLabel(self.self)
        self.alert.setText('')
        self.alert.setFont(QFont('Arial Nova Light', 8))
        self.alert.setFixedWidth(300)
        self.alert.setStyleSheet(f'color: #{bright_alert}')
        self.alert.move(self.passwordEntry.geometry().x(), self.passwordEntry.geometry().y() + 23)

        ### confirm button
        self.confirmButton = QPushButton(self.self)
        self.confirmButton.setFixedSize(100, 30)
        self.confirmButton.move((self.self.width() - self.confirmButton.width())//2, 200)
        self.confirmButton.released.connect(lambda: self.check_password())
        ## set the confirmButton shortcut
        self.shortcut = QShortcut(QKeySequence("Return"), self.self)
        self.shortcut.activated.connect(lambda: self.check_password())

        ### translate
        self.translate(self.self.language)

        self.self.valide = True
        try:
            with open('files/password.txt', 'r') as f:
                file = f.readlines()
                if not file:
                    self.self.valide = False
                    CreatePassword(self).exec_()
        except:
            open('files/password.txt', 'x').close()
            with open('files/password.txt', 'r') as f:
                file = f.readlines()
                if not file:
                    self.self.valide = False
                    CreatePassword(self).exec_()

        ### display window
        if self.self.valide:
            self.self.show()
            del self.self.valide
        else:
            quit()

    def load_variables(self):
        try:
            with open('resources/variables.txt', 'rb') as file:
                variables = load(file)
                self.self.language = variables['language']
                self.self.time = variables['time']
                self.self.time = 250
                self.self.theme = variables['theme']
                file.close()
        except:
            self.self.language = 'english'
            self.self.time = 250
            self.self.theme = 'bright'
            variables = {'language': self.self.language, 'time': self.self.time, 'theme': self.self.theme}
            file = open('resources/variables.txt', "wb")
            dump(variables, file)
            file.close()

    def visible(self):
        if not self.password_isVisible:
            self.passwordEntry.setEchoMode(QLineEdit.Normal)
            self.is_visible.setIcon(QIcon('resources/close_eye.svg'))
            self.password_isVisible = True
        else:
            self.passwordEntry.setEchoMode(QLineEdit.Password)
            self.is_visible.setIcon(QIcon('resources/open_eye.svg'))
            self.password_isVisible = False

    def check_password(self):
        self.passwordEntry.setStyleSheet(f'border: 1px solid #{bright_border};')
        passwordEntry = self.passwordEntry.text().replace(' ', '')
        run = True
        with open('files/password.txt', 'r') as f:
            file = f.readlines()
            try:
                password = convert_bin_txt(file[0], create_seed(passwordEntry))
            except:
                password = 'None'
                run = False
            f.close()
        if hashlib.sha3_512(passwordEntry.encode()).hexdigest() != password or run == False:
            if self.tried >= 3:
                quit()
            else:
                self.passwordEntry.clear()
                self.passwordEntry.setStyleSheet(f'border-top: 1px solid #{bright_border};'
                                                 f'border-bottom: 2px solid #{bright_alert}; border-right: 1px solid #{bright_border}; border-left: 1px solid #{bright_border};')
                if self.self.language == 'french':
                    self.alert.setText("Le mot de passe n'est pas correct")
                elif self.self.language == 'english':
                    self.alert.setText("The password is not correct")
            self.tried += 1
        else:
            seed = create_seed(passwordEntry)
            self.Window__init__(seed)

    def translate(self, language):
        if language == 'french':
            self.self.setWindowTitle('PaMa')
            self.label.setText('Entrer votre mot de passe:')
            self.confirmButton.setText('Confirmer')
        elif language == 'english':
            self.self.setWindowTitle('PaMa')
            self.label.setText('Enter your password:')
            self.confirmButton.setText('Confirm')

    def Window__init__(self, seed):
        self.self.seed = seed
        ## hide the window
        self.self.hide()
        self.label.deleteLater()
        self.passwordEntry.deleteLater()
        self.confirmButton.deleteLater()
        self.alert.deleteLater()

        ### create/fill in variables
        ## load variables
        self.self.read_txt()

        ### build window
        self.self.build()


class CreatePassword(QDialog):

    def __init__(self, main_self):
        super().__init__(None, Qt.WindowCloseButtonHint | Qt.WindowTitleHint)
        ### make the window modal
        self.setWindowModality(Qt.ApplicationModal)
        self.main_self = main_self.self
        self.build()

    def build(self):
        self.setFixedSize(500, 500)
        self.setWindowIcon(QIcon('resources/pama.ico'))

        ### label
        self.label = QLabel(self)
        self.label.setFixedSize(247, 25)
        self.label.move((self.width() - self.label.width()) // 2, 100)
        self.label.setFont(QFont('Arial', 9))

        ### password entry
        self.new_password = QLineEdit(self)
        self.new_password.setFocus()
        self.new_password.setFixedSize(200, 30)
        self.new_password.move((self.width() - self.new_password.width()) // 2, 150)
        self.new_password.setEchoMode(QLineEdit.Password)
        self.new_password.setStyleSheet(f'border: 1px solid #{bright_border};')
        self.password_isVisible = False
        ## see / not to see
        self.is_visible = QPushButton(self.new_password)
        self.is_visible.setIcon(QIcon('resources/open_eye.svg'))
        self.is_visible.setCursor(Qt.ArrowCursor)
        self.is_visible.setStyleSheet('border: 0px;')
        self.is_visible.clicked.connect(self.visible)
        self.is_visible.move(self.new_password.width() - 30, self.new_password.height() // 4)
        ## alert label
        self.alert = QLabel(self)
        self.alert.setText('')
        self.alert.setFont(QFont('Arial Nova Light', 8))
        self.alert.setFixedWidth(300)
        self.alert.setStyleSheet(f'color: #{bright_alert}')
        self.alert.move(self.new_password.geometry().x(), self.new_password.geometry().y() + 32)

        ### confirm button
        self.confirmButton = QPushButton(self)
        self.confirmButton.setFixedSize(100, 30)
        self.confirmButton.move((self.width() - self.confirmButton.width()) // 2, 200)
        self.confirmButton.released.connect(lambda: self.save())
        ## set the confirmButton shortcut
        self.shortcut = QShortcut(QKeySequence("Return"), self)
        self.shortcut.activated.connect(lambda: self.save())

        ### translate
        self.translate(self.main_self.language)

    def translate(self, language):
        if language == 'french':
            self.setWindowTitle('PaMa - Créer le mot de passe')
            self.label.setText('Choisissez un mot de passe pour ce logiciel:')
            self.confirmButton.setText('Confirmer')
        elif language == 'english':
            self.setWindowTitle('PaMa - Create password')
            self.label.setText('Choose a password for this software:')
            self.confirmButton.setText('Confirm')

    def visible(self):
        if not self.password_isVisible:
            self.new_password.setEchoMode(QLineEdit.Normal)
            self.is_visible.setIcon(QIcon('resources/close_eye.svg'))
            self.password_isVisible = True
        else:
            self.new_password.setEchoMode(QLineEdit.Password)
            self.is_visible.setIcon(QIcon('resources/open_eye.svg'))
            self.password_isVisible = False

    def save(self):
        passwordEntry = self.new_password.text().replace(' ', '')
        errorList = list(set(i for i in passwordEntry if not i in alpha))

        if errorList:
            self.new_password.setStyleSheet(f'border-top: 1px solid #{bright_border};'
                                             f'border-bottom: 2px solid #{bright_alert}; border-right: 1px solid #{bright_border}; border-left: 1px solid #{bright_border};')
            if self.main_self.language == 'french':
                self.alert.setText(f"Vous ne pouvez pas utiliser le{'s' if len(errorList) > 1 else ''} caractère{'s' if len(errorList) > 1 else ''} suivant: {''.join(errorList)}")
            elif self.main_self.language == 'english':
                self.alert.setText(f"You cannot use the following character{'s' if len(errorList) > 1 else ''}: {''.join(errorList)}")
        elif passwordEntry in easy_password or search(r'(\d+([/\-|\\])\d+([/\-|\\])\d+)', passwordEntry) is not None:
            if self.main_self.language == 'french':
                self.alert.setText("Votre mot de passe est trop facile")
            elif self.main_self.language == 'english':
                self.alert.setText("Your password is too easy")
        elif len(passwordEntry) <= 4:
            if self.main_self.language == 'french':
                self.alert.setText("Votre mot de passe doit contenir au moins 5 caractères")
            elif self.main_self.language == 'english':
                self.alert.setText("Your password must contain at least 5 characters")
        elif search(r'(\d+)', passwordEntry) is None:
            if self.main_self.language == 'french':
                self.alert.setText("Votre mot de passe doit contenir au moins un chiffre")
            elif self.main_self.language == 'english':
                self.alert.setText("Your password must contain at least one digit")
        elif search(r'([A-Z])', passwordEntry) is None:
            if self.main_self.language == 'french':
                self.alert.setText("Votre mot de passe doit contenir au moins une majuscule")
            elif self.main_self.language == 'english':
                self.alert.setText("Your password must contain at least one capital letter")
        elif search(r'([a-z])', passwordEntry) is None:
            if self.main_self.language == 'french':
                self.alert.setText("Votre mot de passe doit contenir au moins une minuscule")
            elif self.main_self.language == 'english':
                self.alert.setText("Your password must contain at least one lower case letter")
        else:
            confirmPassword = QMessageBox()
            confirmPassword.setIcon(QMessageBox.Critical)
            confirmPassword.setWindowIcon(QIcon('resources/pama.ico'))
            if self.main_self.language == 'french':
                confirmPassword.setWindowTitle('Enregistrer')
                confirmPassword.setText("Voulez-vous valider votre mot de passe sachant qu'il sera irrécupérable si vous l'oubliez ?")
                confirmPassword.addButton("&Oui", QMessageBox.YesRole)
                confirmPassword.addButton("&Non", QMessageBox.NoRole)
            elif self.main_self.language == 'english':
                confirmPassword.setWindowTitle('Save')
                confirmPassword.setText("Do you want to validate your password knowing that it will be unrecoverable if you forget it?")
                confirmPassword.addButton("&Yes", QMessageBox.YesRole)
                confirmPassword.addButton("&No", QMessageBox.NoRole)
            confirmPassword.exec_()
            if confirmPassword.clickedButton().text() == '&Yes' or confirmPassword.clickedButton().text() == '&Oui':
                self.main_self.valide = True
                self.password = hashlib.sha3_512(passwordEntry.encode()).hexdigest()
                passwordEntry = convert_txt_bin(self.password, create_seed(passwordEntry))
                with open('files/password.txt', 'w') as f:
                    f.write(passwordEntry + '\n')
                self.close()


if __name__ == '__main__':
    app = QApplication(sys_argv)
    my_window = Window(app)
    app.exec_()  # sys_exit(app.exec_()) / app.exec_()