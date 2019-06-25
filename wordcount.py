st = " This is a long and boring sentence. This is another, and   so on ."

def words(s):
   State = 0 # 0 means outside, 1 means inside 
   ans = []
   curr = []
   for i in s:
     if State == 0:
       if i != " ":
         State = 1
         curr.append(i)
     elif State == 1:
       if i != " ":
         curr.append(i)
       else:
         State = 0
         ans.append(curr)
         curr = []
# Will miss the last word 
   return(ans)

print(words(st))
st = "This"
print(words(st))

       
     

