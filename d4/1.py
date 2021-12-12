import sys

def calculateBingo(matrix, num):
  x = 0
  for i in range(5):
    
    for j in range(5):
      if matrix[i][j] >= 0:
        x += matrix[i][j]

  return x * num
  
  

def checkBingo(matrix):
  for i in range(5):
    row = True
    for j in range(5):
      if matrix[i][j] >= 0:
        row = False
    
    if row:
      return row
  
  for i in range(5):
    col = True
    
    for j in range(5):
      if matrix[j][i] >= 0:
        col = False
    
    if col:
      return col
  


def markMatrixWithNum(matrix, N):
  for i in range(5):
    for j in range(5):
      if matrix[i][j] == N:
        matrix[i][j] -= 100


def main():
  numbers = [int(x) for x in input().split(",")]
  matrices = []
  
  
  
  for i in range(100):
    input()
    matrix = []
    for i in range(5):
      arr = []
      sArr = input().split(" ")
      for s in sArr:
        if not s == "":
          arr.append(int(s))
      matrix.append(arr)
    matrices.append(matrix)
    
  for num in numbers:
    for matrix in matrices:
      markMatrixWithNum(matrix, num)
      
    for matrix in matrices:
      isBingo = checkBingo(matrix)
      
      print(isBingo)
      if isBingo:
        sm = calculateBingo(matrix, num)
        print(sm)
        sys.exit(0)
  
  
  
main()