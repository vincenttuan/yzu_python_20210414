# 數組: list(元素可重複), set(元素不可重複), dict(key/value)
scores = [100, 90, 80]  # list
scores.append(70)
print(scores)
print(scores[1])  # 取得維度=1的資料(維度是從0開始)
print(len(scores))  # 取得元素個數
print(scores.index(80)) # 取得某元素的維度值
print(max(scores), min(scores)) #取得元素最大最小值
# 走訪每一個元素 I
for x in scores:
    print(x)
# 走訪每一個元素(含維度值) II
for (idx, value) in enumerate(scores):
    print(idx, value)