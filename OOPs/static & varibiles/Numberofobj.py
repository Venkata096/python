class test:
    count = 0
    def __init__(self):
        test.count = test.count + 1
        
    @classmethod
    def getNoOfObject(cls):
        print("No Of Object",cls.count)
t1 = test()
t2 = test()
test.getNoOfObject()
t3 = test()
test.getNoOfObject()