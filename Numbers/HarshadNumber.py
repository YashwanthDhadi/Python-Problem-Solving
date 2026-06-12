def HarshadNumber(n):
    temp = n
    sol =0
    while temp>0:
        digit = temp%10
        sol = sol+digit
        temp//=10
    return n%sol==0
n = 171
if HarshadNumber(n):
    print(f"{(n)} is Harshad Number. ")
else:
    print(f"{(n)} is Not a Harshad Number. ")