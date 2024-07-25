import tkFileDialog
import os
from Tkinter import *

def disTxtFieldrl(f,array):
  t = Text(f,width=100,height=20)
  t.pack(side=LEFT)
  yscroll = Scrollbar(f,command=t.yview)
  t.configure(yscrollcommand = yscroll.set)
  yscroll.pack(side = LEFT, fill = Y)
  for i in array:
    t.insert(END,str(i)+'\n')
  t.config(state=DISABLED)
  

def ret_f_path(f):
  s = list(f)
  s.reverse()
  s = ''.join(s)
  a = s[s.find('/')+1:]
  a = list(a)
  a.reverse()
  a = ''.join(a)
  return a

def quit(self):
  self.root.destroy()


def a():
  #to open fileDialog# select file button
  global testpath
  s = tkFileDialog.askopenfile(parent=root,mode='rb',title='select file')
  testpath = str(s)[13:-31]+'.txt'
  e1.set(testpath)

def b():
   #schedule button
   global o
   global oo
   global root
   #o = str(e2.get())
   oo = str(e1.get())
   print "oo = ",oo
   d = ret_f_path(oo)
   k = "python m_con*.py '/"+str(oo[:-4])+"'"+" & "+"python3 plot.py"
   os.system(k)
   newfil = open("/"+oo[:-8]+"_res.txt","r")
   newfil = newfil.read()
   newfil = newfil.split("\n")
   gh = Frame(root,width=800, height=50)
   disTxtFieldrl(gh,newfil)
   gh.pack()
   # to stop removing file comment below statement
   os.system("rm '/"+oo[:-8]+"_res.txt'")
   g = Frame(root,width=800, height=50)
   Button(g,text="scheduling successful\n(Press to exit)",command = c).pack(side=LEFT)
   g.pack()

def c():
  root.destroy()

root = Tk()
root.title("Cloud Scheduling using Genetic algorithm")

o=""
oo=""
testpath=""
f = Frame(root,width=800,height=50)
Label(f,text="select file : ").pack(side=LEFT,padx=5,pady=40)
e1 = StringVar()
Entry(f,width=40,textvariable=e1).pack(side=LEFT)
Button(f,text="choose file",command = a).pack(side=LEFT)
f.pack()

f3 = Frame(root, width=800, height=50)
Button(f3,text="schedule",command = b).pack(side=LEFT)
f3.pack()
root.mainloop()
os.system("rm example.txt")
