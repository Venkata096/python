def verify(pubg):
    def inner(name):
        if name =="kiran":
            print("hello",name,"pm")
        else:
            pubg(name)
    return inner

@verify
def employee(name):
    print("hello",name,"gm")
employee ("rahul")
employee ("lokesh")
employee ("kiran")