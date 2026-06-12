def leap(n):
    return (n%4==0 and n%100!=0) or (n%400==0)
n = 2025
if leap(n):
    print("Leap")
else:
    print("Not a leap")


# def leap(n):
#     if (n%4==0 and n%100!=0) or (n%400==0):
#         return True
# n = 2024
# if leap(n):
#     print("Leap")
# else:
#     print("Not a leap")
