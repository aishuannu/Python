class Graph:
  
  def __init__(self,n,l):
    self.V = list(range(1,n+1))
    self.E = [[]]
    for v in self.V :
     self.E.append([]) 
    for e in l:
      u,v = e
      self.E[u].append(v)
      self.E[v].append(u)

