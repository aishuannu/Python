def blah(l):
    def insert(v,l):
        cpos = 0
        while cpos < len(l) and l[cpos] < v :
            cpos = cpos + 1
            return l[:cpos] + [v] + l[cpos:]
    i=0
    while(i<len(l)):
        l=insert(l.pop(i),l)
        if (l[i+1]<l[i]):
            i=i+1
        else:
            i=i+2
    return l
