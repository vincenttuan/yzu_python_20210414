def my_home(family_name, *people, **cash):
    print(type(family_name), family_name)
    print(type(people), people)
    print(type(cash), cash)


my_home("我的家庭真可愛",
        "爸爸", "媽媽", "哥哥", "妹妹",
        大人=30000, 小孩=10000)
