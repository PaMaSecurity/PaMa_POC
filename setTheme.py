from additions import dark, bright, \
    bright_entry_border, bright_alert, dark_selection_background, dark_selection_color, bright_border, bright_background_entry, bright_background_hover, bright_background, bright_color, \
    dark_alert, dark_entry_border, dark_border, dark_color_entry, dark_background_entry, dark_background_hover, dark_background, dark_color


class SetTheme:

    def __init__(self, main_self):
        self.self = main_self

    def dark(self):
        self.self.theme = dark
        self.self.background.setStyleSheet(
            f'background: #{dark_background};')
        self.self.searchBackground.setStyleSheet(
            f'color: #{dark_color_entry}; background: #{dark_background_entry}; border-radius: 4px;')
        self.self.searchBar.setStyleSheet(
            f'color: #{dark_color_entry}; background: #{dark_background_entry}; border: 0px; selection-background-color: #{dark_selection_background}; selection-color: #{dark_selection_color};')
        self.self.searchResults.setStyleSheet(
            f'color: #{dark_color}; background: #{dark_background}; border-top: 0px solid #{dark_border};'
            f'border-bottom: 0px solid #{dark_border}; border-right: 1px solid #{dark_border}; border-left: 0px solid #{dark_border};')
        self.self.searchFirstBackground.setStyleSheet(
            f'color: #{dark_color}; background: #{dark_background}; border-top: 1px solid #{dark_border};'
            f'border-bottom: 0px solid #{dark_border}; border-right: 1px solid #{dark_border}; border-left: 0px solid #{dark_border};')
        self.self.table.setStyleSheet(
            f'color: #{dark_color}; background: #{dark_background}; border: 0px; gridline-color: #{dark_border};')
        self.self.progress_bar.setStyleSheet(
            'QProgressBar {border: 1px solid #' + dark_border + '; border-radius: 4px; text-align: center; background-color: #' + dark_background + '; color: #' + dark_color + '} QProgressBar::chunk{background-color: #1060B4; width: 1px;}')

    def bright(self):
        self.self.theme = bright
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
        self.self.progress_bar.setStyleSheet(
            'QProgressBar {border: 1px solid #' + bright_border + '; border-radius: 4px; text-align: center; background-color: #' + bright_background + '; color: #' + bright_color + '} QProgressBar::chunk{background-color: #79D53B; width: 1px;}')