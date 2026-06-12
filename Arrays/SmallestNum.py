def smallest(arr):
    small = arr[0]
    for i in arr:
        if i<small:
            small = i
    return small
arr = [2,5,1,45,6,9]
print(smallest(arr))
