def pattern(n):
    size = n*2
    for i in range(size):
        for j in range(size):
            top = i
            left = j
            bottom = size-1-i
            right = size-1-j
            layer = min(top,left,bottom,right)
            print(n-layer,end ='')
        print()

n = 5
pattern(n)