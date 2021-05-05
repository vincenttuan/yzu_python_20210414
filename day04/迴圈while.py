import random as r
while True:
    n = r.randint(1, 100)
    if n % 3 == 0:
        print(n)
        continue # 繼續執行下個迴圈(此次剩下的程式碼不會執行)
    if n == 50:
        print('離開迴圈, n=', n)
        break # 強制跳離迴圈
