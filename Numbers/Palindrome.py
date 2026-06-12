def palindrome(num):
    temp = num
    rev = 0
    while temp>0:
        digit = temp%10
        rev = (rev*10)+digit
        temp//=10
    if rev == num:
        return True
    else:
        return False
num = 121
if palindrome(num):
    print("Palindrome")
else:
    print("Not a palindrome")
