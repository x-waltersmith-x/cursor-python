# 5, 6, 7, 8, 9, 10, 11 tasks

apples = "eleven"
peaches = "seven"
fruits = {"apples": apples, "peaches": peaches}

print("Anna has {} apples and {} peaches.".format(11, 7))
print("Anna has {fruits['apples']} apples and {fruits['peaches']} peaches.")
print("Anna has {apples:.5} apples and {peaches:.3} peaches.".format(apples, peaches))
print(f"Anna has %s apples and %s peaches." % (apples, peaches))
