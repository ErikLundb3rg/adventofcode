
import sys
sys.setrecursionlimit(10**7)

# This is naive
def getNumberOfFish(timer, totalDays):
  if (totalDays == 80):
    return 1
  if timer == 0:
    return getNumberOfFish(6, totalDays+1) + getNumberOfFish(8, totalDays+1)
  return getNumberOfFish(timer-1, totalDays+1)


def main():
  
  numbers = [int(x) for x in input().split(",")]
  
  combinations = [i for i in range(8)]
  mp = {}
  for fish in combinations:
    mp[fish] = getNumberOfFish(fish, 0)
    
    
  sm = 0
  for fish in numbers:
    sm += mp[fish]
  
  print(sm)
  
  
  
  
  
  
  
main()