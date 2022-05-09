'''
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
l1 = (10,2,3,4,5,6,7,9,8)
x = filter(is_even,l1)
print(x)
l2 = list(filter(is_even,l1))
print(l1)
print(l2)
'''
def is_odd(num):
    if num % 1 != 0:
        return True
    else:
        return False
l1 = [10,20,30,40,50]
a = filter(is_odd,l1)
print(a)
l2 = list(filter(is_odd,l1))
print(l1)
print(l2)