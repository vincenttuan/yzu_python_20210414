import random as r
while True:
    n = r.randint(1, 100)
    if n % 3 == 0:
        print(n)
    if n == 50:
        print('離開迴圈, n=', n)
        break