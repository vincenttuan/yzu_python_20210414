'''
python 裡沒有 switch
A123456789 (1:男生, 2:女生)
sex = 1
switc(sex) {
    case 1:
        print("男生");
        break
    case 2:
        print("女生");
        bbreak;
}

lambda 與 dict 的合作
'''
sex = 1
sex_info = {1: lambda :print("男"), 2 : lambda :print("女")}
sex_info.get(sex)()

sex = 2
sex_info = {
                1 : lambda money :print("男", money),
                2 : lambda money :print("女", money * 1.2)
           }
sex_info.get(sex)(10000)

sex = 3
sex_error = lambda money : print("性別錯誤", 0)
sex_info = {
                1 : lambda money :print("男", money),
                2 : lambda money :print("女", money * 1.2)
           }
sex_info.get(sex, sex_error)(10000)