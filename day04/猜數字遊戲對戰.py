import random as r
ans = r.randint(1, 99)
min = 0
max = 100
count = 5

# 判定結果
def check(guess, who):
    global min, max
    if guess > ans:
        max = guess
    elif guess < ans:
        min = guess
    else:
        print('%s答對了' % who)
        return True

    return False

while count > 0:
    # 使用者猜
    guess = int(input('(%d). 請輸入 %d ~ %d : ' % (count, min, max)))
    # 檢查 guess 的資料是否在 min 與 max 之間 ?
    if guess <= min or guess >= max:
        print('數字範圍錯誤')
        continue

    # 判定結果
    if check(guess, '使用者'):
        break

    # 電腦猜
    guess = r.randint(min+1, max-1)
    print('(%d). 電腦猜 %d ~ %d : %d' % (count, min, max, guess))

    # 判定結果
    if check(guess, '電腦'):
        break

    # 將 count 減去一次
    count = count - 1