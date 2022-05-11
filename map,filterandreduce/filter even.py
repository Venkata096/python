def even_num(x):
    if x % 2 == 0:
        return True
    else:
        return False
obj = filter(even_num,range(0,19))
even = list(obj)
print(even)