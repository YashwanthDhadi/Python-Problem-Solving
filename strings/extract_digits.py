def extract_digits(s):
    result = []
    for i in s:
        if i.isdigit():
            result.append(i)
    return ''.join(result)

s = "abc2@67"
print(extract_digits(s))