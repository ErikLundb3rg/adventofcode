
import statistics


def main():
  crabs = [int(x) for x in input().split(",")]
  
  
  print("sum, ", sum(crabs))
  avg = statistics.median(crabs)
  print("avg ", avg)
  fuel = 0
  for crab in crabs:
    fuel += abs(crab-avg)
  print(fuel)
  
  
  
main()