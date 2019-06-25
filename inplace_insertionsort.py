def insert(v,l):
    cpos = 0
    while cpos < len(l) and l[cpos] < v :
        cpos = cpos + 1
    return l[:cpos] + [v] + l[cpos:],cpos


def inplace_insertionsort(l):
    original_index = 0
    for i in l:
        l,cpos = insert(i,l)
        if cpos <= original_index:
            original_index += 1
            l.pop(original_index)
            original_index -= 1
        else:
            l.pop(original_index)
        original_index += 1
    return l

print(inplace_insertionsort([2,2,3,6,1,7,8]))
