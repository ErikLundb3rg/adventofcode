
import statistics


def main():
  crabs = [int(x) for x in input().split(",")]
  smallest = 10e20
  
  for pos in range(1, max(crabs)+1):
    sm = 0
    
    for crab in crabs:
      N = abs(pos-crab)
      sm += (N*(N+1)) // 2

    smallest = min(smallest, sm)
  
  print(smallest)
  
main()