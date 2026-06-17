def string_dups(s):
    result = [0]*26
    for ch in s.lower():
        result[ord(ch)-ord("a")]+=1
    for i in range(26):
        if result[i]>1:
            print(f"{chr(i+ord('a'))}:{result[i]}",end=' ')
    return
s = "sinstriiintng"
string_dups(s)
