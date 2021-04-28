# -*- coding:UTF-8 -*-
account = 10000000  # 帳戶資金
stock = '台積電'  # 標的
price = 590.5  # 成交價
amount = 5432  # 股數
tax_ratio = 1.425/1000
fee_ratio = 3/1000
# 買入成本
cost = price * amount * (1+tax_ratio)
# 帳戶剩餘資金
account = account - cost
print(cost, account)
print("成本", cost)  # 預設 sep=" " 預設 end="\n"
print("成本", cost, sep="=", end=".\n")
# %f (浮點數) %d (整數) %s (字串)
print("成本: %.1f" % cost)
# 欲印出 --> 買進 台積電 5432 股 花費成本 $ 3212166.8 帳戶餘額 $ 6787833.2
print("買進 %s %d 股 花費成本 $ %.1f 帳戶餘額 $ %.1f" % (stock, amount, cost, account))
print("買進 %s %d 股 花費成本 $ %.1f 帳戶餘額 $ %s" % (stock, amount, cost, format(int(account*10)/10, ',')))
print("帳戶餘額 $ %s" % format(int(account*10)/10, ','))

txt = "a={}, b={}".format(12345, 67890)
print(txt)
txt = "a={:,}, b={}".format(12345, 67890)
print(txt)

# 不足補 0
rate1 = 2.321
rate2 = 32.123
rate3 = 641.567
print("%07.3f" % rate1)
print("%07.3f" % rate2)
print("%07.3f" % rate3)




