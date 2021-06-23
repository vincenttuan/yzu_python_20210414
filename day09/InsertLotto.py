import sqlite3

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
sql = '''
        insert into Lotto(n1, n2, n3, n4, n5) values(1, 3, 5, 7, 9)
      '''

cursor.execute(sql)
id = cursor.lastrowid  # 取得最新 id 值 (新增紀錄時使用)
print("id:", id)

conn.commit()
conn.close()

print('OK')