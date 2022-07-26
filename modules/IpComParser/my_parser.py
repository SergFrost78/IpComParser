from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QPoint, Qt
import sys
import os
import configparser


class MyParser(QtWidgets.QWidget):
    def __init__(self, path):
        super(MyParser, self).__init__()
        self.path = path
        self.readSettings(self.path)
        self.action = None
        self.reload_action = None
        self.context_menu = None
        self.layout = None
        self.label2 = None
        self.label = None
        self.hide_show_flag = 1
        self.init_ui()
        self.press = False
        self.last_pos = QPoint(0, 0)

        self.parser_data = {
            'text_1': '254',
            'font_family_1': 'Arial',
            'font_size_1': 150,
            'transparency_1': 1,
            'font_color_1': '255, 0, 255',
            'text_2': '31 days',
            'font_family_2': 'Comic Sans MS',
            'font_size_2': 30,
            'transparency_2': 1,
            'font_color_2': '0, 0, 0',
        }

        # Настройки прозрачности окна и т. п......................................# Настройки прозрачности окна и т. п.
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.setWindowFlags(
            QtCore.Qt.Window
            | QtCore.Qt.CustomizeWindowHint
            | QtCore.Qt.FramelessWindowHint
            | QtCore.Qt.Tool
        )

        self.reload(self.parser_data)

    def init_ui(self):
        self.label = QtWidgets.QLabel()
        self.label2 = QtWidgets.QLabel()

        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.label.setWordWrap(False)

        self.label2.setAutoFillBackground(False)
        self.label2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
        self.label2.setWordWrap(False)

        self.layout = QtWidgets.QVBoxLayout()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.label2)

        self.setLayout(self.layout)

    def reload(self, data):
        self.label.setText(data['text_1'])
        self.label.setFont(QtGui.QFont(data['font_family_1'], data['font_size_1']))  # Изменить шрифт
        self.label.setStyleSheet(f"color: rgba({data['font_color_1']}, {data['transparency_1']});")  # Цвет и
        # прозрачность

        self.label2.setText(data['text_2'])
        self.label2.setFont(QtGui.QFont(data['font_family_2'], data['font_size_2']))  # Изменить шрифт
        self.label2.setStyleSheet(f"color: rgba({data['font_color_2']}, {data['transparency_2']});")  # Цвет и
        # прозрачность

    def saveSettings(self, path):
        if os.path.exists(path):
            config = configparser.ConfigParser()
            config.read(path)
            config.set('Parser Settings', 'position_X', str(self.pos().x()))
            config.set('Parser Settings', 'position_Y', str(self.pos().y()))

            with open(path, 'w') as config_file:
                config.write(config_file)

    def readSettings(self, path):
        if os.path.exists(path):
            config = configparser.ConfigParser()
            config.read(path)
            position_x = int(config.get('Parser Settings', 'position_X'))
            position_y = int(config.get('Parser Settings', 'position_Y'))
            self.setGeometry(position_x, position_y, 1, 1)

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
            self.saveSettings(self.path)

    def contextMenuEvent(self, event: QtGui.QContextMenuEvent) -> None:
        self.context_menu = QtWidgets.QMenu(self)

        self.reload_action = self.context_menu.addAction('Обновить')
        hide_action = self.context_menu.addAction('Скрыть')
        settings_action = self.context_menu.addAction('Настройки')
        quit_action = self.context_menu.addAction('Закрыть')

        self.action = self.context_menu.exec_(self.mapToGlobal(event.pos()))

        if self.action == quit_action:
            sys.exit(self.close())
        elif self.action == hide_action:
            self.hide()
            self.hide_show_flag = 0
        elif self.action == settings_action:
            pass
        elif self.action == self.reload_action:
            pass
