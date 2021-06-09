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

def out():
    print("我出門了")


john = make_dress(out)
john()