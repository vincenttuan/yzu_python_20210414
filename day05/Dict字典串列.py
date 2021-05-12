# dict 是 key:value 的組合數組
salary = {'John': 50000, 'Mary': 60000}
print(salary)
print('John 的薪資:', salary['John'])
for key in salary:
    print("%s 的薪資 %d" % (key, salary[key]))

# 新增元素
salary.setdefault('Bob', 70000)
print(salary)

# 求薪資總和
sum = 0
for key in salary:
    sum = sum + salary[key]
print(sum)
