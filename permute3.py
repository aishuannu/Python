def permute3():
  for i in range(1,4):
    for j in range(1,4):
      for k in range(1,4):
         x = [i,j,k]
         if len(x) == len(list(set(x))):  # checks if x is a permutation
           print(x)
         else: 
           print(str(x) + " is not a permutation")

permute3()
