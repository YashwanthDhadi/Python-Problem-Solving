def count_repeated_letters(word):
    frequency = [0] * 26
    repeated_letter_count = 0
    for ch in word:
        frequency[ord(ch) - ord('a')] += 1
    for count in frequency:
        if count > 1:
            repeated_letter_count += 1
    return repeated_letter_count

def find_word_with_highest_repeats(sentence):
    words = sentence.split()
    best_word = ""
    highest_repeat_count = 0
    for word in words:
        current_repeat_count = count_repeated_letters(word)
        if current_repeat_count > highest_repeat_count:
            highest_repeat_count = current_repeat_count
            best_word = word
    if highest_repeat_count == 0:
        return -1
    return best_word

sentence = "abcdefg google microsoft"
print(find_word_with_highest_repeats(sentence))