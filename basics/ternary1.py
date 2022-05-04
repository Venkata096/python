a = int(input("enter number:"));
b = int(input("enter number:"));
c = int(input("enter number:"));
max = a if a>b and a>c else b if b>c else c
print("maximum number:" ,max)