class Person:
    name = ''
    sex = ''
    age = 0


# python 的主程式
#print(__name__)
if __name__ == '__main__':
    p1 = Person()
    p1.name = 'Vinent'
    p1.sex = '男'
    p1.age = 18
    p2 = Person()
    p2.name = 'Anita'
    p2.sex = '女'
    p2.age = 19
    print(p1, p2)
