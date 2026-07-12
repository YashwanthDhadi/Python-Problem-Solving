def pattern(n):
    for i in range(n):
        for j in range(1,(n-i)+1):
            print(chr(64+j),end='')
        print()

n = 5
pattern(n)