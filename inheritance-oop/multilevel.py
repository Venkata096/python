class parent:
    def m1(self):
        print("parent class - m1() method")
        
class child(parent):
    def m2(self):
        print("child class - m2 () method")
        
class grandchild(child):
    def m3(self):
        print("grandchild class - m3() method")
        
obj = grandchild()
obj.m1()
obj.m2()
obj.m3()