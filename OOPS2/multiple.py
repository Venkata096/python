class F:
    def m1(self):
        print("father class - m1 method")
class M:
    def m1(self):
        print("mother class - m1 method")

class c(F,M):
    def m2(self):
        print("child class - m2 method")
        
c = c()
c.m1()
c.m2()