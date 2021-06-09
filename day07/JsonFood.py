import json
import requests

url = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'
data = json.loads(requests.get(url).text)
print(data)

# 資料整理
bad_foods = []
for d in data:
    food = {'品名': d.get('品名'), '不合格原因': d.get('不合格原因')}
    bad_foods.append(food)

print(bad_foods)

print()

for food in bad_foods:
    if '池上' in food['品名']:
        print(food)
