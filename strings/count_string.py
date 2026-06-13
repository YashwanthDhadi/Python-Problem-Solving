def countstring(n):
    v_count = s_count = c_count= 0
    for ch in n:
        if ch.lower() in "aeiou":
            v_count+=1
        elif ch == ' ':
            s_count+=1
        elif ch.isalpha():
            c_count+=1
    return v_count,c_count,s_count

n = "Madam I'm Adam"
v_count,c_count,s_count = countstring(n)
print(f"Vowels = {v_count}, consonants = {c_count}, spaces = {s_count}.")

