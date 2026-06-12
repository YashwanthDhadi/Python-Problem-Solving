def prime(num):
    if num<=1:
        return False
    else:
        for i in range(2,num):
            if num%i==0:
                return False
        return True
num = 20
for i in range(num+1):
    if prime(i):
        print(i)