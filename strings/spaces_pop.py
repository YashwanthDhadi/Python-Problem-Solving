def Removespaces(n):
    ans =[]
    for ch in n:
        if ch != " ":
            ans.append(ch)
    return ''.join(ans)
n = " pyt hon   "
print(Removespaces(n))

