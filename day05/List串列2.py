scores = [100, -10, -20, 90, -80, 999]
print(scores)
# error_score = scores.pop(1)
# print(error_score, scores)
# error_score = scores.pop(3)
# print(error_score, scores)

# 利用 pop() 將不合法的分數挑出
error_scores = []
for s in scores:
    if s < 0 or s > 100:
        error_scores.append(s)

print(scores)
print(error_scores)
for e in error_scores:
    scores.pop(scores.index(e))

print(scores)
