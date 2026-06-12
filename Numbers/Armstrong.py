def Armstrong(num):
    temp = num
    sol = 0
    while 0<temp:
        digit =(temp%10)**len(str(num))
        sol = sol+digit
        temp//=10
    if sol == num:
        print("Armstrong")
    else:
        print("Not a Armstrong")
a = 153
Armstrong(a)
