



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
def main():


  global matrix
  matrix = []


  for i in range(100):
    matrix.append(input())
    
  
  sm = 0
  for y in range(100):
    for x in range(len(matrix[0])):
      if isLowPoint(int(x), int(y)):
        sm += int(matrix[y][x])+1
        
  print(sm)
        



main()