def prime(num):
    if num<=1:
        print("Not a prime")
        return
    else:
        for i in range(2,num):
            if num%i==0:
                print("Not a prime")
                return
        print("Prime")
        return 
num = 9
prime(num)