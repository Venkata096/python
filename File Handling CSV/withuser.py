import csv
f = open('user,csv','w')
csvobj = csv.writer(f)
csvobj.writerow(["eno","ename","salary"])
f.close()