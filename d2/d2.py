


def main():
  right = 0
  down = 0
  
  
  arr = []
  
  for i in range(1000):
    arr.append(input())
  
  
  for item in arr:
    s = item.split(" ")
    d, v = s
    val = int(v)
    
    if d == "down":
      down += val
    elif d == "up":
      down -= val
    else:
      right += val
      
  print(right * down)
  
  
main()