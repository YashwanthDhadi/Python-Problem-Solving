def factors(n):
    factors = []
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            factors.append(i)
            if n!=1 and i!=n//i:
                factors.append(n//i)
    factors.sort()
    return factors
n = 24
print(factors(n))