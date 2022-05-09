'''
def fact(n):
    i = 1
    while n >= 1:
        i =i*n
        n =n-1
        return i
result = fact(10)
print(result)
'''
def fact(n):
    i = 2
    while n >= 2:
        i = i+n
        n = n+2
        return i
result = fact(100)
print(result)

def fact(n):
    i=3
    while n <= 3:
        i = i-1
        n = n-3
        return i
result = fact(99)
print(result)