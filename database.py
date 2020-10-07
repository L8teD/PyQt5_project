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

while j<=5000:

    x = parse.get_english_words()

    eng, rus = x.parse()
    for i in range(len(eng)):
        sql.execute(f"SELECT English FROM english_words WHERE English = '{eng[i]}' ")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO english_words VALUES (?, ?)",(eng[i],rus[i]))
            db.commit()
    print(j)
    j+=1


db.close()







