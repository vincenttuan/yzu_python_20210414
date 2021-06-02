def check_score(score):
    if score >= 60:
        return "Pass"
    else:
        return "Fail"

score = 70
result = check_score(score)
print(result)
print(check_score(score))

result = "Pass" if score >= 60 else "Fail"
print(result)

result = lambda x : "Pass" if x >= 60 else "Fail"
print(result(score))

temp = lambda : print("24.5度")
temp()