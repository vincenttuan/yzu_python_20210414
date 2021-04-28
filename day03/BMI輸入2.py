import math
h = float(input('請輸入身高:'))
w = float(input('請輸入體重:'))
bmi = w / math.pow(h/100, 2)
print('BMI計算結果: %.2f' % bmi)
