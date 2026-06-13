def palindrome(n):
    left =0
    right = len(n)-1
    while left<right:
        if n[left].lower()!=n[right].lower():
            return False
        left+=1
        right-=1
    return True
n='Madam'
if palindrome(n):
    print("palindrome")
else:
    print("Not a palindrome.")
