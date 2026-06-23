def large(arr):
    large = float("-inf")
    for i in arr:
        if i>large:
            large = i
    return large
arr = [2,5,1,45,6,9]
print(large(arr))
