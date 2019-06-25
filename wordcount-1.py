st = " This is a long and boring sentence. This is another, and   so on ."

def words(s): # does not work. 
  l = []
  pos1 = 0 
  pos2 = 0
  while pos1 != len(s):
    for i in range(pos2,len(s)):
      if s[i] != " ":
        pos1 = i
        break
    for j in range(pos1,len(s)):
      if s[j] == " ":
        pos2 = j-1
        break
    l.append(s[pos1:pos2+1])
  return l
    
print(words(st))
    


