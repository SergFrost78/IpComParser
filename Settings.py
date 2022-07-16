import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QColorDialog, QGraphicsColorizeEffect, QLCDNumber, QSlider, QVBoxLayout, QPushButton


class Settings(QtWidgets.QWidget):
    def __init__(self):
        super(Settings, self).__init__()

        self.initUI()
        self.show()

    def initUI(self):
        btn1 = QPushButton("Цвет", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Шрифт", self)
        btn2.move(150, 50)

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Настройки')

        label = QtWidgets.QLabel(self)
        label.setText('Прозрачность:')

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(label)
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

    def getColors(self):

        color = QColorDialog(self)
        color.currentColorChanged.connect(lambda: print(color.currentColor().getRgb()))

        color.exec_()

        #graf = QGraphicsColorizeEffect(self)
        #graf.setColor(color)
        #label.setGraphicsEffect(graf)

    def buttonClicked(self):
        sender = self.sender()
        print(sender.text() + ' was pressed')
        if sender.text() == 'Шрифт':
            pass
        elif sender.text() == 'Цвет':
            self.getColors()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = Settings()

    sys.exit(app.exec())