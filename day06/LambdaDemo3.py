# 利用 lambda 判斷 odd 奇數, even 偶數

# def check(n):
#     if n % 2 == 0:
#         return "even"
#     else:
#         return "odd"

# def check(n):
#     return "even" if n % 2 == 0 else "odd"

# def printResult(result):
#     print(result)

result      = lambda n : "even" if n % 2 == 0 else "odd"
printResult = lambda r : print(r)
printResult(result(43))