def iterative_quicksort(l): #length of l is > 2
    n = len(l)
    p = l[n//2]
    left = 0
    right = n-1
    while right >= n//2:
        if l[right] > p:
            right -= 1
        else:
            l[right],l[n//2] = l[n//2],l[right]
    while left <= n//2:
        if l[left] < p:
            left += 1
        else:
            l[left],l[n//2] = l[n//2],l[left]
            p = l[n//2]
            left += 1
    return l
        
            
print(iterative_quicksort([1,2,3,4,5,6,7,8,9,0]))
