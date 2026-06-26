def sum_of_elements(n):
    ans=0
    for i in n:
        ans+=i
    return ans

n = [2,5,1,1,6,0]
print(sum_of_elements(n))

#-----------OR------------------
# def sum_of_elements(n):
#     return sum(n)
# n = [2,5,1,1,6,0]
# print(sum_of_elements(n))