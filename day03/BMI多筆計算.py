import math
# 有三組資料 170, 50 ; 180, 70; 160, 60
def printBMI(h, w):
    bmi = w / math.pow(h/100, 2)
    result = "過重" if bmi > 23 else "過輕" if bmi <= 18 else "正常"
    print("h= %.1f w=%.1f bmi=%.2f result=%s" % (h, w, bmi, result))

printBMI(170, 50)
printBMI(180, 70)
printBMI(160, 60)