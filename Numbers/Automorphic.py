def Automorphic(n):
    temp = n**2
    sol = ''
    for i in range(len(str(n))):
        digit = temp%10
        sol = str(digit) + sol
        temp//=10
    if int(sol) == n:
        return True
    else:
        return False

n = 376
if Automorphic(n):
    print("Automorphic")
else:
    print("Not an Automorphic")

#-------OR-------
# def Automorphic(n):
#     k = len(str(n))
#     return (n*n)%(10**k)==n
#
# n = 376
# if Automorphic(n):
#     print("Automorphic")
# else:
#     print("Not an Automorphic")
