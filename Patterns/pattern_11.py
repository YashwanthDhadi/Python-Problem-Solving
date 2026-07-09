def pattern(n):
    for i in range(1,n+1):
        for j in range (i):
            print((j+i)%2,end='')
        print()

n = 5
pattern(n)