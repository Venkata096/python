class test:
    def __init__(self):
        print("constructor method execute first")
    def m1(self):
        print("method -m1()")
    def m2(self):
        print("method -m2()")
t1 = test()
t2 = test()
t3 = test()
t1.m1()
t2.m2()