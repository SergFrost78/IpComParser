import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QPoint

data = {
    'text': 'halllo',
    'font': 'mr_Payload SpraycanG',
    'color': 'white',
    'size': 180,
    'transperent': .8
}


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.font_list = ['Arial', 'Arial Black', 'Calibri', 'Calibri Light', 'Comic Sans MS', 'Courier', 'Courier New', 'Georgia', 'Impact', 'Modern', 'System', 'Tahoma', 'Terminal', 'Times New Roman']
        self.font_sizes = [70, 100, 150, 200]
        self.font_transparents = [.3, .4, .5, .6, .7, .8, .9, 1]
        self.font_colors = {
            'white': '255, 255, 255',
            'black': '0, 0, 0',
            'red': '255, 0, 0',
            'green': '0, 255, 0',
            'blue': '0, 0, 255',
            'yellow': '255, 255, 0',
            'purple': '255, 0, 255',
            'light_blue': '0, 255, 255'
            }
        self.default_font = {
            'family': 'Arial',
            'size': 150,
            'tranparent': .3,
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
        #.........................................................................# Настройки прозрачности окна и т. п.

        # Инициализируем иконку в Трее ............................................Инициализируем иконку в Трее
        self.tray_icon = QtWidgets.QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_DesktopIcon))
        
        #..... Меню иконки в Трее........................
        quit_action = QtWidgets.QAction('Закрыть',self)
        quit_action.triggered.connect(app.quit)
                
        tray_menu = QtWidgets.QMenu()
        #tray_menu.addSeparator()
        tray_menu.addAction(quit_action)
        
        self.tray_icon.setContextMenu(tray_menu)

        self.tray_icon.show()
        self.tray_icon.activated.connect(self.systemIcon)
        # .........................................................................Инициализируем иконку в Трее

        '''# Список рифотв ............................................ Список рифотв
        self.font_list = QtGui.QFontDatabase()
        self.font_list = self.font_list.families()
        #print(self.font_list)
        # ...........................................................Список рифотв'''
        

    def systemIcon(self, reason): # ............................Свернуть/развернуть по клику в системном трее
        if reason == QtWidgets.QSystemTrayIcon.Trigger:
            if self.hide_show_flsg == 1:
                self.hide()
                self.hide_show_flsg = 0
            elif self.hide_show_flsg == 0:
                self.show()
                self.hide_show_flsg = 1
    
    def setFontStyle(self, data):
        self.label.setFont(QtGui.QFont(data['family'], data['size']))  # Изменить шрифт
        self.label.setStyleSheet(f'color: {data["color"]};')  # Цвет и прозрачность
        #self.color = 'QLabel { color:' + f' rgba({self.font_colors[data["color"]]}, 1);' + ' }'  # Цвет и прозрачность
        #print(self.color)


    def initUI(self):
        '''if self.color == 'black':
            self.color = "QLabel { color: rgba(0, 0, 0, 1); }"
        if self.color == 'white':
            self.color = "QLabel { color: rgba(255, 255, 255, 1); }"'''
            

        #self.WHITE = "QLabel { color: rgba(255, 255, 255, 1); }"
        #self.BLACK = "QLabel { color: rgba(0, 0, 0, 1); }"

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
        settings_menu.setTitle('Настройки')
        font_types = QtWidgets.QMenu(settings_menu)
        font_types.setTitle('Тип шрифта')
        for i in self.font_list:
            font_types.addAction(i)
        font_size = QtWidgets.QMenu(settings_menu)
        font_size.setTitle('Размер шрифта')
        for size in self.font_sizes:
            font_size.addAction(str(size))
        transp_menu = QtWidgets.QMenu(settings_menu)
        transp_menu.setTitle('Прозрачность')
        for tr in self.font_transparents:
            transp_menu.addAction(str(tr))
        color_menu = QtWidgets.QMenu(settings_menu)
        color_menu.setTitle('Цвет')
        for col in self.font_colors.keys():
            color_menu.addAction(col)
        
        hide_action = context_menu.addAction('Скрыть')
        quit_action = context_menu.addAction('Закрыть')

        context_menu.addMenu(settings_menu)
        settings_menu.addMenu(font_types)
        settings_menu.addMenu(font_size)
        settings_menu.addMenu(transp_menu)
        settings_menu.addMenu(color_menu)

        action = context_menu.exec_(self.mapToGlobal(event.pos()))
        #print(action.text())
        if action == quit_action:
            sys.exit(app.exec())
        elif action == hide_action:
            self.hide()
        elif action.text() in self.font_list:
            self.default_font['family'] = action.text()
        elif int(action.text()) in self.font_sizes:
            self.default_font['size'] = int(action.text())
            ###################################################################################################
        elif float(action.text()) in self.font_transparents:
            print('transparent')
        elif action.text() in self.font_colors.keys:
            self.default_font['color'] = action.text()
            print(action.text())
            ##################################################################################################
        self.setFontStyle(self.default_font)
# ................................................................................... Контекстное меню
    def reload(self):
        pass





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = MyWindow()
    application.show()
    sys.exit(app.exec())