n = int(input("enter no of empolyes"))
emp = {}
i=1
while i<=n:
    ename = input("enter empolyes:")
    salary = int(input("enter salary:"))
    emp[ename] = salary
    i=i+1
    
print(emp)
    
for k in emp:
    print(k,":",emp[K])