def APseries(a,n,d):
    second_term = (n - 1) * d
    total  = n * (a+second_term/2)
    return total
a = 8
n = 2
d = 5
print(APseries(a,n,d))