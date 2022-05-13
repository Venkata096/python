def verify(pro):
    def inner(name):
        if name=="anupama":
            print("hello darling,how are you")
        else:
            pro(name)
    return inner
            
@verify
def employee(name):
    print("hello",name,"gm")
employee("angel")
employee("sai")
employee("mahesh")                                   