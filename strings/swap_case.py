def swap_case(s):
    result = []
    for ch in s:
        if  ch.islower():
            result.append(ch.upper())
        elif ch.isupper():
            result.append(ch.lower())
        else:
            result.append(ch)
    return ''.join(result)

s = "pytHOn is bEst"
print(swap_case(s))

#-----------OR--------------------

# def swap_case(s):
#     return s.swapcase()
# s = "pytHOn is bEst"
# print(swap_case(s))
