from additions.constants.themes import *


class SetTheme:

    def __init__(self, main_self):
        self.self = main_self

    def dark(self):
        self.self.theme = dark
        ### https://youtu.be/ttBjf4bMDXY
        self.self.tree.setStyleSheet("""/* VERTICAL SCROLLBAR */
                                QScrollBar:vertical {
                                   border: none;
                                   background: #3D3D3D;
                                   width: 14px;
                                   margin: 15px 0 15px 0;
                                   border-radius: 0px;
                                }
                                /*  HANDLE BAR VERTICAL */
                                QScrollBar::handle:vertical {    
                                    background-color: rgb(80, 80, 122);
                                    min-height: 30px;
                                    width: 5px;
                                    border-radius: 7px;
                                }
                                QScrollBar::handle:vertical:hover{    
                                    background-color: rgb(255, 0, 127);
                                    width: 10px;
                                }
                                /* BTN TOP - SCROLLBAR */
                                QScrollBar::sub-line:vertical {
                                    border: none;
                                    background-color: #F5F5F5;
                                    height: 15px;
                                    border-top-left-radius: 7px;
                                    border-top-right-radius: 7px;
                                    subcontrol-position: top;
                                    subcontrol-origin: margin;
                                }
                                QScrollBar::sub-line:vertical:hover {    
                                    background-color: rgb(255, 0, 127);
                                }
                                QScrollBar::sub-line:vertical:pressed {    
                                    background-color: rgb(185, 0, 92);
                                }
                                /* BTN BOTTOM - SCROLLBAR */
                                QScrollBar::add-line:vertical {
                                    border: none;
                                    background-color: #F5F5F5;
                                    height: 15px;
                                    border-bottom-left-radius: 7px;
                                    border-bottom-right-radius: 7px;
                                    subcontrol-position: bottom;
                                    subcontrol-origin: margin;
                                }
                                QScrollBar::add-line:vertical:hover {    
                                    background-color: rgb(255, 0, 127);
                                }
                                QScrollBar::add-line:vertical:pressed {    
                                    background-color: rgb(185, 0, 92);
                                }
                                /* RESET ARROW */
                                QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                                    background: none;
                                }
                                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                                    background: none;
                                }""")
        self.self.background.setStyleSheet(
            f'background: #{dark_background};')
        self.self.searchBackground.setStyleSheet(
            f'color: #{dark_color_entry}; background: #{dark_background_entry}; border-radius: 4px;')
        self.self.searchBar.setStyleSheet(
            f'color: #{dark_color_entry}; background: #{dark_background_entry}; border: 0px; selection-background-color: #{dark_selection_background}; selection-color: #{dark_selection_color};')
        self.self.searchResults.setStyleSheet(
            "QListWidget {" + f'color: #{dark_color}; background: #{dark_background}; border-top: 0px solid #{dark_border};'
            f'border-bottom: 0px solid #{dark_border}; border-right: 1px solid #{dark_border}; border-left: 0px solid #{dark_border};' + " }")
        self.self.searchFirstBackground.setStyleSheet(
            f'color: #{dark_color}; background: #{dark_background}; border-top: 1px solid #{dark_border};'
            f'border-bottom: 0px solid #{dark_border}; border-right: 1px solid #{dark_border}; border-left: 0px solid #{dark_border};')
        self.self.progress_bar.setStyleSheet(
            'QProgressBar {border: 1px solid #' + dark_border + '; border-radius: 4px; text-align: center; background-color: #' + dark_background + '; color: #' + dark_color + '} QProgressBar::chunk{background-color: #1060B4; width: 1px;}')
        self.self.tree.setStyleSheet(
            "QTreeWidget{ " + f'background: #{dark_background}; color: #{dark_color}; border: 0px;' + " }")
        self.self.tree.header().setStyleSheet(
            "QHeaderView::section { " + f'font: 24px; color: #{dark_color}; background-color: #{dark_background}; border: 1px solid #{dark_background}; border-right: 1px solid #{dark_border};' + " }" +
            "QHeaderView{ border: 0px solid; }")
        self.self.status_bar.setStyleSheet("QStatusBar::item { " + f"border: 0px; " + " }")

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
        self.self.progress_bar.setStyleSheet(
            'QProgressBar {border: 1px solid #' + bright_border + '; border-radius: 4px; text-align: center; background-color: #' + bright_background + '; color: #' + bright_color + '} QProgressBar::chunk{background-color: #79D53B; width: 1px;}')
        self.self.tree.setStyleSheet(
            "QTreeWidget{ " + f'background: #{bright_background}; color: #{bright_color}; border: 0px; font: 16px;' + " }")
        self.self.tree.header().setStyleSheet(
            "QHeaderView::section { " + f'font: 16px; color: #{bright_color}; background-color: #{bright_background}; border: 1px solid #{bright_background}; border-right: 1px solid #{bright_border};' + " }" +
            "QHeaderView{ border: 0px solid; }")
        self.self.status_bar.setStyleSheet("QStatusBar::item { " + f"border: 0px; " + " }")
