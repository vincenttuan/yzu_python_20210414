# 取得 x, y 最大值，並將最大值 x 2

def max(x, y):
    if x > y:
        return x
    else:
        return y

a = 10;
b = 15;
maxValue = max(a, b)
result = maxValue * 2
print(result)

'''
    def lambda(x, y):
        return x if x > y else y
'''
maxValue = lambda x, y : x if x > y else y
result = maxValue(a, b) * 2
print(result)

maxValue = lambda x, y : x if x > y else y
result   = lambda y : y * 2
print(result(maxValue(a, b)))