def palindrome(num):
    for i in range(num+1):
            temp = i
            rev = 0
            while temp>0:
                digit = temp%10
                rev = (rev*10)+digit
                temp//=10
            if rev == i:
                print(i)

num = 100
palindrome(num)

