from PyQt5 import QtWidgets
import sys
from modules.IpComParser.my_parser import MyParser, parser_labels
from modules.DateTime.my_dateTime import MyDateTime, datetime_labels


class DesktopWidget(QtWidgets.QWidget):
    def __init__(self, parser_lab, datetime_lab):
        super(DesktopWidget, self).__init__()
        self.action = None
        self.reload_action = None
        self.context_menu = None
        self.tray_icon = None

        self.parser_labels = parser_lab
        self.datetime_labels = datetime_lab

        self.hide_show_flag = 1
        self.init_ui()

        self.parser = MyParser(self.parser_labels)
        self.parser.show()

        self.date_time = MyDateTime(self.datetime_labels)
        self.date_time.show()
        # self.show()

    def init_ui(self):
        # Init tray icon
        self.tray_icon = QtWidgets.QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_DesktopIcon))

        # Menu tray icon
        quit_action = QtWidgets.QAction('Выход', self)
        quit_action.triggered.connect(app.quit)

        tray_menu = QtWidgets.QMenu()
        # tray_menu.addSeparator()
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = DesktopWidget(parser_labels, datetime_labels)
    sys.exit(app.exec())
