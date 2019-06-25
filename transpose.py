def transpose(l):
    k = []
    for a in l[0]:
        k.append([a])
    l.pop(0)
    for i in l:
        for j in list(range(0,len(i))):
            k[j].append(i[j])
    return k


