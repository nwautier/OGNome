from ast import Return
import random as rng

marker=["a","b","c","d","A","B","C","D"]
p1=[] #Parent1
p2=[] #Parent2
c=[] #Child

numMarkers=23 #Number of markers
TwinProb=2.5 #Probability of Twin Births

#def twinCheck():
#    if rng.randint(1,100) <= TwinProb:
#        return True
#    else:
#        return False

def randomizeParent(parent_list, name, numMarkers):
 parent_list.clear()
 parent_list.append(name)
 for i in range(numMarkers):
  parent_list.append((rng.choice(marker), rng.choice(marker)))

def makeChild(p1, p2):
 c.clear()
 c.append("Child of " + p1[0] + " and " + p2[0])
 for i in range(1, len(p1)):
  if rng.randint(0, 1) == 0:
   c.append(p1[i])
  else:
   c.append(p2[i])
#    if twinCheck():
#        c.append("Twin of " + c[0])