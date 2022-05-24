class InsufficientFundsException(Exception):
    def __init__(self,arg):
        self.msg = arg
        
amount  = int(input("enter amount:"))
try:
    if amount > 500:
        print("go to movie")
    else:
        raise InsufficientFundsException("go to pg")
except InsufficientFundsException as msg:
    print(msg)