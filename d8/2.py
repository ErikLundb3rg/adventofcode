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
      mp[letter] = "a" 

def findMappingUtil(mp, p1, BorD):
  arr = []
  
  for comb in p1.split(" "):
    if len(comb) == 5:
      for letter in comb:
        if letter == BorD:
          arr.append(letter)
          
  # this is a B
  if len(arr) == 1:
    mp[arr[0]] = "b"
  elif len(arr) == 3:
    mp[arr[0]] = "d"
  else:
    print("Should not be here")
  
def findMappingOfBAndD(mp, p1):
  
  nr1 = ""
  nr4 = ""
  
  for comb in p1.split(" "):
    L = len(comb)
    if L == 2:
      nr1 = comb
    elif L == 4:
      nr4 = comb
      
  BD = []
  
  for letter in nr4:
    if letter not in nr1:
      BD.append(letter)
      
  findMappingUtil(mp, p1, BD[0])
  findMappingUtil(mp, p1, BD[1])  
      
# easiest: 1 4 7 8
# 5 letters: 2 3 5
# 6 letters: 0 6 9  

def findMappingOfCAndF(mp, p1):
  nr1 = ""
  
  for comb in p1.split(" "):
    if len(comb) == 2:
      nr1 = comb
      
      
  nr5 = ""
  # end me
  for comb in p1.split(" "):
    if len(comb) == 5:
      for letter in comb:
        if mp[letter] == "b":
          nr5 = comb
          break 
  for letter in nr1:
    if letter in nr5:
      mp[letter] = "f"
    if letter not in nr5:
      mp[letter] = "c"     
  
def findMappingOfEAndG(mp, p1):
  nr9 = ""
  nr8 = ""
  
  for comb in p1.split(" "):
    if len(comb) == 7:
      nr8 = comb
    elif len(comb) == 6:
      hasD = False
      hasC = False
      for letter in comb:
        if mp[letter] == "d":
          hasD = True
        elif mp[letter] == "c":
          hasC = True
      if hasD and hasC: 
        nr9 = comb

  for letter in nr8:
    if letter not in nr9:
      mp[letter] = "e"
  
  for letter in nr8:
    if mp[letter] == "":
      mp[letter] = "g"    
  
from collections import defaultdict


def getSumOf(line):
  
  mp = defaultdict(str)
  
  p1, p2 = line
  
  findMappingOfA(mp, p1)
  findMappingOfBAndD(mp, p1)
  findMappingOfCAndF(mp, p1)
  findMappingOfEAndG(mp, p1)
  
  getDigitValueOf = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9
  }
  
  sm = 0
  for comb in p2.split(" "):
    characters = []
    
    for letter in comb:
      characters.append(mp[letter])
    
    characters.sort()
    
    sm = (sm*10) +  getDigitValueOf["".join(characters)]
      
  return sm
def main():
  
  
  
  lines = []
  for i in range(200):
    p1, p2 = input().split(" | ")
    lines.append((p1, p2))
  
  
  total = 0
  for line in lines:
    total += getSumOf(line)
  print(total)
  
  
  
  
main()