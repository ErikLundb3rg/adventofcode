



def isInGrid(x, y):
  return x >= 0 and x < len(matrix[0]) and y >= 0 and y < len(matrix)
def isLowPoint(x, y):
  
  isLow = True
  curr = matrix[y][x]
  if isInGrid(x+1, y) and matrix[y][x+1] <= curr:
    isLow = False
  if isInGrid(x-1, y) and matrix[y][x-1] <= curr:
    isLow = False
  if isInGrid(x, y+1) and matrix[y+1][x] <= curr:
    isLow = False
  if isInGrid(x, y-1) and matrix[y-1][x] <= curr:
    isLow = False
    
  return isLow



def bfs(xB, yB):
  size = 0
  
  q = [(xB, yB)]
  
  visited = set()
  visited.add((xB, yB))
  while q:
    x, y = q.pop(0)
    
    size += 1

    
    if isInGrid(x+1, y) and int(matrix[y][x+1]) != 9 and (x+1, y) not in visited:
      q.append((x+1, y))
      visited.add((x+1, y))
    if isInGrid(x-1, y) and int(matrix[y][x-1]) != 9 and (x-1, y) not in visited:
      q.append((x-1, y))
      visited.add((x-1, y))
    if isInGrid(x, y+1) and int(matrix[y+1][x]) != 9 and (x, y+1) not in visited:
      q.append((x, y+1))
      visited.add((x, y+1))
    if isInGrid(x, y-1) and int(matrix[y-1][x]) != 9 and (x, y-1) not in visited:
      q.append((x, y-1))
      visited.add((x, y-1))

  return size

  
  
def main():


  global matrix
  matrix = []


  for i in range(100):
    matrix.append(input())
    
  
  basins = []
  for y in range(100):
    for x in range(len(matrix[0])):
      if isLowPoint(int(x), int(y)):
        basins.append(bfs(x, y))
      
  basins.sort()
  
  sm = 1
  for i in range(len(basins)-3, len(basins)):
    sm *= basins[i]
  
  print(basins)
  print(sm)
        



main()