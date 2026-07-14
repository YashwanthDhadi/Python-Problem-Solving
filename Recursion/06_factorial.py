def rec(n):
    if n<0:
        return -1
    elif n == 0 or n == 1:
        return 1
    return n *  rec(n-1)

print(rec(5))