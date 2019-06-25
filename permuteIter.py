def permute(n):
   ans = []
   ls = [0]*n
   pos = 0
   while (pos >= 0):
     if pos < n:
       ls[pos] = ls[pos] + 1
       if ls[pos] > n:
         ls[pos] = 0
         pos = pos - 1
       else:
          pos = pos + 1
     elif len(ls) == len(list(set(ls))):
       ans.append(list(ls))
       pos = pos - 1
     else:
       pos = pos - 1
   return(ans) 
