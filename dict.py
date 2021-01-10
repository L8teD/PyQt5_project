# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dict.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_dict(object):
    def setupUi(self, Form_dict):
        Form_dict.setObjectName("Form_dict")
        Form_dict.resize(1026, 723)
        Form_dict.setStyleSheet("*\n"
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
" QRadioButton {\n"
"     spacing: 5px;\n"
"\n"
" }\n"
"\n"
" QRadioButton::indicator {\n"
"     width: 15px;\n"
"     height: 15px;\n"
"    color:red;\n"
" }\n"
"\n"
"")
        self.tableWidget = QtWidgets.QTableWidget(Form_dict)
        self.tableWidget.setGeometry(QtCore.QRect(13, 13, 495, 703))
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
        self.pushButton_test = QtWidgets.QPushButton(Form_dict)
        self.pushButton_test.setGeometry(QtCore.QRect(611, 247, 261, 66))
        self.pushButton_test.setObjectName("pushButton_test")
        self.splitter = QtWidgets.QSplitter(Form_dict)
        self.splitter.setGeometry(QtCore.QRect(624, 325, 235, 53))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.radioButton = QtWidgets.QRadioButton(self.splitter)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.splitter)
        self.radioButton_2.setObjectName("radioButton_2")
        self.splitter_2 = QtWidgets.QSplitter(Form_dict)
        self.splitter_2.setGeometry(QtCore.QRect(611, 26, 274, 131))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.pushButton_DEL = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_DEL.setObjectName("pushButton_DEL")
        self.pushButton_ALL = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_ALL.setObjectName("pushButton_ALL")

        self.retranslateUi(Form_dict)
        QtCore.QMetaObject.connectSlotsByName(Form_dict)

    def retranslateUi(self, Form_dict):
        _translate = QtCore.QCoreApplication.translate
        Form_dict.setWindowTitle(_translate("Form_dict", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form_dict", "English words"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form_dict", "Russian words"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form_dict", "Check"))
        self.pushButton_test.setText(_translate("Form_dict", "Пройти тест"))
        self.radioButton.setText(_translate("Form_dict", "Используя слова из словаря"))
        self.radioButton_2.setText(_translate("Form_dict", "Используя все слова"))
        self.pushButton_DEL.setText(_translate("Form_dict", "Удалить выбранные элементы"))
        self.pushButton_ALL.setText(_translate("Form_dict", "Очистить словарь"))
