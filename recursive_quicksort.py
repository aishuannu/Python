def recursive_quicksort(l,b,e):
    if e-b < 2:
        if l[b] > l[e]:
            l[b],l[e] = l[e],l[b]
    else:
        p = l[b]
        left = b+1
        right = e
        while (right >= left):
            if (l[right] > p):
                right -= 1
            else:
                l[left],l[right] = l[right],l[left]
                left += 1
        if left > b+1:
            l[b],l[left-1] = l[left-1],l[b]
            l = iterative_quicksort(l,b,left)
            l = iterative_quicksort(l,left,e)
        else:
            l = iterative_quicksort(l,b+1,e)
    return(l)

print(iterative_quicksort([5,11,4,9,100,45,23,765,231,888,56,5432],0,11))
