from Bucket import *

def Bucketsort(l):
    n = 0
    i = 0
    l = Bucket(l,0)
    ls = []
    while p < len(l[0]):
        while len(ls) <  len(l):
            temp = l[n][i]
            x = n
            for k in range(x,len(l)):
                if l[k][i] == temp:
                    n = n+1
                else:
                    break
            ls =ls + (bucket(l[t:k],p+1))
        l = ls
        ls =[]
        n = 0
        p = p + 1























    

l = ["Annu","Aishu","AVinash","ABnuz","Anush","aab","aba","banu","Ba","Aa"]        
print(Bucketsort(l))
