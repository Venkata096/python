def simple_multi(func):
    def inner(a,b):
        if b == 0:
            print("cannot multi zero")
        else:
            return func(a,b)
    return inner

@simple_multi
def multi(a,b):
    return a*b

print(multi(10,5))
print(multi(10,20))
