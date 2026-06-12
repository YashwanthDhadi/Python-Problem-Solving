def large(arr):
    large = arr[0]
    for i in arr:
        if i>large:
            large = i
    return large
arr = [2,5,1,45,6,9]
print(large(arr))
