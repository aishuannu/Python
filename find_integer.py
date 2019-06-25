st = "456 This is a 7lo6ng5 666 666 888. and 6boring 6.8  sentence 6.hbnbm 4.1 5This 6 is another, and  67."

def intgrs(s):
   State = 0
   ans = []
   curr = ""
   for i in s:
     if State == -1:
       if i == " ":
         State = 0
       elif i == ".":
         State - -12     
     elif State == 0 or State == -12:
         if i in ["0","1","2","3","4","5","6","7","8","9"]:
             curr = curr+i
             State = 1
         elif i == ".":
             State = 12
         elif i == " ":
             State = 0
         else:
             State = -1
     elif State == 1:
         if i == " ":
             State = 0
             ans.append(curr)
             curr = ""
         elif i in ["0","1","2","3","4","5","6","7","8","9"]:
             curr = curr+i
             State = 1
         elif i == ".":
             State = 12
         else:
             State = -1
             curr = ""
     elif State == 12:
         if i in ["1","2","3","4","5","6","7","8","9"]:
             curr = ""
             State = -1        
         elif i == " ":
             ans.append(curr)
             curr = ""
             State = 0
         else:
             ans.append(curr)
             curr = ""           
             State = -1
   if curr != "":
       ans.append(curr)
   return(ans)

print(intgrs(st))

