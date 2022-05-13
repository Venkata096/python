def simple_sub(func):
    def  inner(a,b):
        if b == 0:
            print("cannot sub with zero")
        else:
            return func(a,b)
        return inner
    
@simple_sub
def sub (a,b):
    return a-b

print(10,50)

