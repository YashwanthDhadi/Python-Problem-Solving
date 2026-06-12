def NumCheck(n):
    small = float("inf")
    maxi = float("-inf")
    while n>0:
        digit=n%10
        n//=10
        if maxi<digit:
            maxi = digit
        if small>digit:
            small = digit
    return  maxi,small

n = 5288
maxi,mini = NumCheck(n)
print(f"maximun is {maxi}")
print(f"manimun is {mini}")

