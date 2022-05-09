'''
def is_odd(num):
    if num % 2 != 0:
        return True
    else:
        return False
    
l1 = [1,2,33,66,88,77,99,22]
l2 = list(filter(is_odd,l1))
print(l1)
print(l2)
'''
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
l1 = [2,4,6,8,10,3,5,7,9,1]
l2 = list(filter(is_even,l1))
print(l1)
print(l2)