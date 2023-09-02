# imports:
from mainH import *


class Window(QMainWindow):

    def __init__(self, application):
        super().__init__()
        self.close_ = None
        GetPassword(self).exec_()
        if not self.close_:
            application.aboutToQuit.connect(lambda: self.close_window(cross=True))

            ## create dictionary
            self.name_list: list[str] = []
            self.liste: list[str] = []
            self.alias_list: list[str] = []
            self.email_list: list[str] = []
            self.items: list[QTreeWidgetItem] = []

            ## ctrl
            self.ctrl = False
            ## load variables
            self.read_txt()
            ## build the window
            self.build()
        else:
            quit()

    def build(self):
        ### Window
        ## set a fixed size to the window
        self.setMinimumSize(710, 400)
        self.resize(self.screen().geometry().width() - 400, self.screen().geometry().height() - 300)
        ## move the window
        self.move((self.screen().geometry().width() - self.width()) // 2,
                  (self.screen().geometry().height() - self.height()) // 2 - 100)
        ## background
        self.background = QFrame(self)
        self.background.resize(self.width(), self.height())
        self.background.move(0, 0)
        ## add an icon to the window
        self.setWindowIcon(QIcon('resources/pama.ico'))

        ### status_bar
        self.status_bar = self.statusBar()
        self.status_bar.setSizeGripEnabled(False)

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
        self.addMenu = self.menuBar().addMenu('Add...')
        # add an account
        self.addAccountButton = QAction(self)
        self.addAccountButton.setShortcut('Ctrl++')
        self.addAccountButton.triggered.connect(self.addAccount)
        self.addMenu.addAction(self.addAccountButton)
        ## helpMenu
        self.helpMenu = self.menuBar().addMenu('Help')
        # helpMenu
        self.helpButton = QAction(self)
        self.helpButton.setShortcut('F1')
        self.helpButton.triggered.connect(self.help)
        self.helpMenu.addAction(self.helpButton)

        ### Search bar
        ## search result
        self.searchResults = QListWidgetClick(self)
        self.searchResults.move(0, 100)
        self.searchResults.resize(200, self.height() - 100)
        self.searchResults.itemClicked.connect(self.searchResultAction)
        ## first background
        self.searchFirstBackground = QFrame(self)
        self.searchFirstBackground.setFixedSize(self.searchResults.width(), 55)
        self.searchFirstBackground.move(self.searchResults.x(),
                                        self.searchResults.y() - self.searchFirstBackground.height())
        ## background
        self.searchBackground = QFrame(self)
        self.searchBackground.resize(180, 36)
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
        self.searchBar.move(40, 60)

        ### QTreeWidget
        ## create tree
        self.tree = QTreeWidgetRight(self, self.items)
        ## resize the tree
        self.tree.resize(self.width() - self.searchResults.width(), self.height() - 50 - self.status_bar.height())
        self.tree.header().setSectionResizeMode(QHeaderView.Fixed)
        self.tree.header().setDragEnabled(False)
        ## move the tree
        self.tree.move(self.searchResults.width(), 50)
        ## set the tree font
        self.tree.setFont(tree_font)
        ## set the Header's size
        self.tree.setColumnWidth(0, self.tree.width() // 100 * 20)
        self.tree.setColumnWidth(1, self.tree.width() // 100 * 20)
        self.tree.setColumnWidth(2, self.tree.width() // 100 * 25)
        self.tree.setColumnWidth(3, self.tree.width() // 100 * 35)
        # connect signals to their methods
        self.tree.itemLeftClicked.connect(self.get_password)
        self.tree.itemRightClicked.connect(self.rightClickAction)
        self.data_in_table(self)

        ### Translate
        self.translate(self.language)

        ### Progress Bar
        self.progress_bar = QProgressBar(self)
        self.status_bar.addPermanentWidget(self.progress_bar)

        ### setTheme
        self.setTheme(self.theme)

        ### credis
        self.credis = QLabel(self)
        self.credis.setFont(QFont('Arial', 7))
        self.credis.setFixedSize(105, 20)
        self.credis.setText('PaMa 2.3 Elie Ruggiero')
        self.credis.move(self.width() - self.credis.width(), self.credis.height())

        ### shortcuts
        self.maj_1 = QShortcut(QKeySequence("Shift+&"), self)
        self.maj_1.activated.connect(self.resetSizes)

        ### display window
        self.show()

        ### Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.update_timer = False

        ### Progress Bar
        self.progress_bar.setFixedSize(230, 30)
        self.progress_bar.setRange(0, self.time)
        self.count = self.time
        self.progress_bar.setFormat(
            str(self.count // 10) + f'    {"" if self.count // 2 > 9 else " "}')  # %p -> pourcentage, %v -> valeur, %m -> nombre d'étapes
        self.progress_bar.setVisible(0)
        self.progress_bar.setAlignment(Qt.AlignHCenter)
        self.status_bar.resize(self.status_bar.width(), self.progress_bar.height() + 2)
        # self.progress_bar.move(self.width() - self.progress_bar.width() - 1, self.height() - self.progress_bar.height() - 1)
        self.resizeEvent(QSize(self.width(), self.height()))

    def resizeEvent(self, event) -> None:
        self.background.resize(self.width(), self.height())
        self.status_bar.resize(self.status_bar.width(), self.progress_bar.height() + 2)
        self.tree.resize(self.width() - self.searchResults.width(), self.height() - 50 - self.status_bar.height())
        if self.tree.verticalScrollBar().isHidden():
            self.tree.setColumnWidth(0, self.tree.width() // 100 * 20)
            self.tree.setColumnWidth(1, self.tree.width() // 100 * 20)
            self.tree.setColumnWidth(2, self.tree.width() // 100 * 25)
            self.tree.setColumnWidth(3, self.tree.width() // 100 * 35)
        else:
            self.tree.setColumnWidth(0, (self.tree.width() - self.tree.verticalScrollBar().widthMM()) // 100 * 20)
            self.tree.setColumnWidth(1, (self.tree.width() - self.tree.verticalScrollBar().widthMM()) // 100 * 20)
            self.tree.setColumnWidth(2, (self.tree.width() - self.tree.verticalScrollBar().widthMM()) // 100 * 25)
            self.tree.setColumnWidth(3, (self.tree.width() - self.tree.verticalScrollBar().widthMM()) // 100 * 35)
        self.credis.move(self.width() - self.credis.width(), self.credis.height())
        self.searchResults.resize(self.searchResults.width(), self.height() - 100)

    def keyPressEvent(self, event: QKeyEvent = None):
        if event.key() == Qt.Key_Control:
            self.ctrl = True

    def resetSizes(self):
        tree_font.setPixelSize(tree_font_default)
        self.tree.setFont(tree_font)

    def keyReleaseEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Control:
            self.ctrl = False

    def wheelEvent(self, event: QWheelEvent):
        if self.ctrl:
            if event.angleDelta().y() > 0:
                if tree_font.pixelSize() <= 80:
                    tree_font.setPixelSize(tree_font.pixelSize() + 2)
                    self.tree.setFont(tree_font)
            else:
                if 12 <= tree_font.pixelSize():
                    tree_font.setPixelSize(tree_font.pixelSize() - 2)
                    self.tree.setFont(tree_font)

    @staticmethod
    def data_in_table(main_self):
        main_self.tree.clear()
        main_self.items.clear()
        for i in range(len(main_self.liste)):
            item = QTreeWidgetItem(main_self.tree)
            item.setText(0, main_self.liste[i][0])
            item.setText(1, main_self.liste[i][1])
            item.setText(2, main_self.liste[i][2])
            item.setText(3, main_self.liste[i][3])
            item.setTextAlignment(4, Qt.AlignCenter)
            main_self.items.append(item)
        main_self.tree.update_items(main_self.items)

    def edit_account(self, index):
        self.ctrl = False
        EditAccount(self, index).exec_()

    def addAccount(self):
        self.ctrl = False
        AddAccount(self).exec_()

    def settings(self):
        self.ctrl = False
        WindowSettings(self).exec_()

    def delete(self, index):
        accountName = self.liste[index][0]
        delete_accountQMessageBox = QMessageBox()
        delete_accountQMessageBox.setIcon(QMessageBox.Question)
        delete_accountQMessageBox.setWindowIcon(QIcon('resources/pama.ico'))
        if self.language == french:
            delete_accountQMessageBox.setWindowTitle('Supprimer')
            delete_accountQMessageBox.setText(f'Voulez-vous vraiment supprimer le compte {accountName}?')
            delete_accountQMessageBox.addButton("&Oui", QMessageBox.YesRole)
            delete_accountQMessageBox.addButton("&Non", QMessageBox.NoRole)
        elif self.language == english:
            delete_accountQMessageBox.setWindowTitle('Delete')
            delete_accountQMessageBox.setText(f'Do you really want to delete the {accountName} account?')
            delete_accountQMessageBox.addButton("&Yes", QMessageBox.YesRole)
            delete_accountQMessageBox.addButton("&No", QMessageBox.NoRole)
        delete_accountQMessageBox.exec_()
        if delete_accountQMessageBox.clickedButton().text() == '&Yes' or delete_accountQMessageBox.clickedButton().text() == '&Oui':
            with open('files/password.txt', 'r') as f:
                file = f.readlines()
                f.close()
            file = [convert_bin_txt(i, self.seed) for i in file]
            for i in range(len(file)):
                if file[i] == accountName + '::' or file[i] == self.liste[index][1] + '--':
                    line = i
                    for j in range(i, len(file)):
                        if ';;' in file[j]:
                            end_line = j + 1
                            break
            for i in range(line, end_line):
                del file[line]
            with open('files/password.txt', 'w') as f:
                [f.write(convert_txt_bin(i, self.seed) + '\n') for i in file]

            # dicos and lists update
            self.name_list.remove(accountName)
            self.alias_list.remove(self.liste[index][1])
            self.email_list.remove(self.liste[index][3])
            self.liste.remove(self.liste[index])
            self.data_in_table(self)
            self.search()

    def rightClickAction(self, index):
        self.rightClickMenu = QMenuClose(self, 5)
        self.rightClickMenu.setAttribute(Qt.WA_TranslucentBackground)
        editMenu = QAction(self)
        editMenu.setFont(menu_font)
        deleteMenu = QAction(self)
        deleteMenu.setFont(menu_font)
        if self.language == french:
            editMenu.setText('Modifier')
            deleteMenu.setText('Supprimer')
        elif self.language == english:
            editMenu.setText('Edit')
            deleteMenu.setText('Delete')
        if self.theme == dark:
            self.rightClickMenu.setStyleSheet(
                'QMenu{background-color: #' + dark_background + '; border-radius: 5px; border: 2px solid #' + dark_border + ';}' +
                'QMenu::item{background-color: transparent; padding:3px 20px; margin:5px 10px; color: #' + dark_color + ';}' +
                'QMenu::item:selected{background-color: #' + dark_background_hover + ';}')
        elif self.theme == bright:
            self.rightClickMenu.setStyleSheet(
                'QMenu{background-color: #' + bright_background + '; border-radius: 5px; border: 1px solid #' + bright_border + ';}' +
                'QMenu::item{background-color: #' + bright_background + '; color: #000000;}' +
                'QMenu::item:selected{background-color: #' + bright_background_hover + ';}')
        editMenu.triggered.connect(lambda: self.edit_account(index))
        self.rightClickMenu.addAction(editMenu)
        deleteMenu.triggered.connect(lambda: self.delete(index))
        self.rightClickMenu.addAction(deleteMenu)
        self.rightClickMenu.popup(QCursor.pos())
        self.rightClickMenu.closeSignal.connect(lambda: self.items[index].setSelected(False))

    def searchResultAction(self, item: QListWidgetItemIndex):
        if item.text() == 'See all' or item.text() == 'Tout voir':
            for i in range(len(self.liste)):
                self.items[i].setHidden(False)
        else:
            for i in range(len(self.liste)):
                self.items[i].setHidden(True)
            self.items[item.getIndex()].setHidden(False)

    def search(self):
        research = self.searchBar.text().lower().replace(' ', '')
        self.searchResults.clear()
        if self.language == french:
            item = QListWidgetItem()
            item.setText('Tout voir')
            item.setFont(QFont('Arial', 15))
            self.searchResults.addItem(item)
        elif self.language == english:
            item = QListWidgetItem()
            item.setText('See all')
            item.setFont(QFont('Arial', 15))
            self.searchResults.addItem(item)
        if research == '':
            for i in range(len(self.liste)):
                item = QListWidgetItemIndex(self)
                item.setText(self.liste[i][0])
                item.setIndex(i)
                self.searchResults.addItem(item)
        else:
            for i in range(len(self.liste)):
                if research in self.liste[i][0] or research in self.liste[i][1]:
                    item = QListWidgetItemIndex(self)
                    item.setText(self.liste[i][0])
                    item.setIndex(i)
                    self.searchResults.addItem(item)

    @staticmethod
    def help():
        popen(r"web_page\index.html")

    def setTheme(self, theme):
        if theme == dark:
            SetTheme(self).dark()
        elif theme == bright:
            SetTheme(self).bright()

    def translate(self, language):
        if language == french:
            Translate(self).french()
        elif language == english:
            Translate(self).english()

    def get_password(self, index):
        self.items[index].setSelected(False)
        if self.update_timer:
            self.updateTimer()
        self.get_password_index = index
        QApplication.clipboard().setText(self.liste[self.get_password_index][4])
        self.count = self.time
        self.timer.start(100)
        self.start = True
        self.progress_bar.setVisible(1)

    def show_time(self):
        if self.start:
            self.count -= 1
            self.progress_bar.setValue(self.count)
            self.progress_bar.setFormat(str(self.count // 10) + f'    {"" if self.count // 2 > 9 else " "}')
            if self.count == 1:
                self.timer.stop()
                self.start = False
                self.progress_bar.setVisible(0)
                if QApplication.clipboard().text() == self.liste[self.get_password_index][4]:
                    QApplication.clipboard().clear()
                if self.update_timer:
                    self.updateTimer()

    def updateTimer(self):
        self.progress_bar.setRange(0, self.time)
        self.update_timer = False

    def read_txt(self):
        with open('files/password.txt', 'r') as f:
            file = []
            for i in f.readlines():
                if i != "":
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

            self.liste.append([name, alias, identifiant, email, password])
            self.name_list.append(name)
            self.alias_list.append(alias)
            self.email_list.append(email)
        # delete list_
        # del list_

    def close_window(self, cross=False):
        if not cross:
            exitMessage = QMessageBox()
            exitMessage.setIcon(QMessageBox.Question)
            exitMessage.setWindowIcon(QIcon('resources/pama.ico'))
            if self.language == french:
                exitMessage.setWindowTitle('Quitter')
                exitMessage.setText('Voulez-vous vraiment fermer la fenêtre ?')
                exitMessage.addButton("&Oui", QMessageBox.YesRole)
                exitMessage.addButton("&Non", QMessageBox.NoRole)
            elif self.language == english:
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


class GetPassword(QDialog):

    def __init__(self, main_self):
        super().__init__()
        self.main_self = main_self
        self.main_self.close_ = True
        ### set language
        self.tried = 0
        ### load variables
        self.load_variables()
        ### create window
        self.build()

    def build(self):
        ### Window
        ## give a size to the window
        self.setMinimumSize(400, 400)
        self.resize(700, 600)
        ## add an icon to the window
        self.setWindowIcon(QIcon('resources/pama.ico'))

        ### label
        self.label = QLabel(self)
        self.label.adjustSize()
        self.label.setFont(QFont('Arial', 9))

        ### password entry
        self.passwordEntry = QLineEdit(self)
        self.passwordEntry.setFocus()
        self.passwordEntry.setFixedSize(200, 30)
        self.passwordEntry.setEchoMode(QLineEdit.Password)
        self.passwordEntry.setStyleSheet(f'border: 1px solid #{bright_border};')
        self.password_isVisible = False
        ## see / not to see
        self.is_visible = QPushButton(self.passwordEntry)
        self.is_visible.setIcon(QIcon('resources/open_eye.svg'))
        self.is_visible.setCursor(Qt.ArrowCursor)
        self.is_visible.setStyleSheet('border: 0px;')
        self.is_visible.clicked.connect(self.visible)
        self.is_visible.move(self.passwordEntry.width() - 30, self.passwordEntry.height() // 4)
        ## alert label
        self.alert = QLabel(self)
        self.alert.setText('')
        self.alert.setFont(QFont('Arial Nova Light', 8))
        self.alert.setFixedWidth(300)
        self.alert.setStyleSheet(f'color: #{bright_alert}')

        ### confirm button
        self.confirmButton = QPushButton(self)
        self.confirmButton.setFixedSize(100, 30)
        self.confirmButton.move((self.width() - self.confirmButton.width()) // 2, 200)
        self.confirmButton.released.connect(lambda: self.check_password())
        ## set the confirmButton shortcut
        self.shortcut = QShortcut(QKeySequence("Return"), self)
        self.shortcut.activated.connect(lambda: self.check_password())

        ### translate
        self.translate(self.language)

        self.valide = True
        if path.isfile('files/password.txt'):
            with open('files/password.txt', 'r') as f:
                file = f.readlines()
                if not file:
                    self.valide = False
                    CreatePassword(self).exec_()
        else:
            open('files/password.txt', 'x').close()
            with open('files/password.txt', 'r') as f:
                file = f.readlines()
                if not file:
                    self.valide = False
                    CreatePassword(self).exec_()

        ### display window
        if self.valide:
            self.show()
            del self.valide
        else:
            quit()

    def resizeEvent(self, event):
        self.label.move((self.width() - self.label.width()) // 2, self.height() // 6)
        self.passwordEntry.move((self.width() - self.passwordEntry.width()) // 2, self.height() // 4)
        self.alert.move(self.passwordEntry.geometry().x(), self.height() // 4 + self.passwordEntry.height())
        self.confirmButton.move((self.width() - self.confirmButton.width()) // 2, int(self.height() // 2.8))

    def load_variables(self):
        try:
            with open('resources/variables.txt', 'rb') as file:
                variables = load(file)
                self.language = variables['language']
                self.time = variables['time']
                self.theme = variables['theme']
                file.close()
        except:
            self.language = english
            self.time = 250
            self.theme = bright
            variables = {'language': self.language, 'time': self.time, 'theme': self.theme}
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
        # put everything back on the right StyleSheet
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
            if self.tried >= 2:
                quit()
            else:
                self.passwordEntry.clear()
                self.passwordEntry.setStyleSheet(f'border-top: 1px solid #{bright_border};'
                                                 f'border-bottom: 2px solid #{bright_alert}; border-right: 1px solid #{bright_border}; border-left: 1px solid #{bright_border};')
                if self.language == french:
                    self.alert.setText("Le mot de passe n'est pas correct")
                elif self.language == english:
                    self.alert.setText("The password is not correct")
            self.tried += 1
        else:
            self.shortcut.deleteLater()
            self.main_self.language = self.language
            self.main_self.time = self.time
            self.main_self.theme = self.theme
            self.main_self.seed = create_seed(passwordEntry)
            self.main_self.close_ = False
            self.close()

    def translate(self, language):
        if language == french:
            self.setWindowTitle('PaMa')
            self.label.setText('Entrer votre mot de passe:')
            self.label.adjustSize()
            self.confirmButton.setText('Confirmer')
        elif language == english:
            self.setWindowTitle('PaMa')
            self.label.setText('Enter your password:')
            self.label.adjustSize()
            self.confirmButton.setText('Confirm')

    def close(self):
        self.deleteLater()


class CreatePassword(QDialog):

    def __init__(self, main_self):
        super().__init__(None, Qt.WindowCloseButtonHint | Qt.WindowTitleHint)
        ### make the window modal
        self.setWindowModality(Qt.ApplicationModal)
        self.main_self = main_self
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
        if language == french:
            self.setWindowTitle('PaMa - Créer le mot de passe')
            self.label.setText('Choisissez un mot de passe pour ce logiciel:')
            self.confirmButton.setText('Confirmer')
        elif language == english:
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
            if self.main_self.language == french:
                self.alert.setText(
                    f"Vous ne pouvez pas utiliser le{'s' if len(errorList) > 1 else ''} caractère{'s' if len(errorList) > 1 else ''} suivant: {''.join(errorList)}")
            elif self.main_self.language == english:
                self.alert.setText(
                    f"You cannot use the following character{'s' if len(errorList) > 1 else ''}: {''.join(errorList)}")
        elif passwordEntry in easy_password or search(r"(\d+([/\-|\\])\d+([/\-|\\])\d+)", passwordEntry) is not None:
            if self.main_self.language == french:
                self.alert.setText("Votre mot de passe est trop facile")
            elif self.main_self.language == english:
                self.alert.setText("Your password is too easy")
        elif len(passwordEntry) <= 4:
            if self.main_self.language == french:
                self.alert.setText("Votre mot de passe doit contenir au moins 5 caractères")
            elif self.main_self.language == english:
                self.alert.setText("Your password must contain at least 5 characters")
        elif search(r'(\d+)', passwordEntry) is None:
            if self.main_self.language == french:
                self.alert.setText("Votre mot de passe doit contenir au moins un chiffre")
            elif self.main_self.language == english:
                self.alert.setText("Your password must contain at least one digit")
        elif search(r'([A-Z])', passwordEntry) is None:
            if self.main_self.language == french:
                self.alert.setText("Votre mot de passe doit contenir au moins une majuscule")
            elif self.main_self.language == english:
                self.alert.setText("Your password must contain at least one capital letter")
        elif search(r'([a-z])', passwordEntry) is None:
            if self.main_self.language == french:
                self.alert.setText("Votre mot de passe doit contenir au moins une minuscule")
            elif self.main_self.language == english:
                self.alert.setText("Your password must contain at least one lower case letter")
        else:
            confirmPassword = QMessageBox()
            confirmPassword.setIcon(QMessageBox.Critical)
            confirmPassword.setWindowIcon(QIcon('resources/pama.ico'))
            if self.main_self.language == french:
                confirmPassword.setWindowTitle('Enregistrer')
                confirmPassword.setText(
                    "Voulez-vous valider votre mot de passe sachant qu'il sera irrécupérable si vous l'oubliez ?")
                confirmPassword.addButton("&Oui", QMessageBox.YesRole)
                confirmPassword.addButton("&Non", QMessageBox.NoRole)
            elif self.main_self.language == english:
                confirmPassword.setWindowTitle('Save')
                confirmPassword.setText(
                    "Do you want to validate your password knowing that it will be unrecoverable if you forget it?")
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
