import day08.OO_6 as o

if __name__ == '__main__':
    jane = o.Salary('Jane', 40000);
    helen = o.Salary('Helen', 40000);
    jack = o.Salary('Jack', 50000);
    boss = o.Salary('Boss', 0);

    # 進行比較
    print(jane == helen)
    print(helen < jack)
    print(helen == jack)
    print(jane > jack)
