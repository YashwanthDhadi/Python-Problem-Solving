def removeBrackets(n):
    result = []
    for ch in n:
        if ch not in "()":
            result.append(ch)
    return ''.join(result)
n = "(((a-b))+c)"
print(removeBrackets(n))

#-----OR----------

# def removeBrackets(n):
#     n = n.replace('(','').replace(')','')
#     return n
# n = "(((a-b))+c)"
# print(removeBrackets(n))
