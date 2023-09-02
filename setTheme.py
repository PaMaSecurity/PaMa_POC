# variables:
dark_color = 'CFCFCF'
dark_background = '3D3D3D'
dark_background_entry = '868686'
dark_color_entry = '000000'
dark_border = '777777'
dark_entry_border = 'B6B6B6'
dark_alert = 'FF4040'

bright_background = 'F5F5F5'
bright_background_entry = 'D6D6D6'
bright_border = '1F1F1F'
selection_color = '7678FF'
bright_alert = 'FF0000'
bright_entry_border = '000000'


class SetTheme:

    def __init__(self, main_self):
        self.self = main_self

    def dark(self):
        self.self.theme = 'dark'
        self.self.background.setStyleSheet(
            f'background: #{dark_background};')
        self.self.searchBackground.setStyleSheet(
            f'color: #{dark_color_entry}; background: #{dark_background_entry}; border-radius: 4px;')
        self.self.searchBar.setStyleSheet(
            f'color: #{dark_color_entry}; background: #{dark_background_entry}; border: 0px; selection-background-color: #{selection_color}; selection-color: #000000;')
        self.self.searchResults.setStyleSheet(
            f'color: #{dark_color}; background: #{dark_background}; border-top: 0px solid #{dark_border};'
            f'border-bottom: 0px solid #{dark_border}; border-right: 1px solid #{dark_border}; border-left: 0px solid #{dark_border};')
        self.self.searchFirstBackground.setStyleSheet(
            f'color: #{dark_color}; background: #{dark_background}; border-top: 1px solid #{dark_border};'
            f'border-bottom: 0px solid #{dark_border}; border-right: 1px solid #{dark_border}; border-left: 0px solid #{dark_border};')
        self.self.table.setStyleSheet(
            f'color: #{dark_color}; background: #{dark_background}; border: 0px; gridline-color: #{dark_border};')

    def bright(self):
        self.self.theme = 'bright'
        self.self.background.setStyleSheet(
            f'background: #{bright_background};')
        self.self.searchBackground.setStyleSheet(
            f'background: #{bright_background_entry}; border-radius: 4px;')
        self.self.searchBar.setStyleSheet(
            f'background: #{bright_background_entry}; border: 0px;')
        self.self.searchResults.setStyleSheet(
            f'background: #{bright_background}; border-top: 0px solid #{bright_border}; border-bottom: 0px solid #{bright_border};'
            f'border-right: 1px solid #{bright_border}; border-left: 0px solid #{bright_border};')
        self.self.searchFirstBackground.setStyleSheet(
            f'background: #{bright_background}; border-top: 1px solid #{bright_border}; border-bottom: 0px solid #{bright_border};'
            f'border-right: 1px solid #{bright_border}; border-left: 0px solid #{bright_border};')
        self.self.table.setStyleSheet(
            f'background: #{bright_background}; border: 0px; gridline-color: #{bright_border};')