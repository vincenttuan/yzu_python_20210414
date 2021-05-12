import statistics as stat
import matplotlib.pyplot as plt
import matplotlib as mpl
# 調查有五位同學身高與體重如下
no = [1, 2, 3, 4, 5] # 座號
h = [172, 168, 164, 170, 176]  # cm
w = [62, 57, 58, 64, 64]  # kg
# 問該學生身高與體重的分散程度哪一個大
# 變異係數 cv = sd(標準差) / avg(平均)
h_cv = stat.stdev(h)/stat.mean(h)
w_cv = stat.stdev(w)/stat.mean(w)
print('身高 cv:', '%.2f%%' % (h_cv * 100))
print('體重 cv:', '%.2f%%' % (w_cv * 100))

# 繪圖
font = mpl.font_manager.FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
plt.plot(no, h, marker='o', color=(255/255, 0/255, 0/255))
#plt.plot(no, w, marker='o', color=(0/255, 0/255, 255/255))
plt.grid(True)
plt.title('身高統計表', fontproperties=font)
plt.show()



