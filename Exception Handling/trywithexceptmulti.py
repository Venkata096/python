try:
    a = int(input("enter number:"))
    b = int(input("enter number:"))
    print(a/b)
except (valueerror,zerodivisionerror,nameerror) as err:
    print(err)