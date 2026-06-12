def GPseries(a,n,d):
    if r == 1:
        return a * n
    total = a*(1-r**n)/(1-r)
    return total
a = 3
n = 8
r = 1
print(GPseries(a,n,r))
