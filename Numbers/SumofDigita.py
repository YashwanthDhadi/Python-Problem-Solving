def SumOfNumbers(n):
    sol = 0
    while n>=10:
        while n>0:
            digit = n%10
            sol+=digit
            n//=10
        n = sol
        sol = 0
    return n
n = 78
print(SumOfNumbers(n))

#----OR-------
# formula is 1+(n-1)%9

# def SumofNumbers(n):
#     n-=1
#     while n>=10:
#         n = 1+(n%9)
#     return n
# n = 78
# print(SumofNumbers(n))

