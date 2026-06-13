def vowel_pop(n):
    ans = ''
    for ch in n:
        if ch.lower() not in "aeiou":
            ans+=ch
    return ans
n = "Breakfast"
print(vowel_pop(n))


#-------OR--------

# def vowel_pop(n):
#     ans = []
#     for ch in n:
#         if ch.lower() not in "aeiou":
#             ans.append(ch)
#     return ''.join(ans)
# n = "Breakfast"
# print(vowel_pop(n))
