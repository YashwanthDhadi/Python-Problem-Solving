def primefactors(n):
    factors = set()
    divisor = 2
    while divisor*divisor<=n: #or divisor<int(n**0.5)+1:
        if n % divisor==0:
            factors.add(divisor)
            n= n//divisor
        else:
            divisor+=1
    if n>1:
        factors.add(n)

    factors = ','.join(map(str,factors))

    return factors

n = 24
print(primefactors(n))

# --------OR----------

# def primefactors(n):
#     factors = []
#     for i in range(1,int(n**0.5)+1):
#         if n%i==0:
#             factors.append(i)
#             if i!=1 and i!=n//i:
#                 factors.append(n//i)
#     new_items =[]
#     for num in factors:
#         if  is_prime(num):
#             new_items.append(num)
#     return new_items
#
# def is_prime(n):
#     if n<2:
#         return False
#     else:
#         for i in range(2,n):
#             if n%i==0:
#                 return False
#         return True
# n = 24
# print(primefactors(n))