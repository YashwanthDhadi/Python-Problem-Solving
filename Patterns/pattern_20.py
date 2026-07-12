def pattern(n):
    for i in range(1,n+1):
        # top-half
        print("*" * i, end='')
        print(' ' *(2* (n - i)), end='')
        print("*" * i)

    for i in range(1, n):
        #bottom half
        print("*"*(n-i),end='')
        print(' ' * (2 * i), end='')
        print("*"*(n-i))

n = 5
pattern(n)