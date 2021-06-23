# 查出 n1 + n2 + .. + n5 = 60
# 有哪幾筆 ?
import sqlite3

sql = 'select * from Lotto where n1+n2+n3+n4+n5 = 60'

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
cursor.execute(sql)
rows = cursor.fetchall()
print(len(rows), rows)

conn.close()