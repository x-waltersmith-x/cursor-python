# 5, 6, 7, 8, 9, 10, 11 tasks

apples = "eleven"
peaches = "seven"
fruits = {"apples": apples, "peaches": peaches}

# 5
print("Anna has {} apples and {} peaches.".format(11, 7))
# 6
print("Anna has {0} apples and {1} peaches.".format(apples, peaches))
# 7
print("Anna has {apples} apples and {apples} peaches.".format(apples = apples, peaches = peaches))
# 8
print("Anna has {0:.5} apples and {1:.3} peaches.".format(apples, peaches))
# 9, 10 tasks
print(f"Anna has %s apples and %s peaches." % (apples, peaches))
# 11
print("Anna has {apples} apples and {peaches} peaches.".format(**fruits))
