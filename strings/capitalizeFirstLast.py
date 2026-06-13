def capitalizeFirstLast(s):
    result=s.split()
    for i in range(len(result)):
        if len(result[i])==1:
            result[i]=result[i].upper()
        else:
            word = result[i]
            word =word[0].upper()+word[1:-1]+word[-1].upper()
            result[i]=word
    return ' '.join(result)
s = "python coding is awesome"
print(capitalizeFirstLast(s))



