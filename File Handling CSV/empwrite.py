import csv
f = open('cpemp.csv','w',newline="")
csvobj = csv.writer(f)
csvobj.writerow(["eno","ename","salary"])
n = int(input("enter no of employees:"))
for x in range(n):
    eno = int(input("enter employee eno:"))
    ename = input("enter employee ename:")
    esal = int(input("enter salary:"))
    csvobj.writerow([eno,ename,esal])
    
f.close()