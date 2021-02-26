# 20, 21, 22, 23, 24, 25, 26, 27


# 20, 21
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort_rev = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort.sort()
lst_to_sort_rev.sort(reverse=True)
print(lst_to_sort)
print(lst_to_sort_rev)


# 22
print(list(map(lambda x: x * 2, lst_to_sort)))

# 23
list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_A.sort()
list_B.sort(reverse=True)
print(list(map(lambda a: a * 2, list_A)))
print(list(map(lambda b: b * 2, list_B)))