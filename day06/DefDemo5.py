x = 0
y = 0

def changeX(n):
    x = n  # x 是 changeX 的區域變數
    print('changeX() 的 x=', x)

def changeY(n):
    global y
    y = n
    print('changeY() 的 global y=', y)

print('main() 的 x=', x)
changeX(100)
print('main() 的 x=', x)

print('main() 的 y=', y)
changeY(100)
print('main() 的 y=', y)