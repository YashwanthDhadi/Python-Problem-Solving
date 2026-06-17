def find_substring_index(s1,s2):
    return s1.find(s2)
s1= "takeuforward"
s2 = "forward"
print(find_substring_index(s1,s2))

#------------OR-----------------

# def find_substring_index(s1,s2):
#     for i in range(len(s1)-len(s2)+1):
#         if s2 == s1[i:len(s2)+i]:
#             return i
#     return -1
#
# s1= "takeuforward"
# s2 = "forward"
# print(find_substring_index(s1,s2))



