def getChickenAndRabbit(sum, feet):
    if feet/4 <= sum <= feet/2:
        rabbit = (feet - sum * 2)/2
        chicken = sum - rabbit
        return chicken, rabbit
    else:
        print('無法計算')
        return 0, 0

print(getChickenAndRabbit(83, 240))
c, r = getChickenAndRabbit(83, 240)
print(c, r)