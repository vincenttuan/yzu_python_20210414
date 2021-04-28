# 千分位 + 小數點
n = 123 * 99 * 1234 * 1.3216786
print(n)
print("%.2f" % n)
print("{:,}".format(n))
print("{:,}".format(float("%.2f" % n)))
print(format(float("%.2f" % n), ","))

