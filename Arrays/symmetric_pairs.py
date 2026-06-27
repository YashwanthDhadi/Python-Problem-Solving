def symmetric_pair(arr):
    maps = {}
    for i in arr:
        first, second = i
        if second in maps and maps[second]==first:
            print(f"{first,second}",end = " ")
        else:
            maps[first]=second
    return

arr = [(1,2),(2,1),(3,4),(4,5),(5,4)]
symmetric_pair(arr)