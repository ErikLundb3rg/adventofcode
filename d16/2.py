
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
  value = int(number, 2)
  return (value, index)

def subPacketsByLength(index):
  end = index+15
  lengthInBits = int(binaryInp[index:end], 2)
  # jump to head
  index = end
  
  usedLen = 0
  subPackets = []
  while usedLen < lengthInBits:
    value, to = computeSubPackets(index)
    subPackets.append(value)
    usedLen += to-index
    index = to
    
  return (subPackets, index)

def subPacketsByAmount(index):
  numOfSubPackets = int(binaryInp[index:index+11], 2)
  index+=11
  subPackets = []
  for _ in range(numOfSubPackets):
    value, to = computeSubPackets(index)
    subPackets.append(value)
    index = to
    
  return (subPackets, to)
  
def matchPackets(pType, packets):
  print("ptype, packets", pType, packets)
  if pType == 0:
    return sum(packets)
  elif pType == 1:
    product = 1
    for p in packets:
      product *= p
    return product
  elif pType == 2:
    return min(packets)
  elif pType == 3:
    return max(packets)
  elif pType == 5:
    return (1 if packets[0] > packets[1] else 0)
  elif pType == 6:
    return (1 if packets[0] < packets[1] else 0)
  elif pType == 7:
    return (1 if packets[0] == packets[1] else 0)  
  
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
    packets = []
    newIndex = 0
    if lengthTypeId == 0:
      subPackets, to = subPacketsByLength(index)
      newIndex = to
      packets = subPackets
    elif lengthTypeId == 1:
      subPackets, to = subPacketsByAmount(index)
      newIndex = to
      packets = subPackets
    
    return matchPackets(packetType, packets), newIndex 
    
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
  
  a, b  = computeSubPackets(0) 
  print(a)
  
main()