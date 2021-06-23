import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('demo.db')
df = pd.read_sql_query("select * from Stock order by id", con=conn)
print(df)

# 繪圖
ma = df['price'].rolling(window=2).mean()  # window=2 二點計算一個平均
plt.plot(df['id'], df['price']) # 繪製折線圖
plt.plot(df['id'], ma) # 繪製移動平均線
plt.show()

conn.close()
