# @裝飾器 + 參數 4

def login(password):
    def decorated(func):  # func = 要被裝飾的方法
        def check():
            if(password == 1234):
                print("登入成功")
                func()
            else:
                print("登入失敗")
                return None
        return check
    return decorated

@login(password=1234)
def report():
    print("密件: 解禁日期 6.29")

watch = report
watch()