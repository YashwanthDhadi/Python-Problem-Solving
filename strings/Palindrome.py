def palindrome(n):
    left =0
    right = len(n)-1
    while left<right:
        if n[left]!=n[right]:
            return False
        left+=1
        right-=1
    return True
n='Yash'
if palindrome(n):
    print("palindrome")
else:
    print("Not a palindrome.")
