from validrow import *
from transpose import *
from blocktorows import *

def validsolution(l):
    k = transpose(l)
    for i in l:
        if validrow(i) != True:
            return False
    for j in k:
        if validrow(j) != True:
            return False
    for k in [0,3,6]:
        if validrow(blocktorows(l[k:k+3])) != True:
            return False
    return True

    
        
    
