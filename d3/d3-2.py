



def main():
  
  
  
  
  
  
 
  nums = []
  leastCommon = []
  mostCommon = []
  
  for i in range(1000):
    x = input()
    nums.append(x)
    leastCommon.append(x)
    mostCommon.append(x)

  N = len(leastCommon[0])
  
  leastCommonBit = []
  
      
  lowest = ""
  for i in range(N):
    keep = []
    
    diff = 0
    leastCommonBit = 1
    for j in range(len(leastCommon)):
      bit = leastCommon[j][i]
      
      if bit == "1":
        diff += 1
      else:
        diff -= 1

    if diff >= 0:
      leastCommonBit = 0
    
    for j in range(len(leastCommon)):
      
      bit = leastCommon[j][i]
      
      if int(bit) == leastCommonBit:
        keep.append(leastCommon[j])
      
    leastCommon = keep
    if len(leastCommon) == 1:
      lowest = leastCommon[0]
      break
    
  mostCommonBit = []
    
  greatest = ""
  for i in range(N):
    keep = []
    
    diff = 0
    mostCommonBit = 0
    for j in range(len(mostCommon)):
      bit = mostCommon[j][i]
      
      if bit == "1":
        diff += 1
      else:
        diff -= 1

    if diff >= 0:
      mostCommonBit = 1
    
    for j in range(len(mostCommon)):
      
      bit = mostCommon[j][i]
      
      if int(bit) == mostCommonBit:
        keep.append(mostCommon[j])
    mostCommon = keep
    
    if len(mostCommon) == 1:
      greatest = mostCommon[0]
      
      
    
  
  print("low", lowest)
  print("great", greatest)
  
  ga = 0
  ep = 0
  for digit in lowest:
    ga = ga*2 + int(digit)
  for digit in mostCommon[0]:
    ep = ep*2 + int(digit)
  print(ga*ep)
main()