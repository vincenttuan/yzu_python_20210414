import sqlite3

sql = '''
      create table Stock(
        id integer primary key not null,
        name varchar(20) not null,
        price real
      )  
      '''
conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
cursor.execute(sql)

conn.commit()
conn.close()
print('OK')
