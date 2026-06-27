def replace_elements_by_rank(arr):
    sorted_temp = arr.copy()
    sorted_temp.sort()
    maps = {}
    rank = 1
    for i in sorted_temp:
        if not i in maps:
            maps[i]=rank
            rank+=1
    for i in range(len(arr)):
        arr[i]=maps[arr[i]]
    return arr

arr = [20,15,26,2,98,6]
print(replace_elements_by_rank(arr))