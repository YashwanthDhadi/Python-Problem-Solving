def remove_duplicates_string(s):
    check = set()
    result = []
    for i in range(len(s)):
        if not s[i] in check:
            check.add(s[i])
            result.append(s[i])
    return ''.join(result)
s = "abcaddgh"
print(remove_duplicates_string(s))

#why set over list ?
#set directly checks the value while list checks one by one using index
#saves time complexity O(n) to O(1) in specific line