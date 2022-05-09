'''
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
l1 = [1,3,4,5,8]
l2 = list(filter(is_even,l1))
print(l1)
print(l2)
'''
def is_odd(num):
    if num % 2 != 0:
        return True
    else:
        return False
l1 = [1,2,3,4,5,6,7,8,9]
l2 = list(filter(is_odd,l1))
print(l1)
print(l2)