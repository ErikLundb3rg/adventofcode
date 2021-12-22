

def hexaToBin(sign):
  scale = 16 
  num_of_bits = 4
  return bin(int(sign, scale))[2:].zfill(num_of_bits)


def getLiteralValue(index):
  number = ""  
  while True:
    shouldEnd = int(binaryInp[index]) == 0
    number += binaryInp[index+1:index+5]
    index += 5
    if shouldEnd:
      break
  return index

def subPacketsByLength(index):
  end = index+15
  lengthInBits = int(binaryInp[index:end], 2)
  # jump to head
  index = end
  
  usedLen = 0
  while usedLen < lengthInBits:
    to = computeSubPackets(index)
    usedLen += to-index
    index = to
    
  return index

def subPacketsByAmount(index):
  numOfSubPackets = int(binaryInp[index:index+11], 2)
  index+=11
  for _ in range(numOfSubPackets):
    to = computeSubPackets(index)
    index = to
    
  return to
  
  
def computeSubPackets(index): 
  global totalVersion
  versionType = int(binaryInp[index:index+3], 2)
  totalVersion += versionType
  packetType = int(binaryInp[index+3:index+6], 2)
  index += 6
  
  if packetType == 4:
    return getLiteralValue(index)
  else:
    lengthTypeId = int(binaryInp[index])
    index += 1
    if lengthTypeId == 0:
      return subPacketsByLength(index)
    elif lengthTypeId == 1:
      return subPacketsByAmount(index)
    
def main():
  file = open("actual.in", "r")
  
  global hexaDeciMapping, binaryInp, totalVersion
  totalVersion = 0

  hexaString = ""
  for l in file:
    line = l.replace("\n", "")
    hexaString = line
    
  binaryInp = []
  
  for letter in hexaString:
    for digit in hexaToBin(letter):
      binaryInp.append(digit)
  
  binaryInp = "".join(binaryInp)
  
  computeSubPackets(0)
  print(totalVersion)
  
main()