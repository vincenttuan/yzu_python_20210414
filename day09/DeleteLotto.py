import sqlite3

sql = 'delete from lotto where id=%d' % 1
print(sql)

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
cursor.execute(sql)

rowcount = cursor.rowcount
if rowcount > 0:
    print('delete ok, rowcount:', rowcount)
else:
    print('delete none, rowcount:', rowcount)

conn.commit()
conn.close()