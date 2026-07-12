def pattern(n):
    for i in range(n,0,-1):
        for j in range(i,n+1):
            print(chr(64+j),end = '')
        print()

n = 5
pattern(n)