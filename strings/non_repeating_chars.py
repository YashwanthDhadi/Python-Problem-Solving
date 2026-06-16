def non_repeating_chars(s):
    result = {}
    for ch in s:
        result[ch]=result.get(ch,0)+1

    ans = []
    for key,value in result.items():
        if value==1:
            ans.append(key)
    return ",".join(ans)
s = 'google'
print(non_repeating_chars(s))

#--------OR-----------
# Below using ASCII method and the optimised solution
#
# def non_repeating_chars(s):
#     items = [0]*26
#     for ch in s.lower():
#         items[ord(ch)-ord("a")]+=1
#     for i in range(26):
#         if items[i]==1:
#             print(chr(i+ord('a')),end = " ")
#     return
# s = 'google'
# non_repeating_chars(s)


