import sys
from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar

class LoadingBar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.progressbar = QProgressBar(self)
        self.progressbar.setGeometry(30, 40, 200, 25)
        self.progressbar.setValue(1)

        self.timer = QBasicTimer()
        self.step = 1

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Выгрузка отчета по всем партнерам')

    def timerEvent(self, event):
        self.progressbar.setValue(self.step)
        self.step += 1

    def start(self):
        self.timer.start(30000, self)

# Вызываем функцию для отображения полосы загрузки
#def show_loading_bar():
    #App = QApplication (sys.argv)
    #loading_bar = LoadingBar()
    #loading_bar.show()
    #loading_bar.start()

    #sys.exit(App.exec_())


