import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('demo.db')
df = pd.read_sql_query("select * from Stock order by id", con=conn)
print(df)

# 繪圖
plt.plot(df['id'], df['price']) # 繪製折線圖
plt.show()

conn.close()
