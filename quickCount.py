from bleft import *
def quickCount(v,l):
    if v not in l:
        return 0
    elif bleft(v,l) == -1:
        return bleft(v+1,l) + 1 
    else:
        return bleft(v+1,l) - bleft(v,l)
