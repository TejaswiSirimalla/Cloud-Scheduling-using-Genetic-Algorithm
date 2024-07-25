import random
import math
import sys


##############################################    converting data into matrix    #####################################


maximum = 99999

#storing data
f = open(sys.argv[1],"r")
f = f.read()
f = f.split("\n")
while("" in f):
  f.remove("")
n = len(f)
nt = n
np = f[0].count(" ")+1
s=[]
for i in f:
  s+=[i.split(" ")]
c=[]
for i in s:
  temp=[]
  for j in i:
    temp+=[float(j)]
  c+=[temp]

d=c[:]
print "np = ",np
print "nt = ",nt



################################################		defining functions		############################################

# description of function:evalcost
# c = costmatrix; l = candidate for which cost has to be evaluated
def evalcost(c,l):
  global np
  temp={}
  for i in range(np):
    temp[i]=0
  m = len(l) #no. of tasks #l is candidate
  for i in range(m):
    temp[l[i]]+=c[i][l[i]]
  cos = [temp[i] for i in range(np)]
  return max(cos) 


def mutate(x,np): # x is the whole population  # np is the number of processors
  nx=[]
  q=len(x)
  for i in x:
    if(random.randint(0,100)/100.0<0.5):
      l = len(i)
      for j in range(l/7):
        # s is index position for insertion of processor
        s = random.randint(0,l-2)
        p1=i[:s]+[random.randint(0,np-1)]
        p2=i[s+1:]
        nx+=[p1+p2]
    else:
        nx+=[i]
  return nx


def ssort(x,cx):
  nx=x[:]
  ncx=cx[:]
  nxlen=len(nx)
  sx = []
  scx=[]
  for i in range(nxlen):
    mn = min(ncx)
    ind = ncx.index(mn)
    sx+=[nx[ind]]
    scx+=[ncx[ind]]
    nx.remove(nx[ind])
    ncx.remove(ncx[ind])
  return sx,scx


def to(a,b):
  xlen = len(a)-1
  t1 = random.randint(0,xlen)
  t2 = random.randint(0,xlen)
  while(t1==t2):
    t2 = random.randint(0,xlen)
  if(t1>t2):
    t1,t2 = t2,t1
  a1 = a[:t1]+b[t1:t2]+a[t2:]
  b1 = b[:t1]+a[t1:t2]+b[t2:]
  return a1,b1

def work(x):
  try:
    f = open("example.txt","a")
    f.write(x)
    f.close()
  except IOError:
    f = open("example.txt","w")
    f.write(x[1:])
    f.close()

####################################################		core		#####################################################





pop=[]
#initial population generation
if(nt<10 or nt>=10):
  popsize=20
  i=0
  while(i<popsize):
    cand = []
    for j in range(nt):
      cand+=[random.randint(0,np-1)]
    cand=tuple(cand)
    if cand not in pop:
      pop+=[cand]
      i+=1


p=list(set(pop))

pop=[list(i) for i in p]

print len(pop)

x = [i for i in pop]
cx =[evalcost(d,i) for i in pop]


xlen = len(x)

nnx = x[:]
print "evaluating cost"
ncx =[evalcost(d,i) for i in nnx]

print "evaluating sort\n"
px=ssort(nnx,ncx)

uni_niters=0

def ga(x,cx,niters,f):
  global uni_niters
  global pop
  global popsize
  global np
  npp = int(np)
  while(1):
    if(f>=50 and niters>=10):
      return x,cx
    else:
      mincx = min(cx)
      print "iteration count = ",uni_niters+1
      uni_niters+=1
      cx = [evalcost(d,i) for i in x]
      tx = {}
      i=0
      xlen = len(x)
      for i in range(xlen):
        tx[tuple(x[i])]=cx[i]
      nx =[x[i] for i in range(xlen)]
      ncx =[evalcost(c,i) for i in tx]
      i=0
      #p = ssort(tx,tcx)
      #nx=p[0]#sorted candidates
      #ncx = p[1]#sorted candidate costs
      nx=[nx[0]]+nx[:-1]#superior candidate survival #11234
      ncx=[ncx[0]]+ncx[:-1]
      nxlen= len(nx)
      n_par = nxlen/2  #n_par = no. of parents
      
      
      #parent selection
      #=================
      par=[]#parents list
      #nonpar = nx[:]
      newsum = sum(ncx)
      #fitness=[float(i)/newsum for i in ncx]
      zz=0
      while(zz<n_par):#for i in range(nxlen/2):
        #tournament selection
        rsample=[]
        ch=0
        while(ch<3):
          te=random.randint(0,nxlen-1)
          if te not in rsample:
            rsample+=[te]
            ch+=1
        newc=[ncx[h] for h in rsample]
        solu = nx[rsample[newc.index(min(newc))]]
        if solu not in par:
          par+=[solu]
          zz+=1
      nonpar=[]
      for i in nx:
        if i not in par:
          nonpar += [i]
      crossed = []
      print "performing crossover"
      for i in nonpar:
        for j in par:
          rr = to(i,j)#performing two point crossover
          t1=rr[0]
          t2=rr[1]
          crossed+=[t1,t2] #list of all crossed candidates
      x = crossed[:]
      cx =[evalcost(d,i) for i in x]
      mx=mutate(x,npp)#npp=no. of processors
      mcx =[evalcost(d,i) for i in mx]
      x=nx+mx
      cx=ncx+mcx
      anss = min(cx)
      print "Best local optimum = ",anss,"\n"#"\t\n\t\n\n",len(x),len(cx)
      plotdata=str(uni_niters)+","+str(anss)+"\n"
      work(plotdata)
      if(min(cx)==mincx):
        f+=1
      else:
        f=0
      print "======= updating population ======"
      xlen = len(x)
      #updating population
      po={}
      for i in range(xlen):
        po[tuple(x[i])] = cx[i]
      nx=po.keys()
      ncx=[po[i] for i in nx]
      nx=[list(p) for p in nx]
      p=ssort(nx,ncx)
      nx = p[0]
      ncx = p[1]
      n1=20
      x = nx[:n1]
      cx = ncx[:n1]
      niters+=1


x = px[0]
cx=px[1]
res = ga(x,cx,nt,0)
print res[0]
print res[1]

x=res[0][0]
cx = res[1][0]
outputfile = sys.argv[1][:-4]+"_res"+sys.argv[1][-4:]
resfile = open(outputfile,"w")
tempstmt = "===================================="
resfile.write(tempstmt+"\n")
print tempstmt
tempstmt =  "\tresult\n===================================="
resfile.write(tempstmt+"\n")
print tempstmt

tempstmt="tasks\tprocessor\tcost\n------------------------------------"
resfile.write(tempstmt+"\n")
print tempstmt
for i in range(nt):
  tempstmt = str(i+1)+"\t"+str(x[i]+1)+"\t\t"+str(d[i][x[i]])
  resfile.write(tempstmt+"\n")
  print tempstmt

tempstmt = "====================================="
resfile.write(tempstmt+"\n")
print tempstmt

tempstmt="Best Local Optimum found = "+str(cx)
resfile.write(tempstmt+"\n")
print tempstmt
resfile.close()
