



def main():
  
  
  arr = []
  sm = 0
  for i in range(2000):
    arr.append(int(input()))
  
  prev = arr[0]
  for i in range(1, len(arr)):
    if arr[i] > prev:
      sm +=1 
    prev = arr[i]
    
  print(sm)
  
  
  
main()