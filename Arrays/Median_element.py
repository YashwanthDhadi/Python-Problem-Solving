def median_element(arr):
    arr.sort()
    n = len(arr)
    mid = n//2
    if n%2==0:
        return (arr[mid]+arr[mid-1])/2
    else:
        return arr[mid]

arr = [2,4,1,3,5]
print(median_element(arr))