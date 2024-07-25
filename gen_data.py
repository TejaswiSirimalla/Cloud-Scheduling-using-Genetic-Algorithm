import random
import sys
r = int(sys.argv[1])
c = int(sys.argv[2])
f = sys.argv[3]

b=[0]*c#b=[0,0,0,0,.....c times]
b=[b]*r

o = open(f,"w")
for i in range(r):
  s=[]
  for j in range(c):
    s+=[random.randint(1,1000)]
  s=[str(k) for k in s]
  s = ' '.join(s)
  o.write(s+"\n")

#execution
#python gen_data.py rows columns outputfile.txt
#python gen_data.py tasks processors outputfile.txt
