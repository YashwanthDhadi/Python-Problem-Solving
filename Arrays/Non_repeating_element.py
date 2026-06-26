def non_repeating_element(arr):
    maps = {}
    for val in arr:
        if not val in maps:
            maps[val]=1
        else :
            maps[val]+=1
    ans = []
    for key,value in maps.items():
        if maps[key]==1:
            ans.append(key)
    return ans

arr = [1,1,2,3,4,4,5,2]
print(non_repeating_element(arr))