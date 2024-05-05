# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prototype_1.3.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QFileDialog, QProgressBar

from UNC_integration import *
from xlsx_formating import *
from progress import *

import csv
import pandas



import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1111, 827)
        icon = QtGui.QIcon()
        
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1091, 781))
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

        #Удаляем All, у нас будет отдельный отчет
        reporters2 = del_first_element(reporters)

        #Заполняем Комбо-бокс значениями Репортеров
        for reporter in reporters2.values():
            self.comboBox.addItem(reporter)

        self.comboBox_2 = QtWidgets.QComboBox(self.Tab1)
        self.comboBox_2.setGeometry(QtCore.QRect(180, 120, 331, 31))
        self.comboBox_2.setObjectName("comboBox_2")

        #Удаляем All, у нас будет отдельный отчет
        parnters2 = del_first_element(parnters)
        self.comboBox_2.addItem('Отчет по всем партнерам')

        #Заполняем Комбо-бокс значениями Партнеров
        for parnter in parnters2.values():
            self.comboBox_2.addItem(parnter)

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

        #Заполняем Комбо-бокс значениями Товаров и Услуг
        for good in goods_and_servicies.values():
            self.comboBox_3.addItem(good)

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

        self.comboBox_4.addItem('Товары')
        self.comboBox_4.addItem('Услуги (в разработке)')

        self.comboBox_5 = QtWidgets.QComboBox(self.Tab1)
        self.comboBox_5.setGeometry(QtCore.QRect(730, 40, 331, 31))
        self.comboBox_5.setObjectName("comboBox_5")

        self.comboBox_5.addItem('Год')
        self.comboBox_5.addItem('Год-месяц')

        self.label_7 = QtWidgets.QLabel(self.Tab1)
        self.label_7.setGeometry(QtCore.QRect(580, 45, 151, 16))
        self.label_7.setObjectName("label_7")
        self.comboBox_6 = QtWidgets.QComboBox(self.Tab1)
        self.comboBox_6.setGeometry(QtCore.QRect(730, 160, 331, 31))
        self.comboBox_6.setObjectName("comboBox_6")

        self.comboBox_6.addItem('Импорт')
        self.comboBox_6.addItem('Экспорт')

        self.label_8 = QtWidgets.QLabel(self.Tab1)
        self.label_8.setGeometry(QtCore.QRect(580, 165, 161, 16))
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.Tab1)
        self.pushButton.setGeometry(QtCore.QRect(20, 250, 341, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Tab1)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 250, 331, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.Tab1)
        self.pushButton_3.setGeometry(QtCore.QRect(730, 250, 331, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox_7 = QtWidgets.QComboBox(self.Tab1)
        self.comboBox_7.setGeometry(QtCore.QRect(918, 211, 141, 31))
        self.comboBox_7.setObjectName("comboBox_7")

        self.comboBox_7.addItem('xlsx')
        self.comboBox_7.addItem('csv')

        self.label_9 = QtWidgets.QLabel(self.Tab1)
        self.label_9.setGeometry(QtCore.QRect(735, 215, 181, 16))
        self.label_9.setObjectName("label_9")

        self.tableWidget = QtWidgets.QTableWidget(self.Tab1)
        self.tableWidget.setGeometry(QtCore.QRect(20, 300, 1041, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabWidget.addTab(self.Tab1, "")

        self.Tab2 = QtWidgets.QWidget()
        self.Tab2.setObjectName("Tab2")
        self.label_15 = QtWidgets.QLabel(self.Tab2)
        self.label_15.setGeometry(QtCore.QRect(40, 25, 400, 16))
        self.label_15.setObjectName("label_15")
        self.comboBox_8 = QtWidgets.QComboBox(self.Tab2)
        self.comboBox_8.setGeometry(QtCore.QRect(170, 70, 400, 31))
        self.comboBox_8.setObjectName("comboBox_8")
        self.label_10 = QtWidgets.QLabel(self.Tab2)
        self.label_10.setGeometry(QtCore.QRect(40, 75, 151, 16))
        self.label_10.setObjectName("label_10")
        self.pushButton_4 = QtWidgets.QPushButton(self.Tab2)
        self.pushButton_4.setGeometry(QtCore.QRect(650, 20, 331, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.Tab2)
        self.pushButton_5.setGeometry(QtCore.QRect(650, 70, 331, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.widget = QtWidgets.QWidget(self.Tab2)
        self.widget.setGeometry(QtCore.QRect(20, 130, 1041, 601))
        self.widget.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.widget.setObjectName("widget")
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
        self.textEdit_2.setText(_translate("MainWindow", "2022"))
        self.label_2.setText(_translate("MainWindow", "Страна Репортер"))
        self.label_3.setText(_translate("MainWindow", "Страна Партнер"))
        self.label_4.setText(_translate("MainWindow", "Товар или Услуга"))
        self.label_5.setText(_translate("MainWindow", "Период"))
        self.label_6.setText(_translate("MainWindow", "Тип продкута"))
        self.label_7.setText(_translate("MainWindow", "Тип периода"))
        self.label_8.setText(_translate("MainWindow", "Торговый поток"))
        self.pushButton.setText(_translate("MainWindow", "Запрос данных"))
        self.pushButton_2.setText(_translate("MainWindow", "Загрузить"))
        self.pushButton_3.setText(_translate("MainWindow", "Сохранить"))
        self.label_9.setText(_translate("MainWindow", "Формат сохранения"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab1), _translate("MainWindow", "Запрос данных"))
        self.label_15.setText(_translate("MainWindow", "Автоопределение формата: "))
        self.label_10.setText(_translate("MainWindow", "Тип графика"))
        self.pushButton_4.setText(_translate("MainWindow", "Построить"))
        self.pushButton_5.setText(_translate("MainWindow", "Сохранить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab2), _translate("MainWindow", "Анализ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab3), _translate("MainWindow", "Предсказания (Бета)"))

        self.connects()

    #Активация кнопок
    def connects(self):
        self.pushButton.clicked.connect(self.get_data)
        self.pushButton_3.clicked.connect(self.save_to)
        self.pushButton_2.clicked.connect(self.load)

    def get_data(self):
    
        print('Read widgets..')
        subscription_key = self.textEdit.toPlainText()
        reporterText = self.comboBox.currentText()
        partnerText = self.comboBox_2.currentText()
        cmdText = self.comboBox_3.currentText()
        periodType = self.comboBox_5.currentText()
        period = self.textEdit_2.toPlainText()
        productType = self.comboBox_4.currentText()
        tradeType = self.comboBox_6.currentText()

        reporter_code = get_key(reporters, reporterText)
        parnter_code = get_key(parnters, partnerText)
        cmdCodeTxt= get_key(goods_and_servicies, cmdText)

        if cmdText == 'Total Trade':
            cmdCodeTxt == 'TOTAL'

        flowCode = 'M'
        freqCodeq = 'A'
        typeCodeq = 'C'

        if tradeType == 'Импорт':
            flowCode = 'M'
        elif tradeType == 'Экспорт':
            flowCode = 'X'

        # М не работает
        if periodType == 'Год':
            freqCodeq = 'A'
        elif periodType == 'Год-месяц':
            freqCodeq = 'M'

        # S не работает??
        if productType == 'Товары':
            typeCodeq = 'C'
        elif productType == 'Услуги (в разработке)':
            typeCodeq = 'S'

        request = {
            'subscription_key': subscription_key,
            'typeCode': typeCodeq,
            'freqCode': freqCodeq,
            'period': period,
            'partnerCode': parnter_code,
            'reporterCode': reporter_code,
            'cmdCode': cmdCodeTxt,
            'flowCode': flowCode,
            'partтerTxt': partnerText,
            'reporterTxt': reporterText
        }

        print(self.comboBox_2.currentText())

        #Проверяем Отчет или обычная выгрузка
        if self.comboBox_2.currentText() == 'Отчет по всем партнерам':
            print('Отчет по всем партнерам')
            self.loading_bar = LoadingBar()
            self.loading_bar.show()
            self.loading_bar.start()

        else:
            self.df_aistrade = get_request(request)
            #Вывести запросы
            print(self.df_aistrade)
            

            #Проверяем корректность запроса
            if self.df_aistrade is None:
                print('ERROR: NO DATA')
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText("Некорректные параметры запроса. Проверьте выставленные параметры.")
                msg.setIcon(QMessageBox.Warning)
                
                msg.exec_()
            elif self.df_aistrade.empty:
                print('ERROR: Empty')
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText("Не удалось получить данные. Данные отсутсвуют в базе или недоступны.")
                msg.setIcon(QMessageBox.Warning)

                msg.exec_()
            else:
                #Заполняем таблицу данными
                self.df_aistrade = transformation_to_russian(self.df_aistrade)
                self.frame_to_table(self.df_aistrade)

                _translate = QtCore.QCoreApplication.translate
                self.label_15.setText(_translate("MainWindow", "Автоопределение формата: Товарный отчет"))

                self.get_actual_graphics()

    #Сохранение     
    def save_to(self):
        file_path = QFileDialog.getSaveFileName(None, 'Сохранить файл', '', 'Файлы Excel (*.xlsx)')

        print(file_path[0])
        if file_path:
            self.df_aistrade.to_excel(file_path[0], index= False)
            # напечатать сообщение об успехе
            print(f"DataFrame сохранен в {file_path}")
            formating(file_path[0])
    
    #Функция кнопки загрузить
    def load(self):
        file_path = QFileDialog.getOpenFileName(None, "Открыть файл xlsx", "", "Файлы Excel (*.xlsx)")
        self.df_aistrade = pd.read_excel(file_path[0])
        self.frame_to_table(self.df_aistrade)

        #Определение типа даты для посстроения графика
        _translate = QtCore.QCoreApplication.translate

        if str(self.df_aistrade.columns[0]) == 'Reporter':
            self.label_15.setText(_translate("MainWindow", "Автоопределение формата: Отчет по странам"))
        elif str(self.df_aistrade.columns[0])  == 'Тип (C/S)':
            self.label_15.setText(_translate("MainWindow", "Автоопределение формата: Товарный отчет"))
        else:
            self.label_15.setText(_translate("MainWindow", "Автоопределение формата: Не определен"))

        self.get_actual_graphics()

    #Отрисовывает в таблице на окне полученный data_frame
    def frame_to_table(self, df):
        # Устанавливаем количество строк и столбцов в TableWidget
        self.tableWidget.setRowCount(df.shape[0])
        self.tableWidget.setColumnCount(df.shape[1])

        self.tableWidget.setHorizontalHeaderLabels(df.columns)
        # Заполняем TableWidget данными из DataFrame Pandas
        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                item = QTableWidgetItem(str(df.iloc[i, j]))
                self.tableWidget.setItem(i, j, item)
                
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.show()
    
    #Функция отображения досупных графиков в зависимости от типа
    def get_actual_graphics(self):
        if (self.label_15.text() == 'Автоопределение формата: Отчет по странам'):
            #Предложить графики по отчету по странам
            self.comboBox_8.clear()
            self.comboBox_8.addItem('Рейтинг крупнейших партнеров (1 год)')
            self.comboBox_8.addItem('Рейтинг крупнейших партнеров (5 год)')
            self.comboBox_8.addItem('Рейтинг крупнейших партнеров (10 лет)')
            self.comboBox_8.addItem('Рейтинг крупнейших партнеров (MAX)')
            
        elif (self.label_15.text() == 'Автоопределение формата: Товарный отчет'):
            #Предложить графики по товарному отчету
            self.comboBox_8.clear()
            self.comboBox_8.addItem('Рейтинг крупнейших сделок (6 разрдов GS)')
            self.comboBox_8.addItem('Рейтинг крупнейших сделок (4 разряда GS)')
            self.comboBox_8.addItem('Рейтинг крупнейших сделок (2 разряда GS)')




#Возвращает ключ по значению из dict
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
        
def csv_to_dict(file_path):
    import codecs
    with codecs.open(file_path, 'r', 'utf_8_sig') as csv_file:
        reader = csv.reader(csv_file)
        dict_data = {}
        for row in reader:
            dict_data[row[0]] = row[1]

    #Удаляем шапку
    dict_data = del_first_element(dict_data)

    return dict_data

def del_first_element(dict_data):
    first_key = next(iter(dict_data))
    dict_data.pop(first_key)
    return dict_data

#Метод заполняющий комбо-боксы данными из справочника
def directory_to_widgets():
    #Получаем текущую директорию
    current_dir = os.getcwd()

    global reporters
    global parnters
    global goods_and_servicies

    #Получаем данные о доступных Репортерах и Партнерах их Справочной информации
    reporters = csv_to_dict(os.path.join(current_dir,'reference', 'reporterAreas.csv'))
    parnters = csv_to_dict(os.path.join(current_dir,'reference', 'partnerAreas.csv'))

    #Получаем данные о доступных Товарах
    goods_and_servicies = csv_to_dict(os.path.join(current_dir,'reference', 'UN_goods_codes.csv'))

    
    

if __name__ == "__main__":
    import sys
    
    directory_to_widgets()

    #Создаем приложениe
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    #Показать и не дать закрыться
    MainWindow.show()
    sys.exit(app.exec_())
