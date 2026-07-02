def binary_saarch(arr,key):
    i = 0
    j = len(arr)-1
    while i <= j :
        mid = (i+j)// 2
        if arr[mid] == key:
            return mid
        elif arr[mid]>key:
            j = mid-1
        else:
            i = mid+1
    return -1
arr = [0,1,3,5,8,12,42]
key = 8
print(binary_saarch(arr,key))