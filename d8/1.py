



def findMappingOfA(mp, p1):
  
  nr1 = ""
  nr2 = ""
  
  for comb in p1.split(" "):
    L = len(comb)
    if L == 2:
      nr1 = comb
    elif L == 3:
      nr2 = comb
  
  for letter in nr2:
    if letter not in nr1:
      mp[letter] = "A" 

def findMappingOfB(mp, p1):
  lenFives = []
    
  for comb in p1.split(" "):
    if len(comb) == 5:
      lenFives.append(comb) 
      

# easiest: 1 4 7 8
# 5 letters: 2 3 5
# 6 letters: 0 6 9  


def getSumOf(line):
  mp = {}
  
  p1, p2 = line
  
  findMappingOfA(mp, p1)
  
  
    
    
  

def main():
  
  
  
  lines = []
  for i in range(200):
    p1, p2 = input().split(" | ")
    lines.append((p1, p2))
  
  
  sm = 0
  for line in lines:
    x = getSumOf(line)
    
  
  
  print(sm)
  
  
main()