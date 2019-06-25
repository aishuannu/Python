def Bucket(l,i):
    ls = []
    k = 0
    for j in range(len(l)):
        if len(l[j-k]) < i+1:
            ls.append(l.pop(j-k))
            k += 1
    for m in range(53):
        k1 = 0
        for n in range(len(l)):
            if m <= 26:
                if l[n-k1][i] == chr(65+m):
                    ls.append(l.pop(n-k1))
                    k1 += 1
            else:
                if l[n-k1][i] == chr(70+m):
                    ls.append(l.pop(n-k1))
                    k1 += 1               
    return ls

#l = ["Annu","Aishu","AVinash","ABnuz","Anush"]
##l = ['Annu', 'Aishu', 'ABnuz', 'Anush', 'AVinash']
##print(Bucket(l,4))                
   
    


















