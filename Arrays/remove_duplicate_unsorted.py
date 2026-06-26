def remove_duplicate(arr):
    maps = set(arr)
    ans = []
    for i in arr:
        if  i in maps:
            ans.append(i)
            maps.remove(i)
    return ans

arr = [2,3,1,9,3,1,3,9]
print(remove_duplicate(arr))