def anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    items = [0]*26
    for ch in s1.lower():
        items[ord(ch)-ord('a')]+=1
    for ch in s2.lower():
        items[ord(ch)-ord('a')]-=1
    for i in range(26):
        if items[i]!=0:
            return False
    return True

s1,s2 = "ACT","CAT"
print(anagram(s1,s2))

# def anagram(s1,s2):
#     if len(s1)!=len(s2):
#         return False
#     if sorted(s1)!=sorted(s2):
#         return False
#     return True
#
# s1,s2 = "ACT","CAT"
# print(anagram(s1,s2))


