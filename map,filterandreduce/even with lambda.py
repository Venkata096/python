print(list(filter(lambda x: x % 2 == 0 , range(0,19))))
obj = filter(lambda x: x % 2 == 0 , range(0,19))
l1 = list(obj)
print(l1)