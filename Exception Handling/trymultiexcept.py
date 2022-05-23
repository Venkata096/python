try:
    a = int(input("enter number:"))
    b = int(input("enter number:"))
    print(a/b)
    print("gm")
except zerodivisionerror as err:
    print(err)