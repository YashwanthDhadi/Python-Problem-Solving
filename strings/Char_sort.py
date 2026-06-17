def char_sort(s):
    result = [0]*26
    for ch in s:
        if  ch.isalpha():
            result[ord(ch)-ord('a')]+=1
    ans = []
    for i in range(26):
        if result[i]>0:
            ans.append(chr(i+ord('a'))*result[i])
    return ''.join(ans)
s = "zxcbg"
print(char_sort(s))

#----------OR-------------
#
# def char_sort(s):
#     s = sorted(s)
#     return ''.join(s)
# s = "zxcbg"
# print(char_sort(s))


