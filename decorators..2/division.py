def simple_div(func):
    def inner(a,b):
        if b == 0:
            print("cannot divide zero")
        else:
            return func(a,b)
    return inner

@simple_div
def divide(a,b):
    return a/b

print(divide(10,5))
print(divide(10,20))