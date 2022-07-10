from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QPoint


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.default_font = {
            'family': 'Arial',
            'size': 100,
            'transparency': 1,
            'color': 'white'
        }

        self.initUI()

        self.press = False
        self.last_pos = QPoint(0, 0)

# Настройки прозрачности окна и т. п......................................# Настройки прозрачности окна и т. п.
        self.setAttribute(Qt.WA_TranslucentBackground, True) 
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.setWindowFlags(
            QtCore.Qt.Window
            | QtCore.Qt.CustomizeWindowHint
            | QtCore.Qt.FramelessWindowHint
            | QtCore.Qt.Tool
        )

    def reload(self, data):
        pass

    def initUI(self):
        self.label = QtWidgets.QLabel()
        self.label2 = QtWidgets.QLabel()
        
        self.label.setText('Hell')  # Изменить текст
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.label.setWordWrap(False)

        self.label2.setAutoFillBackground(False)
        self.label2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
        self.label2.setWordWrap(False)

        self.layout = QtWidgets.QVBoxLayout()

        self.layout.addWidget(self.label, 0, Qt.AlignBottom)
        self.layout.addWidget(self.label2, 0, Qt.AlignTop)

        self.setLayout(self.layout)

# Перетаскивание окна за виджеты .................................................. # Перетаскивание окна за виджеты
    def mouseMoveEvent(self, event):
        if self.press:
            self.move(event.globalPos() - self.last_pos)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.press = True

        self.last_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.press = False

# Контекстное меню .................................................................. Контекстное меню
    def contextMenuEvent(self, event: QtGui.QContextMenuEvent) -> None:
        pass


