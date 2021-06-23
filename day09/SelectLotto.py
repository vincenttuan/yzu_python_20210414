import sqlite3

sql = 'select * from Lotto where id=%d' % 1
print(sql)

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
cursor.execute(sql)
lotto = cursor.fetchone()
print(lotto)

conn.close()