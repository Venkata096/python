class car:
    def __init__(self,name,model,color):
        self.cname = name
        self.cmodel = model
        self.color = color
    def carDetails(self):
        print('car name:{},model:{},color{}'.format(self.cname,self.cmodel,self.color))
        
class user:
    def __init__(self,name,age,car):
        self.name = name
        self.age = age
        self.car = car
    def userDetails(self):
        print('{} has {} car'.format(self.name,self.car.cname))
        self.car.carDetails()
        
c1 = car("audi","q7","black")
u = user("ksk",19,c1)
u.userDetails()