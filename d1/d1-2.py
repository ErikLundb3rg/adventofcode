



def main():
  
  
  arr = []
  sm = 0
  for i in range(2000):
    arr.append(int(input()))
  
  prev = 0
  
  for i in range(0, 3):
    prev += arr[i]
  
  for i in range(1, len(arr)-2):
    currSm = 0
    
    for j in range(i, i+3):
      currSm += arr[j]
      
    if currSm> prev:
      sm +=1 
    prev = currSm
    
  print(sm)
  
  
  
main()