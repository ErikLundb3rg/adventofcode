



from collections import defaultdict 

def main():
  lines = []
  
  for i in range(500):
    a = [x.split(",") for x in input().split(" -> ")]
    x1, y1 = [int(x) for x in a[0]]
    x2, y2 = [int(x) for x in a[1]]
    lines.append((x1, y1, x2, y2))
    
  
  mp = defaultdict(int)
  
  for line in lines:
    x1, y1, x2, y2 = line
    
    xMin = min(x1, x2)
    xTo = max(x1, x2)
    yMin = min(y1, y2)
    yTo = max(y1, y2)
    
    
    if y1 == y2: 
      for i in range(xMin, xTo+1):
        mp[(i, y1)] += 1
    elif x1 == x2:
      for i in range(yMin, yTo+1):
        mp[(x1, i)] += 1
        
  
  sm = 0
  
  for key in mp:
    if mp[key] > 1:
      sm += 1
      
  print(sm)   
    
    
  
  
main()