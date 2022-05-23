try:
    a = int(input("enter number:"))
    b = int(input("enter number:"))
    print(a/b)
except valueerror as err1:
    print(err1)
except zerodivisionerror as err2:
    print(err2)