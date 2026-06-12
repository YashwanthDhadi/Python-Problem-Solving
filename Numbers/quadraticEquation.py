def quadratic(a,b,c):
    D = (b**2)-(4*a*c)
    if D == 0:
        root1=root2 = (-b)/(2*a)
    elif D>0:
        root1= (-b+(D**0.5))//(2*a)
        root2 = (-b-(D**0.5))//(2*a)
    else:
        real_root = -b//(2*a)
        img_root = ((-D)**0.5)//(2*a)
        root1 = complex(real_root,img_root)
        root2 = complex(real_root,img_root)
    return root1,root2

a = 1
b = -3
c = -10
print(quadratic(a,b,c))

#OR

# import cmath
#
# def quadratic(a,b,c):
#     D = (b**2) - (4*a*c)
#     if D == 0:
#         root1=root2 = (-b)/(2*a)
#     elif D>0:
#         root1= (-b+cmath.sqrt(D))/(2*a)
#         root2 = (-b-cmath.sqrt(D))/(2*a)
#     else:
#         real_root = -b/(2*a)
#         img_root = (cmath.sqrt(-D))/(2*a)
#         root1 = complex(real_root,img_root)
#         root2 = complex(real_root,img_root)
#     return root1,root2
#
# a = 1
# b = 3
# c = 10
# print(quadratic(a,b,c))