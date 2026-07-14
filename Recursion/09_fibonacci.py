def fabinacci(n,a,b):
    if n==0:
        return 0
    elif n == 1:
        return b
    a, b = b, a + b
    return fabinacci(n-1,a,b)

n = 6
print(fabinacci(n,0,1))

#---------OR-----------

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# print(fibonacci(5))