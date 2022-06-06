class car:
    wheels = 4
    def __init__(self):
        pass
    def service(self):
        pass
    @classmethod
    def drive(cls,cname):
        print('{} has {} wheels'.format(cname,cls,cname))
    @staticmethod
    def m1():
        pass
    
car.drive("benz")
car.drive("audi")