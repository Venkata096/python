try:
    f = open('abc.txt')
    data = f.read()
    print(data)
    f.close()
except filenotfounderror as err:
    f = open('abc,txt')
    data = f.read()
    print(data)