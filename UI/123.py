# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prototype_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1111, 728)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Desktop/hero.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1091, 681))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.Tab1 = QtWidgets.QWidget()
        self.Tab1.setObjectName("Tab1")
        self.label = QtWidgets.QLabel(self.Tab1)
        self.label.setGeometry(QtCore.QRect(20, 30, 141, 16))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.Tab1)
        self.textEdit.setGeometry(QtCore.QRect(180, 25, 331, 31))
        self.textEdit.setObjectName("textEdit")
        self.comboBox = QtWidgets.QComboBox(self.Tab1)
        self.comboBox.setGeometry(QtCore.QRect(180, 80, 331, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.Tab1)
        self.comboBox_2.setGeometry(QtCore.QRect(180, 120, 331, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_2 = QtWidgets.QLabel(self.Tab1)
        self.label_2.setGeometry(QtCore.QRect(20, 85, 161, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Tab1)
        self.label_3.setGeometry(QtCore.QRect(20, 125, 161, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Tab1)
        self.label_4.setGeometry(QtCore.QRect(20, 165, 161, 16))
        self.label_4.setObjectName("label_4")
        self.comboBox_3 = QtWidgets.QComboBox(self.Tab1)
        self.comboBox_3.setGeometry(QtCore.QRect(180, 160, 331, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_5 = QtWidgets.QLabel(self.Tab1)
        self.label_5.setGeometry(QtCore.QRect(580, 85, 81, 16))
        self.label_5.setObjectName("label_5")
        self.textEdit_2 = QtWidgets.QTextEdit(self.Tab1)
        self.textEdit_2.setGeometry(QtCore.QRect(730, 80, 331, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_6 = QtWidgets.QLabel(self.Tab1)
        self.label_6.setGeometry(QtCore.QRect(580, 125, 131, 16))
        self.label_6.setObjectName("label_6")
        self.comboBox_4 = QtWidgets.QComboBox(self.Tab1)
        self.comboBox_4.setGeometry(QtCore.QRect(730, 120, 331, 31))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_5 = QtWidgets.QComboBox(self.Tab1)
        self.comboBox_5.setGeometry(QtCore.QRect(730, 40, 331, 31))
        self.comboBox_5.setObjectName("comboBox_5")
        self.label_7 = QtWidgets.QLabel(self.Tab1)
        self.label_7.setGeometry(QtCore.QRect(580, 45, 151, 16))
        self.label_7.setObjectName("label_7")
        self.comboBox_6 = QtWidgets.QComboBox(self.Tab1)
        self.comboBox_6.setGeometry(QtCore.QRect(730, 160, 331, 31))
        self.comboBox_6.setObjectName("comboBox_6")
        self.label_8 = QtWidgets.QLabel(self.Tab1)
        self.label_8.setGeometry(QtCore.QRect(580, 165, 161, 16))
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.Tab1, "")
        self.Tab2 = QtWidgets.QWidget()
        self.Tab2.setObjectName("Tab2")
        self.tabWidget.addTab(self.Tab2, "")
        self.Tab3 = QtWidgets.QWidget()
        self.Tab3.setMinimumSize(QtCore.QSize(0, 0))
        self.Tab3.setBaseSize(QtCore.QSize(0, 0))
        self.Tab3.setObjectName("Tab3")
        self.tabWidget.addTab(self.Tab3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1111, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Ключ запроса"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Verdana\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">543f5e3d26764f089c50805b44fb1bf0</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Страна Репортер"))
        self.label_3.setText(_translate("MainWindow", "Страна Партнер"))
        self.label_4.setText(_translate("MainWindow", "Товар или Услуга"))
        self.label_5.setText(_translate("MainWindow", "Период"))
        self.label_6.setText(_translate("MainWindow", "Тип продкута"))
        self.label_7.setText(_translate("MainWindow", "Тип периода"))
        self.label_8.setText(_translate("MainWindow", "Торговый поток"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab1), _translate("MainWindow", "Запрос данных"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab2), _translate("MainWindow", "Анализ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab3), _translate("MainWindow", "Предсказания (Бета)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    


    MainWindow.show()
    sys.exit(app.exec_())