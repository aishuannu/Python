def bleft(v,l): # assumes that l is sorted
  return left(v,l,0,len(l)-1)

def left(v,l,i,j): 
  if i > j:
    return -1
  if (i == j) and v > l[i]:
    return i
  mid = (i+j)//2
  if l[mid] >= v:
    return left(v,l,i,mid-1)
  elif l[mid+1] >= v:
    return mid
  else:
    return left(v,l,mid+1,j)

