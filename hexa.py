def hexa(a):
    l = len(a)
    lis = ["A","B","C","D","E","F"]
    s = 0
    for i in list(range(0,l)):
        if a[i] in lis:
            s = s + (lis.index(a[i])+10)*(16**(l-1-i))
        else:
            s = s + int(a[i])*(16**(l-1-i))
    return s

print(hexa("AB"))
