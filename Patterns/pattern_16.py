def pattern(n):
    for i in range(1,n+1):
        for _ in range(i):
            print(chr(64+i),end='')
        print()

n = 5
pattern(n)