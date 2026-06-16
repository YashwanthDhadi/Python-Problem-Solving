def count_common_characters(s1,s2):
    result1=[0]*26
    result2 = [0] * 26
    for ch in s1:
        result1[ord(ch)-ord("a")]+=1
    for ch in s2:
        result2[ord(ch)-ord("a")]+=1
    ans = []
    for i in range(26):
        if result1[i]>0 and result2[i]>0 :
            ans.append(chr(i+ord("a")))
    return ','.join(ans)

s1 = "lemon"
s2 = "orange"
print(count_common_characters(s1,s2))

