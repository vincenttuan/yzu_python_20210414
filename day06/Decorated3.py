# 裝飾器 3

def make_dress(func):
    def dress():
        print("穿衣服")
        func()
    return dress

def make_shoes(func):
    def shoes():
        print("穿鞋子")
        func()
    return shoes

@make_dress
@make_shoes
def out():
    print("我出門了")

@make_shoes
def out2():
    print("我出門了")

#john = make_dress(make_shoes(out))
john = out
john()

tom = out2
tom()