import sqlite3

sql = 'update lotto set n1=%d, n2=%d where id=%d' % (39, 38, 1)
print(sql)

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
cursor.execute(sql)

print('Update ok, rowcount:', cursor.rowcount)

conn.commit()
conn.close()