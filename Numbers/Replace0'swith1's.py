def replacement(n):
    if n ==0:
        return 1
    temp = n
    sol =''
    while temp>0:
        digit = temp%10
        if digit == 0 :
            digit=1
        sol= str(digit)+sol
        temp//=10
    return sol

n = 7500450
print(replacement(n))

