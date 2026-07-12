def pattern(n):
    for i in range(1,n+1):
        # top-half
        print("*" * ((n - i) + 1), end='')
        print(' ' *(2* (i - 1)), end='')
        print("*" * ((n - i) + 1))

    for i in range(2, n + 1):
        #bottom half
        print("*"*i,end='')
        print(' ' * (2 * (n - i)), end='')
        print("*" * i)

n = 5
pattern(n)