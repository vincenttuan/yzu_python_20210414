import sqlite3
import random

stocks = []
for i in range(100):
    stock = []
    stock.append(i+1)
    stock.append('2330')
    stock.append(random.randint(500, 600))
    stocks.append(tuple(stock))

print(stocks)

sql = 'insert into Stock(id, name, price) values(?, ?, ?)'
conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
cursor.executemany(sql, stocks)

conn.commit()
conn.close()
print('OK')