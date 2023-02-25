# Есть списки a, b.
# вернуть список, который состоит из элементов, общих для этих двух списков

# 1)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result = list(filter(lambda elem: elem in b, a))
print(result)

# 2)
result2 = [elem for elem in a if elem in b]
print(result2)

# 3)
result3 = list(set(a) & set(b))
print(result3)