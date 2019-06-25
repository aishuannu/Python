st = " This is a long and boring sentence. This is another, and   so on ."

def words(s): 
  ls = []
  l = []
  for i in range(0,len(s)):
    if s[i] == " ":
      if l != []:
        ls.append(l)
        l = []
    else:
      l.append(s[i])
  return ls
 
print(words(st))


