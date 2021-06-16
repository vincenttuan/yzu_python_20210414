class Person:  # 類別, 物件的規格書(藍圖)
    name = ''  # 屬性(物件變數)
    sex  = ''
    age  = 0


# python 的主程式
#print(__name__)
if __name__ == '__main__':
    p1 = Person()  # 建立物件
    p1.name = 'Vinent'  # 設定物件變數/屬性內容
    p1.sex  = '男'
    p1.age  = 18
    p2 = Person()
    p2.name = 'Anita'
    p2.sex = '女'
    p2.age = 19
    print(p1, p2)
    print(p1.name, p1.sex, p1.age)
    print(p2.name, p2.sex, p2.age)