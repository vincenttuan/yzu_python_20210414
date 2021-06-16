class Salary:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, amount):  # +
        if amount > 0:
            self.salary = self.salary + amount

    def __str__(self) -> str:
        return self.name + " $" + str(self.salary)


if __name__ == '__main__':
    mary = Salary('Mary', 40000)
    print(mary)
    # 加薪 5000
    mary + 5000
    print(mary)