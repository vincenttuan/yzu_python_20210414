file = open('salary.txt', 'r', encoding='UTF-8')
# content = file.read()
# print(type(content), content)

# row = file.readline()
# print(type(row), row)

rows = file.readlines()
print(type(rows), rows)
print(rows[0].strip('\n'))  # 去除 \n