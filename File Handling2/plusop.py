f = open('abc.txt','a+')
f.write("good morning")
data = f.read()
print(data)
f.close()