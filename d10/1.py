







def main():
  openers = set(["[", "{", "(", "<"])
  closer = {
    "[": "]",
    "{": "}",
    "(": ")",
    "<": ">"
  }
  
  errorMP = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
  }  
  
  errorSm = 0
  
  for i in range(98):
    line = input()
    
    stack = []
    for letter in line:
      if letter in openers:
        stack.append(letter)
      else:
        topOfStack = stack[-1]
        if letter != closer[topOfStack]:
          errorSm += errorMP[letter]
          break
        else:
          stack.pop()
  print(errorSm)

main()