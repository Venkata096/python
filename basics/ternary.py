# wap to print min number among 3 numbers
a = int(input("enter number:"));
b = int(input("enter number:"));
c = int(input("enter number:"));
min = a if a<b and a<c else b if b<c else c

print("minimum number:" ,min)