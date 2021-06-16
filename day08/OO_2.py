class Account:
    name = ''  # 公有變數
    __balance = 100  # 私有變數

    def addBalance(self, amount):
        if(amount > 0):
            self.__balance = self.__balance + amount

    def __str__(self):
        return self.name + " 有 $" + str(self.__balance)


if __name__ == '__main__':
    acc1 = Account()
    acc1.name = 'Vincent'
    #acc1.__balance = -200
    #acc1.addBalance(-200)
    acc1.addBalance(200)
    print(acc1)