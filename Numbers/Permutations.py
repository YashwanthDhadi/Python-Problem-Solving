def permutations(n,r):
    if n<0 or r<0 or r>n:
        return "Invalid input"
    p = 1
    for i in range(r):
        p = p*(n-i)
    return p
n = 5
r = 3
print(permutations(n,r))

