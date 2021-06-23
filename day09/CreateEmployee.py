import sqlite3

sql = '''
      create table Employee(
        id integer primary key not null,
        name varchar(20) not null,
        salary real
      )  
      '''
conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
cursor.execute(sql)

conn.commit()
conn.close()
print('OK')
