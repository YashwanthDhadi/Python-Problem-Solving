def fibanacci(n):
    a = 0
    b = 1
    items=[]
    for i in range(n):
        items.append(a)
        a,b = b, a+b
    return items
n = 45
print(fibanacci(n))