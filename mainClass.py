import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QPoint


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.default_font = {
            'family': 'Arial',
            'size': 150,
            'transparency': 1,
            'color': 'white'
        }

        self.initUI()

        self.reload(self.default_font)

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
        self.label.setFont(QtGui.QFont(data['family'], data['size']))  # Изменить шрифт
        self.label.setStyleSheet(f"color: rgba(255, 255, 255, {data['transparency']});")  # Цвет и прозрачность



    def initUI(self):
        self.label = QtWidgets.QLabel()
        
        self.label.setText('Helllo')  # Изменить текст
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label)
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
        context_menu = QtWidgets.QMenu(self)

        settings_menu = QtWidgets.QMenu(context_menu)

        hide_action = context_menu.addAction('Скрыть')
        settings_action = context_menu.addAction('Настройки')
        quit_action = context_menu.addAction('Закрыть')

        action = context_menu.exec_(self.mapToGlobal(event.pos()))

        if action == quit_action:
            sys.exit(self.close())
        elif action == hide_action:
            self.hide()
        elif action == settings_action:
            pass