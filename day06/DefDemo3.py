def print_score(**exam):
    #print(type(exam), exam)
    print_score2(exam)


def print_score2(exam):
    print(type(exam), exam)
    print(exam.keys(), exam.values())

# 國文=100, 數學=80, 英文=70
print_score(國文=100, 數學=80, 英文=70, 地理=60)

exams = {'國文': 100, '數學': 80, '英文': 70}
print_score2(exams)
