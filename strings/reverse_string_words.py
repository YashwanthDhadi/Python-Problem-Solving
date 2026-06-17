def reverse_string_words(s):
    result = []
    current_word=''
    i = len(s)-1
    while i>-1:
        if s[i]!=" ":
            current_word=s[i]+current_word
            i-=1
        else:
            if current_word:
                result.append(current_word)
                current_word=''
            i-=1
    if current_word:
        result.append(current_word)
    return " ".join(result)

s = "python is executable pseudo code"
print(reverse_string_words(s))

#============OR-----------------

# def reverse_string_words(s):
#     ans =''
#     word=''
#     i = len(s)-1
#     while i>-1:
#         if s[i]!=" ":
#             word = s[i] + word
#             i-=1
#         else:
#             ans+=word+" "
#             word = ''
#             i-=1
#     ans+=word
#     return ans
# s = "python is executable pseudo code"
# print(reverse_string_words(s))

