def palindrome(string,l,r):
    if l>=r:
        return True
    elif string[l]==string[r] :
        return palindrome(string,l+1,r-1)
    else :
        return False

string = 'madam'
l=0
r=len(string)-1
print(palindrome(string,l,r))