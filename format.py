# 5, 6, 7, 8, 9, 10, 11 tasks

apples = "eleven"
peaches = "seven"
fruits = {"apples": apples, "peaches": peaches}

# 5
print("5) Anna has {} apples and {} peaches.".format(11, 7))
# 6
print("6) Anna has {0} apples and {1} peaches.".format(apples, peaches))
# 7
print("7) Anna has {apples} apples and {apples} peaches.".format(apples=apples, peaches=peaches))
# 8
print("8) Anna has {0:.5} apples and {1:.3} peaches.".format(apples, peaches))
# 9, 10 tasks
print(f"9-10) Anna has %s apples and %s peaches." % (apples, peaches))
# 11
print("11) Anna has {apples} apples and {peaches} peaches.".format(**fruits))
