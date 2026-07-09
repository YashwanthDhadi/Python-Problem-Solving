def pattern(n):
    c = 1
    for i in range(n-1,-1,-1):
        for j in range(i+1):
            print(' ',end ='')
        for j in range(1,c+1):
            print("*",end='')
        c+=2
        print()

n = 5
pattern(n)

#OR
# def pattern(n):
#     for i in range(1,n+1):
#         print(' '*(n-i),end='')
#         print('*'*(2*i-1))
#
# n = 5
# pattern(n)
