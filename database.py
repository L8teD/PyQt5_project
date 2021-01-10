# -*- coding: utf8 -*-
import _sqlite3
import parse

db = _sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS english_words (
    English TEXT,
    Russian TEXT)   
""")

db.commit()

j=0

"""Заполняем БД 5000 новых слов"""
while j <= 5000:
    x = parse.GetEnglishWords()
    eng, rus = x.parse()
    print (eng)
    for i in range(len(eng)):
        sql.execute(f"SELECT English FROM english_words WHERE English = '{eng[i]}' ") # Проверяем, есть ли слово в БД
        if sql.fetchone() is None: #Если строка пуста - заносим слово и перевод в БД
            sql.execute(f"INSERT INTO english_words VALUES (?, ?)",(eng[i],rus[i]))
            db.commit()
    j+=1

db.close()







