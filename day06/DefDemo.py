def add(x=1, y=2, z=None) :
    if z is None:  # z == None
        return x + y
    return (x + y) * z


print(add())           # 3
print(add(10))         # 12
print(add(y=10))       # 11
print(add(z=10))       # 30
print(add(10, 20, 2))  # 60



