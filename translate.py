class Translate:

    def __init__(self, main_self):
        self.self = main_self

    def french(self):
        self.self.language = 'french'

        ### give title to the window
        self.self.setWindowTitle('Gestionnaire de mots de passe')
        self.self.fileMenu.setTitle('Fichier')
        self.self.settingsButton.setText('Paramètres')
        self.self.exitButton.setText('Quitter')
        self.self.addAccountMenu.setTitle('Ajouter un compte')
        self.self.addAccountButton.setText('Ajouter un compte')
        self.self.helpMenu.setTitle('Aide')
        self.self.helpButton.setText('Aide en ligne')
        self.self.searchBar.setPlaceholderText('Recherche')
        self.self.item_AccountName.setText('Nom du compte')
        self.self.item_AccountAlias.setText('Alias')
        self.self.item_AccountID.setText('Identifiant')
        self.self.item_AccountEmail.setText('Email')
        self.self.item_AccountPassword.setText('Mot de passe')

        ### update window
        self.self.search()

    def english(self):
        self.self.language = 'english'

        ### give title to the window
        self.self.setWindowTitle('Password Manager')
        self.self.fileMenu.setTitle('File')
        self.self.settingsButton.setText('Settings')
        self.self.exitButton.setText('Exit')
        self.self.addAccountMenu.setTitle('Add an account')
        self.self.addAccountButton.setText('Add an account')
        self.self.helpMenu.setTitle('Help')
        self.self.helpButton.setText('Online help')
        self.self.searchBar.setPlaceholderText('Search')
        self.self.item_AccountName.setText('Account name')
        self.self.item_AccountAlias.setText('Alias')
        self.self.item_AccountID.setText('Identifier')
        self.self.item_AccountEmail.setText('Email')
        self.self.item_AccountPassword.setText('Password')

        ### update window
        self.self.search()
