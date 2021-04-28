def f(n):
    if n == 0 or n == 1:
        return n

    return f(n-1) + f(n-2)

n = 30
value = f(n)
print(n, value)
