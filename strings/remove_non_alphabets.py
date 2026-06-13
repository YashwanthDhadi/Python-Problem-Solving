def remove_nonAlpha(n):
    ans = []
    for ch in n:
        if ch.isalpha():
            ans.append(ch)
    return "".join(ans)
n = "#python12@ 3"
print(remove_nonAlpha(n))

#----------OR-------------

# def remove_nonAlpha(n):
#     for ch in n:
#         if not ch.isalpha():
#             n = n.replace(ch,'')
#     return n
# n = "#python12@ 3"
# print(remove_nonAlpha(n))








