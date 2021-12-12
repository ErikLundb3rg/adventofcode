def isLineCorrupted(line):
  stack = []
  for letter in line:
    if letter in openers:
      stack.append(letter)
    else:
      topOfStack = stack[-1]
      if letter != closer[topOfStack]:
        return True
      stack.pop()
  return False

def sumFromLine(line):
  stack = []
  
  for letter in line:
    if letter in openers:
      stack.append(letter)
    else:
      stack.pop()
  
  stack.reverse()      
  sm = 0
  for symbol in stack:
    sm = (sm*5)+scoreMP[symbol]
  return sm
    

def main():
  global openers, closer, scoreMP
  openers = set(["[", "{", "(", "<"])
  closer = {
    "[": "]",
    "{": "}",
    "(": ")",
    "<": ">"
  }
  
  scoreMP = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
  }  
  
  scores = []
  for i in range(98):
    line = input()
    sm = 0
    
    if not isLineCorrupted(line):
      scores.append(sumFromLine(line))

  scores.sort()
  print(scores[len(scores) // 2])    

main()