def average_element(arr):
    total = 0
    length = len(arr)
    for i in arr:
        total+=i
    return total/length
arr = [1,2,3,4,5]
print(average_element(arr))

