
from collections import defaultdict
def getResult(template):
  count = defaultdict(int)
  for letter in template:
    count[letter] += 1
  
  pairs = list(count.values())
  
  return max(pairs)-min(pairs)

def main():
  file = open("actual.in", "r")
  mp = {}
  
  template = []
  for i, l in enumerate(file):
    line = l.replace("\n", "")

    if i == 0:
      template = list(line)
    if i >= 2:
      a, b = line.split(" -> ")
      mp[a] = b
  
  
  for iteration in range(10):
    nextIt = []
    
    for i in range(len(template)-1):
      a = template[i]
      b = template[i+1]
      AB =a+b
      between = mp[AB]
      nextIt.append(a)
      nextIt.append(between)
      if i == len(template)-2:
        nextIt.append(b)
          
    template = nextIt

  print(len(template))
  print(getResult(template))
  
  
  
main()