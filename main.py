# -*- coding: utf8 -*-
import sys
import _sqlite3
from des import *
from PyQt5.QtWidgets import  QMessageBox
from dict import *
from tested import *

"""Создание объекта окна словаря"""
class Dict (QtWidgets.QMainWindow):
    def __init__(self ,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.dict = Ui_Form_dict ()
        self.dict.setupUi (self)

"""Создание объекта окна теста"""
class Test(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__ (self ,parent)
        self.test = Ui_MainWindow_test()
        self.test.setupUi(self)

"""Создание главного окна"""
class MyWin(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Параметры таблицы
        self.row_count = 1
        self.table_index = 0
        # Кол-во выводимых слов
        self.cnt_wrd = 0
        # Открытие БД
        self.db = _sqlite3.connect('server.db')
        self.sql = self.db.cursor()

        # Кнопки главного окна
        self.ui.pushButton_add.clicked.connect(self.add_table_item)
        self.ui.pushButton_del.clicked.connect(self.delete_table_item)
        self.ui.pushButton_make.clicked.connect(self.make_dict)
        self.ui.pushButton_open.clicked.connect(self.open_dict)

    """Заполнение таблицы главного окна"""
    def add_table_item(self):
        self.row_count = 1
        self.table_index = 0
        if self.ui.radioButton.isChecked():
            self.cnt_wrd = 5
        elif self.ui.radioButton_3.isChecked():
            self.cnt_wrd = 10
        elif self.ui.radioButton_2.isChecked():
            self.cnt_wrd = 15
        else:
            self.show_error_dict()
        # Открываем таблицу англ. слов внутри БД
        self.sql.execute ("""CREATE TABLE IF NOT EXISTS english_words (
            English TEXT,
            Russian TEXT)   
        """)
        self.db.commit()

        curr_wrd = 0 # Счетчик уже занесенных в таблицу слов
        for value in self.sql.execute("SELECT * FROM english_words ORDER BY RANDOM()"):
            if curr_wrd < self.cnt_wrd:
                self.ui.tableWidget.setRowCount (self.row_count)
                self.ui.tableWidget.setItem (self.table_index ,0 ,QtWidgets.QTableWidgetItem (value[0]))
                self.ui.tableWidget.setItem (self.table_index ,1 ,QtWidgets.QTableWidgetItem (value[1]))
                self.ui.tableWidget.setCellWidget (self.table_index ,2 ,QtWidgets.QCheckBox())
                self.ui.tableWidget.resizeColumnsToContents()
                self.table_index += 1
                self.row_count += 1
                curr_wrd += 1

    """Формирование словаря"""
    def make_dict(self):
        """Создаем таблицу словаря"""
        self.sql.execute ("""CREATE TABLE IF NOT EXISTS dictionary (
            English TEXT,
            Russian TEXT)   
        """)
        self.db.commit()
        """Формируем таблицу БД в соответствии с отметками в таблице словаря"""
        for i in range (self.ui.tableWidget.rowCount ()):
            if self.ui.tableWidget.cellWidget (i ,2).isChecked ():
                self.sql.execute (f"SELECT English FROM dictionary WHERE "
                             f"English = '{self.ui.tableWidget.item(i,0).text()}' ")
                if self.sql.fetchone() is None: # Является ли строка таблицы БД пустой
                    self.sql.execute(f"INSERT INTO dictionary VALUES (?, ?)",
                                (self.ui.tableWidget.item(i,0).text(),self.ui.tableWidget.item(i,1).text()))
                    self.db.commit()


    """Открытие словаря в новом окне"""
    def open_dict(self):
        self.row_count = 1
        self.table_index = 0
        """Инициализация объекта окна словаря"""
        self.dict_window = Dict()
        self.dict_window.show()
        """Заполняем таблицу словаря"""
        for value in self.sql.execute ("SELECT * FROM dictionary"):
            self.dict_window.dict.tableWidget.setRowCount (self.row_count)
            self.dict_window.dict.tableWidget.setItem (self.table_index ,0 ,QtWidgets.QTableWidgetItem (value[0]))
            self.dict_window.dict.tableWidget.setItem (self.table_index ,1 ,QtWidgets.QTableWidgetItem (value[1]))
            self.dict_window.dict.tableWidget.setCellWidget (self.table_index ,2 ,QtWidgets.QCheckBox ())
            self.dict_window.dict.tableWidget.resizeColumnsToContents ()
            self.table_index += 1
            self.row_count += 1
        """Кнопки окна словаря"""
        self.dict_window.dict.pushButton_ALL.clicked.connect(lambda:self.clear_dict())
        self.dict_window.dict.pushButton_test.clicked.connect(lambda:self.pass_test())
        self.dict_window.dict.pushButton_DEL.clicked.connect(lambda:self.del_selected())

    """Удаление выбранных слов из словаря"""
    def del_selected(self):
        for i in range (self.dict_window.dict.tableWidget.rowCount ()):
            if self.dict_window.dict.tableWidget.cellWidget(i,2).isChecked():
                self.sql.execute(f"DELETE FROM dictionary WHERE English = '{self.dict_window.dict.tableWidget.item(i,0).text()}'")
                self.db.commit()
        return self.open_dict() # Открываем окно словаря заново

    """Открытия окна с тестом"""
    def pass_test(self):
        self.cnt_correct = 0
        self.cnt_mistakes = 0
        self.old_rus_words = []
        self.old_eng_words = []
        if self.dict_window.dict.radioButton.isChecked():
            self.test_window = Test() # Инициализация объекта окна теста
            self.test_window.show()
            """Кнопки окна с тестом"""
            self.test_window.test.pushButton_new.clicked.connect(self.new_word_dict) # Слова из словаря
            self.test_window.test.pushButton_switch.clicked.connect(self.change_languages)
        elif self.dict_window.dict.radioButton_2.isChecked():
            self.test_window = Test () # Инициализация объекта окна теста
            self.test_window.show ()
            """Кнопки окна с тестом"""
            self.test_window.test.pushButton_new.clicked.connect (self.new_word_all) # Все слова
            self.test_window.test.pushButton_switch.clicked.connect (self.change_languages)
        else:
            self.show_error_test ()

    """Функция смены языков"""
    def change_languages(self):
        doc = QtGui.QTextDocument ()
        doc.setHtml (self.test_window.test.label_2.text ())
        text = doc.toPlainText ()

        if text == 'ENG':
            self.test_window.test.label_2.clear()
            self.test_window.test.label_3.clear()
            self.test_window.test.label_2.setText('RUS')
            self.test_window.test.label_3.setText('ENG')

        if text=='RUS':
            self.test_window.test.label_2.clear()
            self.test_window.test.label_3.clear()
            self.test_window.test.label_2.setText('ENG')
            self.test_window.test.label_3.setText('RUS')

    """Добавление нового слова из БД"""
    def new_word_all(self):
        doc = QtGui.QTextDocument ()
        doc.setHtml (self.test_window.test.label_2.text ())
        text = doc.toPlainText ()
        self.test_window.test.label.clear ()
        self.test_window.test.listWidget.clear ()
        self.test_window.test.lineEdit.clear ()
        self.sql.execute ("""CREATE TABLE IF NOT EXISTS english_words (
                                       English TEXT,
                                       Russian TEXT)
                                   """)
        if text == 'ENG':
            for value in self.sql.execute ("SELECT * FROM english_words ORDER BY RANDOM()"):
                if value[0] not in self.old_eng_words: # Добавлялось ли слово раньше
                    self.eng_test_value = value[0]
                    self.rus_test_value = value[1]
                    self.test_window.test.listWidget.addItem (self.eng_test_value)
                    self.old_eng_words.append (self.eng_test_value)
                    break
        elif text == 'RUS':
            for value in self.sql.execute ("SELECT * FROM english_words ORDER BY RANDOM()"):
                if value[1] not in self.old_eng_words: # Добавлялось ли слово раньше
                    self.eng_test_value = value[0]
                    self.rus_test_value = value[1]
                    self.test_window.test.listWidget.addItem (self.rus_test_value)
                    self.old_eng_words.append (self.rus_test_value)
                    break

        self.test_window.test.pushButton_send.clicked.connect (self.res_test)

    """Добавление нового слова из словаря"""
    def new_word_dict(self):
        doc = QtGui.QTextDocument ()
        doc.setHtml (self.test_window.test.label_2.text ())
        text = doc.toPlainText ()
        self.test_window.test.label.clear()
        self.test_window.test.listWidget.clear()
        self.test_window.test.lineEdit.clear()

        self.sql.execute ("""CREATE TABLE IF NOT EXISTS dictionary (
                               English TEXT,
                               Russian TEXT)   
                           """)
        if text == 'ENG':
            for value in self.sql.execute ("SELECT * FROM dictionary ORDER BY RANDOM()"):
                if value[0] not in self.old_eng_words: # Добавлялось ли слово раньше
                    self.eng_test_value = value[0]
                    self.rus_test_value = value[1]
                    self.test_window.test.listWidget.addItem(self.eng_test_value)
                    self.old_eng_words.append(self.eng_test_value)
                    break
        elif text == 'RUS':
            for value in self.sql.execute ("SELECT * FROM dictionary ORDER BY RANDOM()"):
                if value[1] not in self.old_eng_words: # Добавлялось ли слово раньше
                    self.eng_test_value = value[0]
                    self.rus_test_value = value[1]
                    self.test_window.test.listWidget.addItem (self.rus_test_value)
                    self.old_eng_words.append (self.rus_test_value)
                    break
        self.test_window.test.pushButton_send.clicked.connect (self.res_test)

    """Вывод результатов теста"""
    def res_test(self):
        doc = QtGui.QTextDocument ()
        doc.setHtml (self.test_window.test.label_2.text ())
        text = doc.toPlainText ()
        if text == 'ENG':
            if self.test_window.test.lineEdit.text() != '':
                if self.test_window.test.lineEdit.text() not in self.old_rus_words:
                    self.old_rus_words.append(self.test_window.test.lineEdit.text())
                    if self.test_window.test.lineEdit.text() == self.rus_test_value:
                        self.test_window.test.label.setText("Абсолютно верно")
                        self.cnt_correct += 1

                        self.test_window.test.tableWidget.setItem(0,0,QtWidgets.QTableWidgetItem(str(self.cnt_correct)))
                        self.test_window.test.tableWidget.setItem(1,0,QtWidgets.QTableWidgetItem(str(self.cnt_mistakes)))
                        self.test_window.test.tableWidget.setItem(2,0,QtWidgets.QTableWidgetItem(str(self.cnt_correct+self.cnt_mistakes)))
                    else:
                        string = "Не совсем точно:\n {} - {}".format(self.eng_test_value,self.rus_test_value)
                        self.test_window.test.label.setText (string)
                        self.cnt_mistakes += 1

                        self.test_window.test.tableWidget.setItem (0 ,0 ,QtWidgets.QTableWidgetItem (str (self.cnt_correct)))
                        self.test_window.test.tableWidget.setItem (1 ,0 ,QtWidgets.QTableWidgetItem (str (self.cnt_mistakes)))
                        self.test_window.test.tableWidget.setItem (2 ,0 ,QtWidgets.QTableWidgetItem (str (self.cnt_correct + self.cnt_mistakes)))
        elif text == 'RUS':
            if self.test_window.test.lineEdit.text () != '':
                if self.test_window.test.lineEdit.text () not in self.old_rus_words:
                    self.old_rus_words.append (self.test_window.test.lineEdit.text ())
                    if self.test_window.test.lineEdit.text () == self.eng_test_value:
                        self.test_window.test.label.setText ("Абсолютно верно")
                        self.cnt_correct += 1

                        self.test_window.test.tableWidget.setItem (0 ,0 ,
                                                                   QtWidgets.QTableWidgetItem (str (self.cnt_correct)))
                        self.test_window.test.tableWidget.setItem (1 ,0 ,
                                                                   QtWidgets.QTableWidgetItem (str (self.cnt_mistakes)))
                        self.test_window.test.tableWidget.setItem (2 ,0 ,QtWidgets.QTableWidgetItem (str (self.cnt_correct + self.cnt_mistakes)))
                    else:
                        string = "Не совсем точно:\n {} - {}".format (self.eng_test_value ,self.rus_test_value)
                        self.test_window.test.label.setText (string)
                        self.cnt_mistakes += 1

                        self.test_window.test.tableWidget.setItem (0 ,0 ,
                                                                   QtWidgets.QTableWidgetItem (str (self.cnt_correct)))
                        self.test_window.test.tableWidget.setItem (1 ,0 ,
                                                                   QtWidgets.QTableWidgetItem (str (self.cnt_mistakes)))
                        self.test_window.test.tableWidget.setItem (2 ,0 ,QtWidgets.QTableWidgetItem (
                            str (self.cnt_correct + self.cnt_mistakes)))


    """Очистка словаря"""
    def clear_dict(self):
        self.dict_window_current = Dict()
        self.dict_window_current.show()
        self.sql.execute ("DELETE FROM dictionary")
        self.db.commit()
        self.dict_window.dict.tableWidget.clear()
        self.table_index = 0
        self.row_count = 1
        self.dict_window_current.dict.tableWidget.setHorizontalHeaderItem (0 ,QtWidgets.QTableWidgetItem ('English'))
        self.dict_window_current.dict.tableWidget.setHorizontalHeaderItem (1 ,QtWidgets.QTableWidgetItem ('Russian'))

        return self.dict_window.close()

    """Очистка таблицы главного окна"""
    def delete_table_item(self):
        self.table_index = 0
        self.row_count = 1
        self.ui.tableWidget.clear ()
        self.ui.tableWidget.setHorizontalHeaderItem (0 ,QtWidgets.QTableWidgetItem ('English'))
        self.ui.tableWidget.setHorizontalHeaderItem (1 ,QtWidgets.QTableWidgetItem ('Russian'))
        self.ui.tableWidget.setHorizontalHeaderItem (2 ,QtWidgets.QTableWidgetItem ('Check'))
    """Показ окна с ошибкой"""
    def show_error_dict(self):
        msg = QMessageBox()
        msg.setWindowTitle('Ошибка')
        msg.setText('Выберите количество вводимых слов')
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    """Показ окна с ошибкой"""
    def show_error_test(self):
        msg = QMessageBox()
        msg.setWindowTitle('Ошибка')
        msg.setText('Выберите список, используемых слов')
        msg.setIcon(QMessageBox.Information)
        msg.exec_()


# Ссылка на перехватчик исключений
sys._excepthook = sys.excepthook

def my_exception_hook(exctype, value, traceback):
    # Вывести ошибку и ее трейсбек
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)

# Установить ловушку исключений
sys.excepthook = my_exception_hook

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    try:
        sys.exit (app.exec_ ())
    except:
        print ("Exiting")