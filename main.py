from PyQt5 import QtWidgets, QtGui
import sys
from mainClass import MyWindow
from modules.IpComParser.my_parser import MyParser
from modules.IpComParser.my_parser import parser_labels

from modules.DateTime.my_dateTime import MyDateTime
from modules.DateTime.my_dateTime import datetime_labels


class DesktopWidget(MyWindow):
    def __init__(self, parser_lab, datetime_lab):
        super(DesktopWidget, self).__init__()
        self.hide_show_flag = 1

        self.parser_labels = parser_lab
        self.datetime_labels = datetime_lab

        self.parser = MyParser(self.parser_labels)
        self.parser.show()

        self.datetime = MyDateTime(self.datetime_labels)
        self.datetime.show()

    def initUI(self):
        # Инициализируем иконку в Трее ............................................Инициализируем иконку в Трее
        self.tray_icon = QtWidgets.QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_DesktopIcon))

        # ..... Меню иконки в Трее........................
        quit_action = QtWidgets.QAction('Выход', self)
        quit_action.triggered.connect(app.quit)

        tray_menu = QtWidgets.QMenu()
        # tray_menu.addSeparator()
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)

        self.tray_icon.show()
        self.tray_icon.activated.connect(self.systemIcon)

    def systemIcon(self, reason): # ............................Свернуть/развернуть по клику в системном трее
        if reason == QtWidgets.QSystemTrayIcon.Trigger:
            if self.hide_show_flag == 1:
                self.hide()
                self.hide_show_flag = 0
            elif self.hide_show_flag == 0:
                self.show()
                self.hide_show_flag = 1

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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = DesktopWidget(parser_labels, datetime_labels)
    application.show()

    sys.exit(app.exec())