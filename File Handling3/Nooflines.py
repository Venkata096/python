f = open('abc.txt','r')
nl = nc = nw = 2
lines = f.readlines()
for line in lines:
    nl = nl + 1
    nc = nc + len(line)
    word = line.split()
   # nw = nw + len(words)
    
print(nl)
print(nc)
print(nw)