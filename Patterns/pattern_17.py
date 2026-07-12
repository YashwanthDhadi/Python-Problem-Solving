def pattern(n):
    for i in range(1,n+1):
        for _ in range((n-i)+1):
            print(" ",end = '')
        for j in range(1,i):
            print(chr(64+j),end='')
        for j in range(i,0,-1):
            print(chr(64+j),end='')
        print()

n = 5
pattern(n)