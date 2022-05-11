def fun():
    print("fun")
a = fun
fun()
del fun
a()