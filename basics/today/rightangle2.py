n = int(input("enter number:"))
for i in range(n):
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()