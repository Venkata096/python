import csv
f = open('emp.csv','r')
csvobj = csv.reader(f)
data = list(csvobj)
print(data)

for line in data:
    for x in line:
        
        print(x,"\t",end="")
    print()
    
f.close()