import random as r
ans = r.randint(1, 99)
min = 0
max = 100

while True:
    guess = int(input('請輸入 %d ~ %d : ' % (min, max)))
    if guess > ans:
        max = guess
    elif guess < ans:
        min = guess
    else:
        print('答對了')
        break;