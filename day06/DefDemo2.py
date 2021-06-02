def get_sum(*score):
    print(type(score), score)
    return sum(score)

print(get_sum(10, 20, 30))
print(get_sum(10))
print(get_sum())
print(get_sum(10, 3.14))