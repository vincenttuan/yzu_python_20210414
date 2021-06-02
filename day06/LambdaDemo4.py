# 利用 lambda 設計一個 bmi 函數式宣告
# 並 "印出" 170, 60 的 "bmi 值"

h = 170
w = 60
bmiValue = lambda h, w : w / (h/100)**2
printBmiValue = lambda value : print("bmi: %.2f" % value)

printBmiValue(bmiValue(h, w))