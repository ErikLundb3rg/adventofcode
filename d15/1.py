
from queue import PriorityQueue

from collections import defaultdict

def isInGrid(x, y):
  return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)
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
  INF = 1000
  
  dist = [[INF for i in range(len(grid[0]))] for j in range(len(grid))]
  xS, yS = start
  dist[yS][xS] = 0
  pq = PriorityQueue()
  pq.put((dist[yS][xS], xS, yS))
  prevMp = {}
  visited = set()
  
  while not pq.empty():
    wC, xC, yC = pq.get()
    visited.add((xC, yC))
    
    if (xC, yC) == target:
      #printPath(prevMp)
      return dist[yC][xC]
    
    for neighbor in getNeighbours(xC, yC):
      if neighbor not in visited:
        neighborWeight, x, y = neighbor
        alt = dist[yC][xC] + neighborWeight
        
        if alt < dist[y][x]:
          
          prevMp[(x, y)] = (xC, yC)
          dist[y][x] = alt
          pq.put((alt, x, y))
    
  return -1
def main():
  
  
  file = open("actual.in", "r")
  global grid
  grid = []
  
  for l in file:
    line = l.replace("\n", "")
    grid.append([int(x) for x in list(line)])
  
  start = (0, 0)
  finish = (len(grid)-1, len(grid[0])-1)



  print(dijkstra(start, finish))
  
  
  
    
  
  
  
  
main()