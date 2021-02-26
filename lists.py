# 20, 21, 22, 23, 24, 25, 26, 27
from functools import reduce

# 20, 21
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort_rev = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort.sort()
lst_to_sort_rev.sort(reverse=True)
print(lst_to_sort, ' AND ', lst_to_sort_rev)


# 22
print(list(map(lambda x: x * 2, lst_to_sort)))


# 23
list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_A.sort()
list_B.sort(reverse=True)
print(list(map(lambda a: a * 2, list_A)), ' AND ', list(map(lambda b: b * 2, list_B)))


# 24, 25
print(reduce(lambda a, b: a + b, lst_to_sort), ' AND ', list(filter(lambda x: x % 2 == 1, lst_to_sort)))


# 26
b = range(-10, 10)
print(list(filter(lambda x: x < 0, b)))


# 27
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
print('1) ', list(filter(lambda a: a % 2 == 1, list_1)),' 2)', list(filter(lambda b: b % 2 == 0, list_2)),' 3)', list(filter(lambda c: c in list_1, list_2)))
