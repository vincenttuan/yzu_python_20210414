import sqlite3
import random

def getLotto():
    nums = set()
    # 取出1~39不重複的數字5個
    while len(nums) < 5:
        n = random.randint(1, 39)
        nums.add(n)
    return nums

print(getLotto())
print(tuple(getLotto())) # 放入資料庫，必須轉成元祖

lottos = []
for i in range(999):
    lottos.append(tuple(getLotto()))
print(len(lottos), lottos)

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
sql = 'insert into Lotto(n1, n2, n3, n4, n5) values(?, ?, ?, ?, ?)'
cursor.executemany(sql, lottos)  # 批次新增

conn.commit()
conn.close()
print('OK')