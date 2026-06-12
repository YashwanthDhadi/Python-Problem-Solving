def strongNumber(n):
    facts = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}
    temp = n
    sol =0
    while temp>0:
         digit= temp%10
         sol = sol+facts[digit]
         temp//=10
    return sol
n = 145
if n == strongNumber(n):
    print("strong Number")
else:
    print("Not a strong Number")

#--------OR----------

# def factorial(n):
#     fact =1
#     for i in range(1,n+1):
#         fact = fact* i
#     return fact
#
# def strongnumber(n):
#     temp = n
#     sol =0
#     while temp>0:
#         digit = temp%10
#         sol = factorial(digit)+sol
#         temp//=10
#     return sol
#
# n =145
# print(strongnumber(n))
