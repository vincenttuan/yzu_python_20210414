import random as r
n = r.randint(1, 99)
result = "偶數" if n % 2 == 0 else "奇數"
print(n, result)
print(str(n) + "是" + result)
