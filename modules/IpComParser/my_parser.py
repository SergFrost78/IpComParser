from PyQt5 import QtWidgets, QtGui,QtCore, Qt
import sys
from mainClass import MyWindow

parser_labels = {
    'text_1': '254',
    'font_family_1': 'Arial',
    'font_size_1': 150,
    'transparency_1': 1,
    'font_color_1': '255, 255, 255',
    'text_2': '31 days',
    'font_family_2': 'Comic Sans MS',
    'font_size_2': 30,
    'transparency_2': 1,
    'font_color_2': '0, 0, 0',
}


class MyParser(MyWindow):
    def __init__(self, data):
        super(MyParser, self).__init__()
        self.data = data
        self.hide_show_flag = 1

        self.reload(self.data)

    def initUI(self):
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
        self.label.setStyleSheet(f"color: rgba({data['font_color_1']}, {data['transparency_1']});")  # Цвет и прозрачность

        self.label2.setText(data['text_2'])
        self.label2.setFont(QtGui.QFont(data['font_family_2'], data['font_size_2']))  # Изменить шрифт
        self.label2.setStyleSheet(f"color: rgba({data['font_color_2']}, {data['transparency_2']});")  # Цвет и прозрачность

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
