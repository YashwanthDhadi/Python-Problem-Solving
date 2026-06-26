def mid_descending(n):
    n.sort()
    mid  = len(n) //2
    left = mid
    right = len(n)-1
    while left < right:
        n[left],n[right]=n[right],n[left]
        left+=1
        right-=1
    return n

n= [8,7,1,6,5,9]
print(mid_descending(n))



