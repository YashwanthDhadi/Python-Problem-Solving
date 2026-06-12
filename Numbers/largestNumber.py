def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c

a = 10
b = 20
c = 30
print(largest(a,b,c))

#//Built-in function method//

# def largest(a,b,c):
#     return max(a,b,c)
# a = 10
# b = 20
# c = 30
# print(largest(a,b,c))



