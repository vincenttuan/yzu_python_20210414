# 裝飾器 2

def login(func, password):
    def check():
        if(password == 1234):
            print("登入成功")
            func()
        else:
            print("登入失敗")
            return None
    return check

def report():
    print("密件: 解禁日期 6.29")

#watch = login(report, 1234)
watch = login(report, int(input('請輸入密碼: ')))
watch()