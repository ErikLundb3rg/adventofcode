from collections import defaultdict

def dfs(curr, end, mp, visited, hasVisitedOneSmallCaveTwice):
  if curr == end:
    return 1
  if curr in visited:
    if hasVisitedOneSmallCaveTwice or curr == "start":
      return 0
    hasVisitedOneSmallCaveTwice = True
  if curr in smallCaves:
    visited.add(curr)
  
  sm = 0
  for neighbor in mp[curr]:
    sm += dfs(neighbor, end, mp, visited.copy(), hasVisitedOneSmallCaveTwice)
  
  return sm

def main():
  file = open("actual.in", "r")
  mp = defaultdict(list)
  global smallCaves
  smallCaves = set()
  
  for line in file:
    u, v = line.replace("\n", "").split("-")
    
    if u.islower():
      smallCaves.add(u)
    if v.islower():
      smallCaves.add(v)
      
    mp[u].append(v)
    mp[v].append(u)

  print(mp)
  sm = dfs("start", "end", mp, set(), False)
  print(sm)
  
  
  file.close()
main()