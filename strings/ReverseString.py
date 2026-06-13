def reverse_String(n):
    ans = []
    right = len(n)-1
    for i in range(len(n)):
        ans.append(n[right])
        right-=1
    return ''.join(ans)
n= 'programming'
print(reverse_String(n))

#-------OR------------
#
# def revorsestring(n):
#     n = n[::-1]
#     return n
# n = 'programming'
# print(revorsestring(n))


