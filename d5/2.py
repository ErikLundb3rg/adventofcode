



from collections import defaultdict 



def match(delta):
  if delta > 0:
    return 1
  elif delta < 0:
    return -1
  return 0


def main():
  lines = []
  
  for i in range(10):
    a = [x.split(",") for x in input().split(" -> ")]
    x1, y1 = [int(x) for x in a[0]]
    x2, y2 = [int(x) for x in a[1]]
    lines.append((x1, y1, x2, y2))
    
  
  mp = defaultdict(int)
  
  for line in lines:
    x1, y1, x2, y2 = line
    
    dx = x2-x1
    dy = y2-y1
    
    dx = match(dx)
    dy = match(dy)
    
    while (x1, y1) != (x2, y2):
      mp[(x1, y1)] += 1
      x1 += dx
      y1 += dy
      
    mp[(x2, y2)] += 1
    
    
  sm = 0
  
  for key in mp:
    #print(key, mp[key])
    if mp[key] > 1:
      sm += 1
      
  print(sm)   
    
    
  
  
main()