


def main():
  right = 0
  down = 0
  aim = 0
  
  
  arr = []
  
  for i in range(1000):
    arr.append(input())
  
  
  for item in arr:
    s = item.split(" ")
    d, v = s
    val = int(v)
    
    if d == "down":
      aim += val
    elif d == "up":
      aim -= val
    else:
      right += val
      down += aim * val
      
  print(right * down)
  
  
main()