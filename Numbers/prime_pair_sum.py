def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def sumofNumbers(n):
    for i in range(2,n+1):
        n1 = n-i
        if prime(n1) and prime(i):
            return True
    return False

n=74
print(sumofNumbers(n))
