from additions.constants.languages import *


class Translate:

    def __init__(self, main_self):
        self.self = main_self

    def french(self):
        self.self.language = french

        ### give title to the window
        self.self.setWindowTitle('PaMa')
        self.self.fileMenu.setTitle('Fichier')
        self.self.settingsButton.setText('Paramètres')
        self.self.exitButton.setText('Quitter')
        self.self.addMenu.setTitle('Ajouter')
        self.self.addAccountButton.setText('Ajouter un compte')
        self.self.helpMenu.setTitle('Aide')
        self.self.helpButton.setText('Aide en ligne')
        self.self.searchBar.setPlaceholderText('Recherche')
        self.self.tree.setHeaderLabels(['Nom du compte', 'Alias', 'Identifiant', 'Email'])

        ### update window
        self.self.search()

    def english(self):
        self.self.language = english

        ### give title to the window
        self.self.setWindowTitle('PaMa')
        self.self.fileMenu.setTitle('File')
        self.self.settingsButton.setText('Settings')
        self.self.exitButton.setText('Exit')
        self.self.addMenu.setTitle('Add')
        self.self.addAccountButton.setText('Add an account')
        self.self.helpMenu.setTitle('Help')
        self.self.helpButton.setText('Online help')
        self.self.searchBar.setPlaceholderText('Search')
        self.self.tree.setHeaderLabels(['Name', 'Alias', 'Identifier', 'Email'])

        ### update window
        self.self.search()