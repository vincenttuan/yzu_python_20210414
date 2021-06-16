class Account:
    name = ''  # 公有變數
    __balance = 100  # 私有變數
    __password = ''

    def __init__(self, name, amount, password):
        self.name = name
        self.addBalance(amount)
        self.__password = password

    def addBalance(self, amount):
        if(amount > 0):
            self.__balance = self.__balance + amount

    def getBalance(self, password):
        if(self.__password == password):
            return self.__balance
        else:
            print("密碼不正確")
            return None

    def __str__(self):
        return self.name + " 有 $" + str(self.__balance)


if __name__ == '__main__':
    # acc1 = Account()
    # acc1.name = 'Vincent'
    # #acc1.__balance = -200
    # #acc1.addBalance(-200)
    # acc1.addBalance(200)
    # print(acc1)

    acc2 = Account('Anita', 5000, '1234')
    print('Balance $', acc2.getBalance('1234'))
    print(acc2)