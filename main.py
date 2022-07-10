from PyQt5 import QtWidgets, QtGui
import sys
from mainClass import MyWindow

label_font = {
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

class DesktopWidget(MyWindow):
    def __init__(self, data):
        super(DesktopWidget, self).__init__()
        self.data = data
        self.hide_show_flag = 1
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
        self.reload(self.data)

    def reload(self, data):
        self.label.setText(data['text_1'])
        self.label.setFont(QtGui.QFont(data['font_family_1'], data['font_size_1']))  # Изменить шрифт
        self.label.setStyleSheet(f"color: rgba({data['font_color_1']}, {data['transparency_1']});")  # Цвет и прозрачность

        self.label2.setText(data['text_2'])
        self.label2.setFont(QtGui.QFont(data['font_family_2'], data['font_size_2']))  # Изменить шрифт
        self.label2.setStyleSheet(f"color: rgba({data['font_color_2']}, {data['transparency_2']});")  # Цвет и прозрачность

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
    application = DesktopWidget(label_font)
    application.show()

    sys.exit(app.exec())