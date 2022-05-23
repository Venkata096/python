a = int(input("enter number:"))
b = int(input("enter number:"))
try:
    print(a/b)
except zerodividionerror:
    print(a/1)