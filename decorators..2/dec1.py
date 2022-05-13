def verify(func):
    def inner(name):
        if name == "modi":
            print("hi how r u ")
        else:
            func(name)
    return inner
@verify

def employee(name):
    print("hello",name,"gm")
employee("anupama")
employee("sonia")
employee("lenovo")