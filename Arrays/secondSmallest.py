def smallest(arr):
    small = float("inf")
    second_small = float("inf")
    for i in arr:
        if i<small:
            second_small = small
            small = i
        elif i<second_small and i>small:
            second_small = i
    return second_small
arr = [2,5,1,45,6,9]
print(smallest(arr))
