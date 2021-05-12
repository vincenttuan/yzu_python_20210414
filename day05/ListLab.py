import statistics as stat
# 調查有五位同學身高與體重如下
h = [172, 168, 164, 170, 176]  # cm
w = [62, 57, 58, 64, 64]  # kg
# 問該學生身高與體重的分散程度哪一個大
# 變異係數 cv = sd(標準差) / avg(平均)
h_cv = stat.stdev(h)/stat.mean(h)
w_cv = stat.stdev(w)/stat.mean(w)
print('身高 cv:', '%.2f%%' % (h_cv * 100))
print('體重 cv:', '%.2f%%' % (w_cv * 100))


