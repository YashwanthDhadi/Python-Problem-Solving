def decimal_Conversion(n):
    sol = 0
    power_place = 1
    while n>0:
        sol+=(n%10)*power_place
        power_place*=8
        n//=10
    return sol
n = 345
print(decimal_Conversion(n))

#--------------OR-------------

# def decimal_Conversion(n):
#     return int(str(n),8)
#
# n = 345
# print(decimal_Conversion(n))