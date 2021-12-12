from collections import deque

def getNum(fish):
  week = [0] * 9
  week[fish] = 1
  
  for day in range(days):
    zeroDay = week[0]
    week.pop(0)
    week.append(0)
    
    week[6] += zeroDay
    week[8] += zeroDay

  return sum(week)
  
  
def main():  
  numbers = [int(x) for x in input().split(",")]
  
  combinations = [i for i in range(8)]
  mp = {}
  
  global days
  days = 256
  for fish in combinations:
    mp[fish] = getNum(fish)
    
  sm = 0
  for fish in numbers:
    sm += mp[fish]
  print(sm)
  
  
  
  
  
  
  
main()




