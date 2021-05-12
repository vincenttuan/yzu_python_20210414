e1 = {'name': 'John', 'salary': 50000, 'program': ['HTML', 'JS']}
e2 = {'name': 'Mary', 'salary': 60000, 'program': ['HTML', 'Python']}
e3 = {'name': 'Bob', 'salary': 70000, 'program': ['Java', 'Python', 'C#']}
# 請求出會 python 的員工人名, 並將放入到 names = [] 中
emps = [e1, e2, e3]
target = 'Python'
names = []
for emp in emps:
    # print(emp['name'], emp['program'])
    for p in emp['program']:
        if p == target:
            #print(emp['name'], p)
            names.append(emp['name'])

print(names)