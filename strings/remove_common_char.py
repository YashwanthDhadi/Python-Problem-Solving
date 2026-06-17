def remove_common_char(s1,s2):
    seen = set(s2.lower())
    ans = []
    for ch in s1.lower():
        if not ch in seen:
            ans.append(ch)
    return "".join(ans)
s1 = "abcdef"
s2 = "cefz"
print(remove_common_char(s1,s2))