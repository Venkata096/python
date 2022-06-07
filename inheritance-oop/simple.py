class parent:
    def m1(self):
        print("instance method - parent")
    @classmethod
    def m2(cls):
        print("class method - parent")
    @staticmethod
    def m3():
        print("static method - parent")
        
class child(parent):
    def m4(self):
        print("instance method - child")
        
c = child()
c.m1()
c.m2()
c.m3()
c.m4()