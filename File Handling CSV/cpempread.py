import csv
f = open('cpemp.csv','r')
data = csv.reader(f)
print(data)

for line in list(data):
    for x in line:
        print(x,"\t",end="")
    print()