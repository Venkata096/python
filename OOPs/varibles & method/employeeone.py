class Employee:
    def __init__(self,id):
        self.eid = id
    def setName(self,name):
        self.ename = name
        
e1 = Employee(101)
e1.setName("rupesh")
e1.sal = 450000
print(e1.__dict__)
print("****")
e2 = Employee(102)
e2.setName("naveen")
e2.sal = 550000
print(e2.__dict__)