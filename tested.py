# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tested.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_test(object):
    def setupUi(self, MainWindow_test):
        MainWindow_test.setObjectName("MainWindow_test")
        MainWindow_test.resize(713, 512)
        MainWindow_test.setStyleSheet("*\n"
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
"       padding: 4px;\n"
"    font-size: 10pt;\n"
"    border-style: solid;\n"
"\n"
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
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow_test)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(143, 13, 40, 53))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(481, 13, 40, 53))
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(52, 273, 209, 157))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(312, 286, 352, 53))
        self.label.setStyleSheet("QLabel\n"
"{\n"
"    font-size:22px;\n"
"    font-family:\"MS Shell Dlg 2\";\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(286, 0, 131, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(39, 78, 638, 53))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.listWidget = QtWidgets.QListWidget(self.splitter_2)
        self.listWidget.setObjectName("listWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(52, 156, 625, 92))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.splitter)
        self.pushButton.setObjectName("pushButton")
        MainWindow_test.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_test)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 713, 26))
        self.menubar.setObjectName("menubar")
        MainWindow_test.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_test)
        self.statusbar.setObjectName("statusbar")
        MainWindow_test.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_test)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_test)

    def retranslateUi(self, MainWindow_test):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_test.setWindowTitle(_translate("MainWindow_test", "MainWindow"))
        self.label_2.setText(_translate("MainWindow_test", "ENG"))
        self.label_3.setText(_translate("MainWindow_test", "RUS"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow_test", "Верно"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow_test", "Ошибки"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow_test", "Всего"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow_test", "Результаты"))
        self.pushButton_3.setText(_translate("MainWindow_test", "Поменять языки"))
        self.pushButton_2.setText(_translate("MainWindow_test", "Новое слово"))
        self.pushButton.setText(_translate("MainWindow_test", "Отправить"))
