# 嵌套含式

def message(text):
    text = text + " by 元智大學"

    def print_message():
        print(text)

    return print_message


def message2(text):
    text = text + " by 元智大學 II"

    def print_message():
        print(text)

    return print_message()  # 有 () 表示立即執行

m1 = message("Hello")
m1()

message2("Hello2")