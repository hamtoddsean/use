import json
import os
import time
clist=[]
pathh='fule.json'
if not os.path.exists(pathh):
  with open(pathh,'w') as dou:
    douu=json.dump(clist,dou)


for i in range(600):
  time.sleep(1)
  with open(pathh,'r') as d:
    g=json.load(d)
    #print(g)
    g.append(2)
    with open(pathh,'w') as gc:
      json.dump(g,gc)
