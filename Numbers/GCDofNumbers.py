def gcd(n1,n2):
    while n1!=n2:
        if n1>n2:
            n1=n1-n2
        else:
            n2=n2-n1
    return n1

n1 = 474
n2=20
print(f"GCP is for {(n1,n2)} is {gcd(n1,n2)}")

#------or-----
# def gcd(n1,n2):
#     while n2:
#         n1,n2 = n2,n1%n2
#     return n1
# n1,n2 = 474,20
# print(f"GCP is for {(n1,n2)} is {gcd(n1,n2)}")
