def next_alphabet(s):
    ans = []
    for ch in s.lower():
        if ch.isalpha():
            if ch!='z':
                ans.append(chr(ord(ch)+1))
            else:
                ans.append("a")
    return ''.join(ans)

s = "abcdxyz"
print(next_alphabet(s))

#-----------OR----------
#More optimised Time-O(n) and space-O(1) but return has no value

# def next_alphabet(s):
#     for ch in s.lower():
#         if ch.isalpha():
#             if ch!='z':
#                 print(chr(ord(ch)+1),end='')
#             else:
#                 print("a",end='')
#     return
#
# s = "abcdxyz"
# next_alphabet(s)

