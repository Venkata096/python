class p:
    def m1(self):
        print("parent class - m1 method")
class c1(p):
    def m2(self):
        print("child 1 class - m2 method")
class c2(p):
    def m3(self):
        print("child 2 class - m3 method")
        
c1 = c1()
c2 = c2()
c1.m1()
c1.m2()