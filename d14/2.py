
from collections import defaultdict

def main():
  file = open("actual.in", "r")
  mp = {}
  pairToOccurance = defaultdict(int)
  count = defaultdict(int)
  
  template = []
  for i, l in enumerate(file):
    line = l.replace("\n", "")

    if i == 0:
      template = list(line)
    if i >= 2:
      a, b = line.split(" -> ")
      mp[a] = b
  
  for i in range(len(template)-1):
    a = template[i]
    b = template[i+1]
    pairToOccurance[a+b] += 1
  
  for letter in template:
    count[letter] += 1
  
  for iteration in range(40):
    newEntries = defaultdict(int)
    keys = list(pairToOccurance.keys())
    for AB in keys:
      occurances = pairToOccurance[AB]
      a = AB[0]
      b = AB[1]
      between = mp[AB]
      count[between] += occurances
      newEntries[a+between] += occurances
      newEntries[between+b] += occurances
    
    pairToOccurance = newEntries

  countValues = list(count.values())
  print(max(countValues) - min(countValues))
  
  
main()