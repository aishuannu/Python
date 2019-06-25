def interleave(v,l):
  ans = []
  for i in range(0,len(l)+1):
    ans.append(l[:i] + [v] + l[i:]) 
  return ans
   
def permute(n):
  if n == 1:
    return [[1]]
  ls = permute(n-1)
  ans = []
  for p in ls:
    ans = ans + interleave(n,p) 
  return ans
  
print(permute(3))
