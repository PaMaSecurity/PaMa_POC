from PyQt5.QtWidgets import QPushButton, QTreeWidget, QMenu, QListWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSignal, Qt, QRectF
from PyQt5.QtGui import QCloseEvent, QMouseEvent, QPainterPath, QRegion, QTransform


class QPushButtonRight(QPushButton):
    rightClick = pyqtSignal()

    # creation de notre fonction __init__ avec un arg string pour le nom du futur bouton
    def __init__(self, window_):
        # on intègre la classe QPushButton a notre class PushRightButton
        QPushButton.__init__(self, window_)

    # modification de la fonction mousePressEvent
    def mousePressEvent(self, event):
        # on intègre la fonction QPushButton.mousePressEvent(self, event) a notre fonction PushRightButton.mousePressEvent(self, event)
        QPushButton.mousePressEvent(self, event)

        # condition du click droit
        if event.button() == Qt.RightButton:
            # émition du signal rightClick
            self.rightClick.emit()


class QTreeWidgetRight(QTreeWidget):
    itemRightClicked = pyqtSignal(object)
    itemLeftClicked = pyqtSignal(object)

    def __init__(self, window_, items: list):
        QTreeWidget.__init__(self, window_)
        self.items = items

    def mousePressEvent(self, event: QMouseEvent):
        QTreeWidget.mousePressEvent(self, event)
        if event.button() == Qt.RightButton:
            for i in range(self.topLevelItemCount()):
                rect = self.visualItemRect(self.items[i])
                if rect.topLeft().x() <= event.pos().x() <= rect.bottomRight().x() and rect.topLeft().y() <= event.pos().y() <= rect.bottomRight().y():
                    self.itemRightClicked.emit(i)
        elif event.button() == Qt.LeftButton:
            if self.topLevelItemCount() > 0:
                if event.pos().y() > self.visualItemRect(self.items[self.topLevelItemCount() - 1]).bottom():
                    for i in range(self.topLevelItemCount()):
                        if self.items[i].isSelected():
                            self.items[i].setSelected(False)
                            break
                else:
                    for i in range(self.topLevelItemCount()):
                        rect = self.visualItemRect(self.items[i])
                        if rect.topLeft().x() <= event.pos().x() <= rect.bottomRight().x() and rect.topLeft().y() <= event.pos().y() <= rect.bottomRight().y():
                            self.itemLeftClicked.emit(i)

    def update_items(self, items: list):
        self.items = items


class QMenuClose(QMenu):
    closeSignal = pyqtSignal()

    def __init__(self, window_, radius):
        QMenu.__init__(self, window_)
        # https://stackoverflow.com/questions/65574567/rounded-corners-for-qmenu-in-pyqt
        self.radius = int(radius)

    def closeEvent(self, event: QCloseEvent):
        self.closeSignal.emit()
        event.accept()

    def resizeEvent(self, event):
        path = QPainterPath()
        # the rectangle must be translated and adjusted by 1 pixel in order to
        # correctly map the rounded shape
        rect = QRectF(self.rect()).adjusted(.5, .5, -1.5, -1.5)
        path.addRoundedRect(rect, self.radius, self.radius)
        # QRegion is bitmap based, so the returned QPolygonF (which uses float
        # values must be transformed to an integer based QPolygon
        region = QRegion(path.toFillPolygon(QTransform()).toPolygon())
        self.setMask(region)


class QListWidgetClick(QListWidget):
    def __init__(self, window_):
        QListWidget.__init__(self, window_)

    def mousePressEvent(self, event: QMouseEvent):
        QListWidget.mousePressEvent(self, event)
        if event.button() == Qt.LeftButton:
            if event.pos().y() > self.visualItemRect(self.item(self.count() - 1)).bottom():
                for i in range(self.count()):
                    if self.item(i).isSelected():
                        self.item(i).setSelected(False)
                        break


class QListWidgetItemIndex(QListWidgetItem):
    def __init__(self, window_, text=None):
        QListWidgetItem.__init__(self, text)
        self.window = window_
        self.index = None

    def setIndex(self, index):
        self.index = index

    def getIndex(self):
        return self.index