from PyQt5 import QtWidgets
import sys
from mainClass import MyWindow


class DesktopWidget(MyWindow):
    def __init__(self):
        super(DesktopWidget, self).__init__()
        self.hide_show_flsg = 1

        # Инициализируем иконку в Трее ............................................Инициализируем иконку в Трее
        self.tray_icon = QtWidgets.QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_DesktopIcon))

        # ..... Меню иконки в Трее........................
        quit_action = QtWidgets.QAction('Закрыть', self)
        quit_action.triggered.connect(app.quit)

        tray_menu = QtWidgets.QMenu()
        # tray_menu.addSeparator()
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)

        self.tray_icon.show()
        self.tray_icon.activated.connect(self.systemIcon)

    def systemIcon(self, reason): # ............................Свернуть/развернуть по клику в системном трее
        if reason == QtWidgets.QSystemTrayIcon.Trigger:
            if self.hide_show_flsg == 1:
                self.hide()
                self.hide_show_flsg = 0
            elif self.hide_show_flsg == 0:
                self.show()
                self.hide_show_flsg = 1


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = DesktopWidget()
    application.show()

    sys.exit(app.exec())