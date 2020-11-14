# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1379, 770)
        MainWindow.setStyleSheet("*\n"
"{\n"
"    background:#c8a2c8;\n"
"    font-size: 15px;\n"
"    font-family: Century Gothic, sans-serif;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: #3cc9c7;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: #48f0ed;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color:#3cc9c7;\n"
"    padding: 4px;\n"
"    font-size: 10pt;\n"
"    border-style: solid;\n"
"    border-bottom: 1px solid #3cc9c7;\n"
"    border-right: 1px solid #3cc9c7;\n"
"}\n"
"\n"
"\n"
"QTableWidget {\n"
"    gridline-color:#3cc9c7 ;\n"
"    font-size: 10pt;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color:#3cc9c7;\n"
"    border: 1px solid #3cc9c7;\n"
"}\n"
"QRadioButton {\n"
"     spacing: 5px;\n"
"\n"
" }\n"
"\n"
"QRadioButton::indicator {\n"
"     width: 15px;\n"
"     height: 15px;\n"
"    color:red;\n"
" }\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(52, 26, 547, 638))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(871, 286, 339, 248))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.pushButton_make = QtWidgets.QPushButton(self.splitter)
        self.pushButton_make.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_make.setFlat(False)
        self.pushButton_make.setObjectName("pushButton_make")
        self.pushButton_open = QtWidgets.QPushButton(self.splitter)
        self.pushButton_open.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_open.setFlat(False)
        self.pushButton_open.setObjectName("pushButton_open")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(778, 93, 534, 105))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.pushButton_add = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_add.setStyleSheet("QpushButton{color:red;}")
        self.pushButton_add.setFlat(False)
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_del = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_del.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_del.setFlat(False)
        self.pushButton_del.setObjectName("pushButton_del")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setGeometry(QtCore.QRect(778, 26, 508, 40))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic,sans-serif")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(self.splitter_3)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_3 = QtWidgets.QRadioButton(self.splitter_3)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.splitter_3)
        self.radioButton_2.setObjectName("radioButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1379, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton_make, self.pushButton_del)
        MainWindow.setTabOrder(self.pushButton_del, self.tableWidget)
        MainWindow.setTabOrder(self.tableWidget, self.pushButton_add)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "English words"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Russian words"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Check"))
        self.pushButton_make.setText(_translate("MainWindow", "Добавить выделенное в словарь"))
        self.pushButton_open.setText(_translate("MainWindow", "Открыть словарь"))
        self.pushButton_add.setText(_translate("MainWindow", "Заполнить таблицу"))
        self.pushButton_del.setText(_translate("MainWindow", "Очистить таблицу"))
        self.label.setText(_translate("MainWindow", "Выбери количество выводимых слов:"))
        self.radioButton.setText(_translate("MainWindow", "5"))
        self.radioButton_3.setText(_translate("MainWindow", "10"))
        self.radioButton_2.setText(_translate("MainWindow", "15"))
