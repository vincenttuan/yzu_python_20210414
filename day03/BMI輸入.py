h = input('請輸入身高:')
w = input('請輸入體重:')
print(h, type(h))
print(w, type(w))
h = float(h)  # 將 str 轉成 float
w = float(w)  # 將 str 轉成 float
print(h, type(h))
print(w, type(w))
bmi = w / ((h/100) ** 2)
print("%.2f" % bmi)

