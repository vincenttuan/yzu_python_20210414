# x 要大於 0 才進行運算
def add(x):
    return x + 1

def sub(x):
    return x - 1

def operator(func, x):
    if x > 0:
        return func(x)
    else:
        return None

def operator2(func1, func2, x):
    if x > 0:
        return func1(x) * func2(x)
    else:
        return None

x = 1
x = operator(add, x)
print(x)

x = operator(sub, x)
print(x)

x = 10
x = operator2(add, sub, x)
print(x)