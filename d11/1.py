def isInGrid(x, y):
  return x >= 0 and x < width and y >= 0 and y < height
  
def getNeighborsOf(x, y):
  for otherY in range(y-1, y+2):
    for otherX in range(x-1, x+2):
      if (otherX, otherY) != (x, y) and isInGrid(otherX, otherY):
        yield (otherX, otherY)
        


def bfs(startX, startY):
  q = [(startX, startY)]
  hasFlashed.add((startX, startY))
  
  while q:
    x, y = q.pop(0)
    
    for neighbor in getNeighborsOf(x, y):
      otherX, otherY = neighbor
      grid[otherY][otherX] += 1  
      if grid[otherY][otherX] > 9 and not (otherX, otherY) in hasFlashed:
        hasFlashed.add((otherX, otherY))
        q.append((otherX, otherY))
def step():
  global hasFlashed
  hasFlashed = set()
  
  for x in range(width):
    for y in range(height):
      if grid[y][x] > 9 and not (x, y) in hasFlashed:
        bfs(x, y)

def increaseByOne():
  for x in range(width):
    for y in range(height):
      grid[y][x] += 1
  
def getFlashCount():
  cnt = 0
  for x in range(width):
    for y in range(height):
      if grid[y][x] > 9:
        cnt += 1
  return cnt
  
def resetFlashed():
  for x in range(width):
    for y in range(height):
      if grid[y][x] > 9: 
        grid[y][x] = 0
        
        
def printGrid():
  print("----------")
  for row in grid:
    print(row)
  print("----------")
def main():
  global width, height, grid
  
  grid = []
  for i in range(10):
    row = []
    for letter in input():
      row.append(int(letter))
    grid.append(row)
    
  height = len(grid)
  width = len(grid[0])
  
  sm = 0
  for steps in range(100):
    increaseByOne()
    step()
    sm += getFlashCount()
    resetFlashed()
    #printGrid()
  
  print(sm)
main()