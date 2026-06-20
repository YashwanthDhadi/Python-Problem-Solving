def numbers_in_words(number):
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                  "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    thousand = number//1000
    hundred = (number%1000)//100
    two_digits = number%100
    word = []
    if thousand>0:
        word.append(ones[thousand])
        word.append("thousand")
    if hundred>0:
        word.append(ones[hundred])
        word.append("hundred")
    if two_digits<=9:
            word.append(ones[two_digits])
    elif 10<=two_digits<=19:
            word.append(teens[two_digits%10])
    else:
        if two_digits%10!=0:
            word.append(tens[two_digits//10])
            word.append(ones[two_digits%10])
        else:
            word.append(tens[two_digits//10])

    return ' '.join(word)


number = 458
print(numbers_in_words(number))
