# -*- coding:UTF-8 -*-
import math

print(math.pow(2, 3))  # 2**3
print(math.sqrt(4))  # 平方根

# 隨堂練習
x1, y1 = 10, 20
x2, y2 = 15, 45
# 求二點間的距離 d = ?
x = math.pow((x1-x2), 2)
y = math.pow((y1-y2), 2)
d = math.sqrt(x + y)
print("d=%.1f" % d)

