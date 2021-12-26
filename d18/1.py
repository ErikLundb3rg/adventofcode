import json

class Node: 
  def __init__(self, value, left = None, right = None):
    self.value = value
    self.right = right
    self.parent = None
    self.left = left
  def addParent(self, parent):
    self.parent = parent
  
  def boom(self):
    self.value = 0
    self.right = None
    self.left = None
    #self.parent = self.parent.parent
  
  def split(self):
    half = self.value // 2
    leftVal = half
    rightVal = (half if self.value % 2 == 0 else half+1)
    self.value = -1
    self.left = Node(leftVal)
    self.left.addParent(self)
    self.right = Node(rightVal)
    self.right.addParent(self)

    
def addLeftVal(curr, value, cameFrom):
  global changedLeft
  if changedLeft or curr == None:
    return
  
  if curr.value != -1:
    curr.value += value
    changedLeft = True
    return
  
  cameFromRight = cameFrom == curr.right
  cameFromLeft = cameFrom == curr.left
  
  if cameFromRight:
    addLeftVal(curr.left, value, curr)
    if curr.parent: 
      addLeftVal(curr.parent, value, curr)
  if cameFromLeft:
    if curr.parent:
      addLeftVal(curr.parent, value, curr)
  else:
    addLeftVal(curr.right, value, curr)
    addLeftVal(curr.left, value, curr)
    
def addRightVal(curr, value, cameFrom):
  global changedRight
  if changedRight or curr == None:
    return
  
  if curr.value != -1:
    curr.value += value
    changedRight = True
    return
  
  cameFromRight = cameFrom == curr.right
  cameFromLeft = cameFrom == curr.left
  
  if cameFromLeft:
    addRightVal(curr.right, value, curr)
    if curr.parent:
      addRightVal(curr.parent, value, curr)
  if cameFromRight:
    if curr.parent:
      addRightVal(curr.parent, value, curr)
  else:
    addRightVal(curr.left, value, curr)
    addRightVal(curr.right, value, curr)
  
def explode(curr, depth):
  if curr.value != -1:
    return False
  if depth == 4:
    global changedLeft
    changedLeft = False
    addLeftVal(curr.parent, curr.left.value, curr)
    global changedRight 
    changedRight = False
    addRightVal(curr.parent, curr.right.value, curr)
    curr.boom()
    
    return True    
  
  else:
    return explode(curr.left, depth+1) or explode(curr.right, depth+1)

def split(curr):
  if curr == None:
    return False
  
  if curr.value > 9:
    curr.split()
    return True
  
  return split(curr.left) or split(curr.right)
    
def addBst(a, b):
  newRoot = Node(-1, a, b)
  a.addParent(newRoot)
  b.addParent(newRoot)  
  didExplode = True
  didSplit = True
  
  while explode(newRoot, 0) or split(newRoot):
    pass
  
  return newRoot


def bstFromArr(arr):
  if type(arr) == int:
    return Node(arr)
  else:
    left = bstFromArr(arr[0])
    right = bstFromArr(arr[1])
    root = Node(-1, left, right)
    left.addParent(root)
    right.addParent(root)
    return root

def arrFromString(s):
  return json.loads(s)
  
  

def tree(curr):
  if curr == None:
    return 0
  if curr.value != -1:
    return curr.value
  
  res = []
  res.append(tree(curr.left))
  res.append(tree(curr.right))
  return res
  
def magnitude(curr):
  if curr.value != -1:
    return curr.value 
  return ( 3*magnitude(curr.left) ) + ( 2*magnitude(curr.right))
  
def main():
  
  file = open("actual.in", "r")
  start = True
  root = -1
  for l in file:
    lineArr = arrFromString(l.replace("\n", ""))
    
    if start:
      root = bstFromArr(lineArr)
      start = False
    else:
      root = addBst(root, bstFromArr(lineArr))
      
  
  print("Magnitude: ", magnitude(root))
  print(tree(root))
main()