def binary_conversion(n):
    binary_value = ''
    if n==0:
        return 0
    while n>0:
        binary_value=str(n%2)+binary_value
        n//=2
    return binary_value


n = 18
print(binary_conversion(n))