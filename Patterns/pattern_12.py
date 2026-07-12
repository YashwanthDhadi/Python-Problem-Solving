def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end='')
        print(' '*((n-i)*2),end='')
        for j in range(i,0,-1):
            print(j, end='')
        print()


n = 5
pattern(n)