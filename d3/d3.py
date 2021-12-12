



def main():
  epArr = [] 
  gaArr = []
  
  nums = []
  
  for i in range(1000):
    nums.append(input())
  
  
  N = len(nums[0])
  
  for i in range(N):
    diff = 0
    
    for j in range(1000):
      bit = nums[j][i]
      
      if bit == "1":
        diff += 1
      else:
        diff -= 1
    
    if diff > 0:
      gaArr.append(1)
      epArr.append(0)
    else:
      gaArr.append(0)
      epArr.append(1)
  
  ga = 0
  ep = 0

  for digit in gaArr:
    ga = ga*2 + int(digit)
  for digit in epArr:
    ep = ep*2 + int(digit)
    
  print(ga * ep)
  
main()