import matplotlib.pyplot as p
import matplotlib.animation as anim
from matplotlib import style
import os
style.use("fivethirtyeight")
d = p.figure("Cloud Scheduling using Genetic Algorithm - Graph")
u = d.add_subplot(1,1,1)
def a(n):
  if(os.path.exists("example.txt")==False):
    f = open("example.txt","w")
    f.close()
  f = open("example.txt","r").read()
  l = f.split("\n")
  x = []
  y = []
  for i in l:
    if len(i)>1:
      a,b = i.split(",")
      x+=[a]
      y+=[b]
  u.clear()
  u.plot(x,y)
an = anim.FuncAnimation(d,a,interval=1000)
p.show()
