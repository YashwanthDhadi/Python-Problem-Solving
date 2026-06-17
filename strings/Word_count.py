def word_count(s):
    count=1
    for i in range(len(s)):
        if s[i]==" "  :
            count+=1
    return count
s = "Python is executable pseudocode"
print(word_count(s))

#-----OR-------
#With using split() build in function

# def word_count(s):
#     return len(s.split())
# s = "Python is executable pseudocode"
# print(word_count(s))
