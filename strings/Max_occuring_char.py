def Max_Occuring_Char(s):
    result=[0]*26
    for ch in s.lower():
        result[ord(ch)-ord('a')]+=1
    ans = result.index(max(result))
    return chr(ans+ord("a"))

s = 'Elephant'
print(Max_Occuring_Char(s))