import sqlite3

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()

# 查詢 sql
sql = 'select id, n1, n2, n3, n4, n5, ts from Lotto'
cursor.execute(sql)
rows = cursor.fetchall()
#print(rows)
for r in rows:
    #print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(r[0], r[1], r[2], r[3], r[4], r[5], r[6]))
    print('%d\t%d\t%d\t%d\t%d\t%d\t%s' % (r[0], r[1], r[2], r[3], r[4], r[5], r[6]))

conn.close()