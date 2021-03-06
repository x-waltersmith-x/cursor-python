# 18, 19

# (7)
def foo(x, y):
    if x < y:
        return x
    else:
        return y
lambda_foo = lambda x, y: x if x < y else y
print('BEFORE: ', foo(x=3, y=5), ' AND AFTER: ', lambda_foo(x=3, y=5))


#(8)
foo_2 = lambda x, y, z: z if y < x and x > z else y
def unlambda_foo_2(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y
print('BEFORE: ', foo_2(x=3, y=5, z=7), ' AND AFTER: ', unlambda_foo_2(x=3, y=5, z=7))