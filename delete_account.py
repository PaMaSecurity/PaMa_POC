from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from additions import *


def delete(self, index, question=True):
    will_delete = True
    alias_name = self.liste[index][1]
    account_name = self.liste[index][0]

    if question:
        # Message Box asks a confirmation
        delete_account = QMessageBox()
        delete_account.setIcon(QMessageBox.Question)
        delete_account.setWindowIcon(QIcon('resources/pama.ico'))
        if self.language == french:
            delete_account.setWindowTitle('Supprimer')
            delete_account.setText(f'Voulez-vous vraiment supprimer le compte {account_name} ?')
            delete_account.addButton("&Oui", QMessageBox.YesRole)
            delete_account.addButton("&Non", QMessageBox.NoRole)
        elif self.language == english:
            delete_account.setWindowTitle('Delete')
            delete_account.setText(f'Do you really want to delete the {account_name} account?')
            delete_account.addButton("&Yes", QMessageBox.YesRole)
            delete_account.addButton("&No", QMessageBox.NoRole)
        delete_account.exec_()
        will_delete = delete_account.clickedButton().text() == '&Yes' or delete_account.clickedButton().text() == '&Oui'

    # Deletes the account
    if will_delete:
        with open('files/password.txt', 'r') as f:
            file: list = f.readlines()
            f.close()
        file = [convert_bin_txt(i, self.seed) for i in file]

        line: int = 0
        end_line: int = 0

        for i in range(len(file)):
            if file[i] == alias_name + '--':
                line = i
                for j in range(i, len(file)):
                    if ';;' in file[j]:
                        end_line = j + 1
                        break
        print(file)
        for i in range(line, end_line):
            file.pop(line)
        print(file)
        with open('files/password.txt', 'w') as f:
            for i in file:
                f.write(convert_txt_bin(i, self.seed) + '\n')
            f.close()

        # updates dicts and lists
        self.name_list.remove(account_name)
        self.alias_list.remove(self.liste[index][1])
        self.email_list.remove(self.liste[index][3])
        self.liste.remove(self.liste[index])
        self.data_in_table(self)
        self.search()
