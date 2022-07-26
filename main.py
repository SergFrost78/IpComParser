from PyQt5 import QtWidgets
import sys
import os
import configparser
from modules.IpComParser.my_parser import MyParser
from modules.DateTime.my_dateTime import MyDateTime


class DesktopWidget(QtWidgets.QWidget):
    def __init__(self):
        super(DesktopWidget, self).__init__()
        self.path = 'Settings.ini'
        if not os.path.exists(self.path):
            self.createConfigFile(self.path)
        self.action = None
        self.reload_action = None
        self.context_menu = None
        self.tray_icon = None

        self.hide_show_flag = 1
        self.init_ui()

        self.parser = MyParser(self.path)
        self.parser.show()

        self.datetime = MyDateTime(self.path)
        self.datetime.show()
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

    def createConfigFile(self, path):
        config = configparser.ConfigParser()
        config.add_section('Parser Settings')
        config.add_section('DateTime Settings')

        with open(path, 'w') as config_file:
            config.write(config_file)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = DesktopWidget()
    sys.exit(app.exec())
