
def isInBox(x, y):
  return xInBox(x) and yInBox(y) 

def yInBox(y):
  sX, eX, sY, eY = box
  return y >= sY and y <= eY

def xInBox(x):
  sX, eX, sY, eY = box
  return x >= sX and x <= eX

def simulateXVel(vel):
  pos = 0
  MAX = 1000
  steps = 0
  
  possibleSteps = []
  for i in range(MAX):
    steps += 1
    pos += vel
    if xInBox(pos):
      possibleSteps.append(steps)
    if vel > 0:
      vel -= 1
    elif vel < 0:
      vel += 1
  return possibleSteps

def simulateYVel(vel):
  steps = 0
  MAX = 1000
  pos = 0
  mxPos = 0
  
  for i in range(MAX):
    steps += 1
    pos += vel
    mxPos = max(mxPos, pos)
    vel -= 1
    if yInBox(pos):
      return (mxPos, steps)
  
  return (-1, -1)


def main():
  
  file = open("actual.in", "r")
  # x1, x2, y1, y2
  global box
  box = (-1, -1, -1, -1)
  for l in file:
    line = l.replace("\n", "")
    
    xStart = line.split(",")[0].split("..")[0].replace("target area: x=", "")
    xEnd = line.split(",")[0].split("..")[1]
    yStart = line.split(",")[1].split("..")[0].replace(" y=", "")
    yEnd = line.split(",")[1].split("..")[1]
    box = (int(xStart), int(xEnd), int(yStart), int(yEnd))
  
  possibleXSteps = set()
  
  
  for xVel in range(1000):
    res = simulateXVel(xVel)
    
    for possibleStep in res:
      possibleXSteps.add(possibleStep)
  
  
  possibleYThrows = []
  for yVel in range(-1000, 1000):
    mxPos, steps = simulateYVel(yVel)
    if steps != -1:
      possibleYThrows.append((mxPos, steps))
      
  possibleYThrows.sort()
  possibleYThrows.reverse()
  
  for throw in possibleYThrows:
    mxPos, steps = throw
    if steps in possibleXSteps:
      print(mxPos)
      return
    
  print("not found")
    
      
  
  
main()