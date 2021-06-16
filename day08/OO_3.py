class Human:
    name = ""
    sex = ""
    age = 0
    def __str__(self):
        return self.name + "," + self.sex + "," + str(self.age)

class Student(Human):  # Student 繼承 Human
    number = 0
    grade = ''
    def __init__(self, name, sex, age, number, grade):
        self.name = name
        self.sex = sex
        self.age = age
        self.number = number
        self.grade = grade
    def __str__(self):
        return self.name + "," + self.sex + "," + str(self.age) + "," + \
               str(self.number) + "," + self.grade

if __name__ == '__main__':
    s = Student('Vincent', '男', 18, 10, 'A+')
    print(s)

