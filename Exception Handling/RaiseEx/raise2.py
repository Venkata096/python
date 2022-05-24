class GetMarrySoon(Exception):
    def __init__(self,arg):
        self.msg = arg
age = int(input("enter your age:"))
try:
    if age > 25:
        print("eligible for marriage")
    else:
        raise GetMarrySoon("not eligible for marriage")
except GetMarrySoon as sk:
    print(sk)
    