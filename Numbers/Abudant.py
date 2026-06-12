def Abundant(n):
    sol = 0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            sol+=i
            if i!=1 and i!=n//i:
                sol+= n//i
    return sol>n
n = 178
if Abundant(n):
    print("Abundant")
else:
    print("Not an Abundant")