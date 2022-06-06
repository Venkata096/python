class bank:
    def setName(self,name):
        self.ename = name
    def getName(self):
        return self.name
c1 = bank()
c1.setName("ksk")
print(c1.getName)