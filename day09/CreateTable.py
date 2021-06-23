import sqlite3

sql = '''
        create table if not exists Lotto(
            id integer primary key autoincrement,
            n1 integer not null,
            n2 integer not null,
            n3 integer not null,
            n4 integer not null,
            n5 integer not null,
            ts timestamp default current_timestamp)
      '''
conn = sqlite3.connect('demo.db')  # 建立連線
cursor = conn.cursor()  # 取得指標
cursor.execute(sql)  # 執行 sql 語句
conn.commit()  # 執行確認
conn.close()  # 關閉連線
print("OK")