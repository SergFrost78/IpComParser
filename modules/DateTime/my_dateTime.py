from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QPoint, Qt, QTimer
import datetime
import sys
import os
import configparser


class MyDateTime(QtWidgets.QWidget):
    def __init__(self, path):
        super(MyDateTime, self).__init__()
        self.grid = None
        self.path = path
        self.readSettings(self.path)
        self.action = None
        self.reload_action = None
        self.context_menu = None
        self.label = None
        self.label2 = None
        self.label3 = None
        self.label4 = None

        self.datetime_data = {
            'text_1': self.current_time(),
            'font_family_1': 'Arial',
            'font_size_1': 130,
            'transparency_1': 1,
            'font_color_1': '255, 255, 0',
            'text_2': self.current_time_secs(),
            'font_family_2': 'Times New Roman',
            'font_size_2': 15,
            'transparency_2': 1,
            'font_color_2': '255, 255, 0',
            'text_3': self.current_day_of_week(),
            'font_family_3': 'Comic Sans MS',
            'font_size_3': 70,
            'transparency_3': 1,
            'font_color_3': '0, 0, 0',
            'text_4': self.current_date(),
            'font_family_4': 'Comic Sans MS',
            'font_size_4': 30,
            'transparency_4': 1,
            'font_color_4': '0, 0, 0',
        }

        self.hide_show_flag = 1
        self.init_ui()
        self.reload(self.datetime_data)

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

        timer = QTimer(self)
        timer.timeout.connect(self.run)
        timer.start(1000)

    def init_ui(self):
        self.label = QtWidgets.QLabel()
        self.label2 = QtWidgets.QLabel()
        self.label3 = QtWidgets.QLabel()
        self.label4 = QtWidgets.QLabel()

        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.label.setWordWrap(False)

        self.label2.setAutoFillBackground(False)
        self.label2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
        self.label2.setWordWrap(False)

        self.label3.setAutoFillBackground(False)
        self.label3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
        self.label3.setWordWrap(False)

        self.label4.setAutoFillBackground(False)
        self.label4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.label4.setWordWrap(False)

        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)
        self.grid.addWidget(self.label, 0, 0)
        self.grid.addWidget(self.label2, 0, 1)
        self.grid.addWidget(self.label3, 1, 0)
        self.grid.addWidget(self.label4, 1, 1, 1, 1)

    def reload(self, data):
        self.label.setText(data['text_1'])
        self.label.setFont(QtGui.QFont(data['font_family_1'], data['font_size_1']))  # Изменить шрифт
        self.label.setStyleSheet(f"color: rgba({data['font_color_1']}, {data['transparency_1']});")  # Цвет и 
        # прозрачность 

        self.label2.setText(data['text_2'])
        self.label2.setFont(QtGui.QFont(data['font_family_2'], data['font_size_2']))  # Изменить шрифт
        self.label2.setStyleSheet(f"color: rgba({data['font_color_2']}, {data['transparency_2']});")  # Цвет и 
        # прозрачность

        self.label3.setText(data['text_3'])
        self.label3.setFont(QtGui.QFont(data['font_family_3'], data['font_size_3']))  # Изменить шрифт
        self.label3.setStyleSheet(f"color: rgba({data['font_color_3']}, {data['transparency_3']});")  # Цвет и
        # прозрачность

        self.label4.setText(data['text_4'])
        self.label4.setFont(QtGui.QFont(data['font_family_4'], data['font_size_4']))  # Изменить шрифт
        self.label4.setStyleSheet(f"color: rgba({data['font_color_4']}, {data['transparency_4']});")  # Цвет и
        # прозрачность

    def saveSettings(self, path):
        if os.path.exists(path):
            config = configparser.ConfigParser()
            config.read(path)
            config.set('DateTime Settings', 'position_X', str(self.pos().x()))
            config.set('DateTime Settings', 'position_Y', str(self.pos().y()))

            with open(path, 'w') as config_file:
                config.write(config_file)

    def readSettings(self, path):
        if os.path.exists(path):
            config = configparser.ConfigParser()
            config.read(path)
            position_x = int(config.get('DateTime Settings', 'position_X'))
            position_y = int(config.get('DateTime Settings', 'position_Y'))
            self.setGeometry(position_x, position_y, 1, 1)

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

    def current_date(self):
        data = datetime.datetime.now()
        date_now = data.date()
        date_now = str(date_now).split('-')[1:]
        date_now = date_now[1], date_now[0]
        date_now = ':'.join(date_now)
        return date_now

    def current_time(self):                             # 22:35:44.65465
        data = datetime.datetime.now()
        time_now = str(data.time())
        time_now = str(time_now).split(':')[:2]
        time_now = ':'.join(time_now)
        return time_now

    def current_time_secs(self):
        data = datetime.datetime.now()
        time_now = str(data.time())
        secs = time_now.split(':')[-1].split('.')[0]
        return secs

    def current_day_of_week(self):
        week_day = datetime.datetime.today().weekday()
        week = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
        return week[week_day]

    def run(self):
        self.datetime_data['text_1'] = self.current_time()
        self.datetime_data['text_2'] = self.current_time_secs()

        self.reload(self.datetime_data)
