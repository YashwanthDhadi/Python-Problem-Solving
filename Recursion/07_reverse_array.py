def array(arr,left,right):
    if left>=right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    return array(arr,left+1,right-1)

arr = [1, 2, 3, 4, 5]
left = 0
right = len(arr)-1
array(arr,left,right)
print(arr)