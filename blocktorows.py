def blockTorows(l): #list of list with three elements in which each element is of length9
    k =[[],[],[]]
    for i in l:
        for j in [0,1,2,3,4,5,6,7,8]:
            k[(j//3)].append(i[j])
    return k
        
        
    
