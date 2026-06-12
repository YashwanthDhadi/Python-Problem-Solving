def perfect(n):
    sol=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            sol+=i
            if i!=1 and i!=n//i:
                sol+= n//i
    if sol == n:
        print("perfect number")
    else:
        print("Not a perfect")
n = 28
perfect(n)


