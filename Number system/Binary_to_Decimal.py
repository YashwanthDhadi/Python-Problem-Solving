def decimal_conversion(n):
    sol = 0
    power = 1
    while n>0:
        sol +=(n%10)*power
        power=power*2
        n//=10
    return sol

n = 101011
print(decimal_conversion(n))

#----------------OR_________________

# def decimal_conversion(n):
#     return int(str(n),2)
#
# n = 101011
# print(decimal_conversion(n))
