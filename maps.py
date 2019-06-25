l = [2,100,29,97,33,38,59,67]

def sqr(n):
   return n*n


print(list(map(sqr,l)))

## I wrote it simply
def square(l):
   i = 0
   l1 = []
   while i < len(l):
      l1.append(l[i]*l[i])
      i += 1
   return(l1)
      
print(square(l))
