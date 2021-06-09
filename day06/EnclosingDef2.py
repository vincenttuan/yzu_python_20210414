# 嵌套含式 II

def calc_bmi(h, w):
    if h <= 0 and w <= 0:
        return False

    def get_bmi():
        bmi = w / ((h/100)**2)
        return bmi

    return get_bmi

def compare_bmi(a, b):
    print(a(), b(), a() > b())

bmi1 = calc_bmi(170, 60)
bmi2 = calc_bmi(180, 90)
compare_bmi(bmi1, bmi2)
