def char_count(s):
    result = {}
    for ch in s.lower():
        if ch not in result :
            result[ch]=1
        else:
            result[ch]+=1
    for ch in result:
        print(f"{ch}:{result[ch]}",end=' ')
    return
s = "Approach"
char_count(s)

#----------OR---------
# Below using ASCII method and the optimised solution

# def char_count(S):
#     items=[0]*26
#     for ch in s.lower():
#         items[ord(ch)-ord('a')]+=1
#     for i in range(26):
#         if items[i]!=0:
#             print(f"{chr(i+ord('a'))}-{items[i]}",end = "  ")
#     return
#
# s = "Approach"
# char_count(s)


