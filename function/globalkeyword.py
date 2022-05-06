def fun1():
    a=10
    global b
    b=20
    print(a)
    print(b)
    
def fun2():
    print(b)
fun1()
fun2()