# 5, 6, 7, 8, 9, 10, 11 tasks

apples = "eleven"
peaches = "seven"
fruits = {"apples": apples, "peaches": peaches}


print(f"Anna has {apples:.5s} apples and {peaches:.3s} peaches.".format(apples = apples, peaches = peaches))
print(f"Anna has %s apples and %s peaches." % (apples, peaches))
print(f"Anna has {fruits['apples']} apples and {fruits['peaches']} peaches.")