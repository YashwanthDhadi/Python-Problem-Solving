def count_frequently(arr):
    freq_count = {}
    for i in arr:
        if i not in freq_count:
            freq_count[i]=1
        else:
            freq_count[i] += 1
    ans =[]
    for key,value in freq_count.items():
        ans.append(f"{key}:{value}")

    return ','.join(ans)

arr = [10,5,10,15,10,5]
print(count_frequently(arr))