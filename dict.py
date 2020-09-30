# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dict.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_dict(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(804, 622)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 417, 469))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.pushButton_dict = QtWidgets.QPushButton(Form)
        self.pushButton_dict.setGeometry(QtCore.QRect(468, 26, 261, 61))
        self.pushButton_dict.setObjectName("pushButton_dict")
        self.pushButton_test = QtWidgets.QPushButton(Form)
        self.pushButton_test.setGeometry(QtCore.QRect(468, 156, 261, 66))
        self.pushButton_test.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(468, 221, 222, 40))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(468, 260, 209, 40))
        self.radioButton_2.setObjectName("radioButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "English words"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Russian words"))
        self.pushButton_dict.setText(_translate("Form", "Очистить словарь"))
        self.pushButton_test.setText(_translate("Form", "Пройти тест"))
        self.radioButton.setText(_translate("Form", "Используя слова из словаря"))
        self.radioButton_2.setText(_translate("Form", "Используя все слова"))
