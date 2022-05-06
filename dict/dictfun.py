emp = {'id':101,'name':"rahul",'sal':45000}
print(emp.get('id'))
print(emp.get('loc'))
print(emp.get('loc','nodia'))

print(emp.keys())
for k in emp.keys():
    print(k)
    
print(emp.values())
for v in emp.values():
    print(v)
    
print(emp.items())