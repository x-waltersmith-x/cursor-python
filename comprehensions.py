# 12, 13, 14, 15, 16, 17


# (1)
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
convert_list = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst)
print(convert_list)


# (2)
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
convert_comp = []
for num in range(10):
    if num % 2 == 0:
        convert_comp.append(num // 2)
    else:
        convert_comp.append(num * 10)
print(list_comprehension)
print(convert_comp)


# (3)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
d_comp = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(d)
print(d_comp)


# (4)
d_2 = {}
for num in range(1, 11):
    if num % 2 == 1:
        d_2[num] = num ** 2
    else:
        d_2[num] = num // 0.5
d_2_comp = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(d_2)
print(d_2_comp)


# (5)
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
dict_reg = {}
for x in range(10):
    if x**3 % 4 == 0:
        dict_reg[x] = x**3
print(dict_comprehension)
print(dict_reg)


# (6)
dict_2_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
dict_2_reg = {}
for x in range(10):
    if x**3 % 4 == 0:
        dict_2_reg[x] = x**3
    else:
        dict_2_reg[x] = x
print(dict_2_comprehension)
print(dict_2_reg)