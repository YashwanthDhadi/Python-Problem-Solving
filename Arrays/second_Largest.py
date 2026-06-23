def second_largest(arr):
    large = float("-inf")
    second_large = float("-inf")
    for i in arr:
        if i>large:
            second_large = large
            large = i
        elif i>second_large and i!= large:
                second_large = i
    return second_large

arr = [2, 5, 1, 45, 6, 9]
print(second_largest(arr))