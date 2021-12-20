
from queue import PriorityQueue

from collections import defaultdict

def isInGrid(x, y):
  return x >= 0 and x < width and y >= 0 and y < height

def getNeighbours(xS, yS):
  for y in range(yS-1, yS+2):
    for x in range(xS-1, xS+2):
      if ((
        (x, y) == (xS+1, yS) or 
        (x, y) == (xS-1, yS) or 
        (x, y) == (xS, yS+1) or 
        (x, y) == (xS, yS-1) )
        and isInGrid(x, y)
      ):
        yield (grid[y][x], x, y)
        
  
def printPath(mp): 
  total = grid[9][9]
  curr = (9, 9)
  print(curr)
  while curr in mp:
    prev = mp[curr]
    print(prev)
    curr = prev
    
def dijkstra(start, target):
  INF = 10e10
  
  dist = [[INF for i in range(width)] for j in range(height)]
  xS, yS = start
  dist[yS][xS] = 0
  pq = PriorityQueue()
  pq.put((dist[yS][xS], xS, yS))
  prevMp = {}
  visited = set()
  
  while not pq.empty():
    dC, xC, yC = pq.get()
    visited.add((xC, yC))
    
    if (xC, yC) == target:
      #printPath(prevMp)
      return dist[yC][xC]
    
    for neighbor in getNeighbours(xC, yC):
      #if neighbor not in visited:
        neighborWeight, x, y = neighbor
        alt = dist[yC][xC] + neighborWeight
        
        if alt < dist[y][x]:
          prevMp[(x, y)] = (xC, yC)
          dist[y][x] = alt
          pq.put((alt, x, y))


  return -1

def incrementedRow(row, inc):
  newR = []
  
  for item in row:
    x = item+inc
    newVal = x if x <= 9 else x-9
    newR.append(newVal)
  return newR

def flatten(t):
  return [item for sublist in t for item in sublist]
  
def main():
  
  
  file = open("actual.in", "r")
  global grid, width, height
  smallGrid = []
  
  for l in file:
    line = l.replace("\n", "")
    smallGrid.append([int(x) for x in list(line)])
  
  
  width = len(smallGrid[0])*5
  height = len(smallGrid)*5
  grid = []
  
  for i in range(5):
    
    for smallRow in smallGrid:
      bigRow = flatten([incrementedRow(smallRow, i+p) for p in range(5)])
      grid.append(bigRow)
      
  start = (0, 0)
  finish = (width-1, height-1)
  print(finish)
  print(dijkstra(start, finish))
  

  
  
main()