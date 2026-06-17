def largest_word(s):
    a = s.split()
    large_word = ''
    for i in a:
        if len(i)>len(large_word):
            large_word=i
    return large_word

s = "Google Docs Microsoft Teams"
print(largest_word(s))


