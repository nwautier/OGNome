from ast import Return
import random as rng

marker=["a","b","c","d","A","B","C","D"]
p1=[] #Parent1
p2=[] #Parent2
c=[] #Child

numMarkers=10 #Number of markers
TwinProb=2.5 #Probability of Twin Births
MutationProb=0.5 #Probability of Mutation

#def twinCheck():
#    if rng.randint(1,100) <= TwinProb:
#        return True
#    else:
#        return False

def randomizeP1():
    p1.clear()
    p1.append("Parent 1")
    for i in range(numMarkers):
        p1.append(marker[rng.randint(0, len(marker)-1)])
def randomizeP2():
    p2.clear()
    p2.append("Parent 2")
    for i in range(numMarkers):
        p2.append(marker[rng.randint(0, len(marker)-1)])


def makeChild(p1, p2):
 c.clear()
 c.append("Child 01")
 for i in range(1, len(p1)):
  if rng.randint(0, 1) == 0:
   c.append(p1[i])
  else:
   c.append(p2[i])
   if rng.randint(0, 99) <= MutationProb:
    c[i] = "M"
    #c[i] = marker[rng.randint(0, len(marker)-1)]
#    if twinCheck():
#        c.append("Twin of " + c[0])

def OutputFamily():
    print("Family:")
    print(p1)
    print(p2)
    print(c)

#program starts here
randomizeP1()
randomizeP2()
makeChild(p1, p2)
OutputFamily()