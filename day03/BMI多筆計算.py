import math
# 有三組資料 170, 50 ; 180, 70; 160, 60
def printBMI(h, w):
    bmi = w / math.pow(h/100, 2)
    print("h= %.1f w=%.1f bmi=%.2f" % (h, w, bmi))

printBMI(170, 50)
printBMI(180, 70)
printBMI(160, 60)