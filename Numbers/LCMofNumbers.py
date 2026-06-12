def LCM(a,b):
    t1,t2 = a,b
    while t2:
        t1,t2 = t2,t1%t2
    t1 = (a*b)//t1
    return t1
a = 15
b = 20
print(f"LCM of {(a,b)} is {LCM(a,b)}.")