class Account:
    name = ''  # 公有變數
    __balance = 100  # 私有變數
    __password = ''

    def __init__(self, name, amount, password):
        self.name = name
        self.addBalance(amount)
        self.__password = password

    def addBalance(self, amount):  # 存款
        if(amount > 0):
            self.__balance = self.__balance + amount
            return True
        else:
            return False

    def subBalance(self, amount):  # 提款
        if (amount > 0 and amount <= self.__balance):
            self.__balance = self.__balance - amount
            return True
        else:
            return False

    def getBalance(self, password):  # 查詢餘額
        if(self.__password == password):
            return self.__balance
        else:
            print("密碼不正確")
            return None

    # 轉帳
    def transfer(self, acct, amount):
        status = self.subBalance(amount) # 提出
        if(status):  # if(status == True)
            acct.addBalance(amount) # 存入

    def __str__(self):
        return self.name + " 有 $" + str(self.__balance)


if __name__ == '__main__':
    # acc1 = Account()
    # acc1.name = 'Vincent'
    # #acc1.__balance = -200
    # #acc1.addBalance(-200)
    # acc1.addBalance(200)
    # print(acc1)

    # acc2 = Account('Anita', 5000, '1234')
    # print('Balance $', acc2.getBalance('1234'))
    # acc2.subBalance(700)
    # print('Balance $', acc2.getBalance('1234'))
    # print(acc2)

    a = Account('Anita', 5000, '1234')
    b = Account('Bob', 1000, '5678')
    print(a, b)
    a.transfer(b, 1500)
    print(a, b)