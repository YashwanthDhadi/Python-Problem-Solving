def pattern(n):
    for i in range(n,0,-1):
        print(' '*(n-i),end="")
        print('*'*(2*i-1))

n = 5
pattern(n)
