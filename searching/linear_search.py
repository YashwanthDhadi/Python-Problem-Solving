def linear_saarch(arr,key):
    for i in range(len(arr)):
        if key == arr[i]:
            return i
    return -1
arr = [3,5,1,8,42,0]
key = 8
print(linear_saarch(arr,key))