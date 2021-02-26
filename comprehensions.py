# 12


# (1)
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)

convert_lst = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(convert_lst)


# (2)
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
convert_comprehension = []
for num in range(10):
    if num % 2 == 0:
        convert_comprehension.append(num // 2)
    else:
        convert_comprehension.append(num * 10)

print(convert_comprehension)

# (3)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)

# (4)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)

# (5)
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}

# (6)
dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}