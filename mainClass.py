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
        self.hide_show_flsg = 1
        self.initUI()

        self.setFontStyle(self.default_font)

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
        # .........................................................................# Настройки прозрачности окна и т. п.

        # Инициализируем иконку в Трее ............................................Инициализируем иконку в Трее
        self.tray_icon = QtWidgets.QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_DesktopIcon))
        
        # ..... Меню иконки в Трее........................
        quit_action = QtWidgets.QAction('Закрыть',self)
        quit_action.triggered.connect(app.quit)
                
        tray_menu = QtWidgets.QMenu()
        # tray_menu.addSeparator()
        tray_menu.addAction(quit_action)
        
        self.tray_icon.setContextMenu(tray_menu)

        self.tray_icon.show()
        self.tray_icon.activated.connect(self.systemIcon)
        # .........................................................................Инициализируем иконку в Трее
    def setFontStyle(self, data):
        self.label.setFont(QtGui.QFont(data['family'], data['size']))  # Изменить шрифт
        self.label.setStyleSheet(f"color: rgba(255, 255, 255, {data['transparency']});")  # Цвет и прозрачность

    def systemIcon(self, reason): # ............................Свернуть/развернуть по клику в системном трее
        if reason == QtWidgets.QSystemTrayIcon.Trigger:
            if self.hide_show_flsg == 1:
                self.hide()
                self.hide_show_flsg = 0
            elif self.hide_show_flsg == 0:
                self.show()
                self.hide_show_flsg = 1

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
# ................................................................................... # Перетаскивание окна за виджеты

# Контекстное меню .................................................................. Контекстное меню
    def contextMenuEvent(self, event: QtGui.QContextMenuEvent) -> None:
        context_menu = QtWidgets.QMenu(self)

        settings_menu = QtWidgets.QMenu(context_menu)

        hide_action = context_menu.addAction('Скрыть')
        settings_action = context_menu.addAction('Настройки')
        quit_action = context_menu.addAction('Закрыть')


        action = context_menu.exec_(self.mapToGlobal(event.pos()))

        if action == quit_action:
            sys.exit(app.exec())
        elif action == hide_action:
            self.hide()
        elif action == settings_action:
            pass

# ................................................................................... Контекстное меню
    def reload(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = MyWindow()
    application.show()
    sys.exit(app.exec())