class Father:
    amount = 0

    def __init__(self, amount) -> None:
        self.amount = amount

    def __str__(self) -> str:
        return "amount: " + str(self.amount)


class Son(Father):
    age = 0

    def __init__(self, amount, age) -> None:
        super().__init__(amount)  # Father.__init__(self, amount)
        self.age = age

    def __str__(self) -> str:
        return super().__str__() + " age: " + str(self.age)


if __name__ == '__main__':
    son = Son(5000, 18)
    print(son)