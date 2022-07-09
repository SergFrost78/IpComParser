from PyQt5 import QtWidgets, QtGui
import sys
from mainClass import MyWindow


class DesktopWidget(MyWindow):
    def __init__(self):
        super(DesktopWidget, self).__init__()
        self.hide_show_flag = 1
        self.label.setText('455')
        self.label2.setText('35 days')
        # self.secondWin = MyWindow()
        # self.secondWin.show()

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

        hide_action = self.context_menu.addAction('Скрыть')
        settings_action = self.context_menu.addAction('Настройки')
        quit_action = self.context_menu.addAction('Закрыть')

        action = self.context_menu.exec_(self.mapToGlobal(event.pos()))

        if action == quit_action:
            sys.exit(self.close())
        elif action == hide_action:
            self.hide()
            self.hide_show_flag = 0
        elif action == settings_action:
            pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = DesktopWidget()
    application.show()

    sys.exit(app.exec())