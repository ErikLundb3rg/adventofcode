from collections import defaultdict


def foldUp(mp, foldAtY):
  keys = list(mp.keys())
  for key in keys:
    x, y = key

    if y > foldAtY:
      dy = abs(y - foldAtY)
      newY = foldAtY - dy
      mp[(x, newY)] = 1
      del mp[(x, y)]
  
def foldLeft(mp, foldAtX):
  keys = list(mp.keys())
  for key in keys:
    x, y = key
    
    if x > foldAtX:
      dx = abs(x - foldAtX)
      newX = foldAtX - dx
      mp[(newX, y)] = 1
      del mp[(x, y)]
  
def getCount(mp):
  return len(list(mp.keys()))
  
  
def main():
  
  file = open("actual.in", "r")

  mp = defaultdict(int)
  
  folds = []
  
  gettingFolds = False
  for l in file:
    line = l.replace("\n", "")    
    
    if line == "":
      gettingFolds = True
      continue
    
    if gettingFolds: 
      foldType, cord = line.replace("fold along ", "").split("=") 
      folds.append((foldType, int(cord)))
    else:
      x, y = map(int, line.split(","))
      mp[(x, y)] = 1
  
  
  for i in range(1):
    foldType, cord = folds[i]
    
    if foldType == "x":
      foldLeft(mp, cord)
    else:
      foldUp(mp, cord)
  
  print(getCount(mp))
      
  
main()