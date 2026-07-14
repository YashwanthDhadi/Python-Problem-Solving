def rec(n):
    if n == 0:
        return 0
    return n+rec(n-1)

print(rec(5))
