def count_words(text):
    words = text.split()
    return len(words)



def count_letters(text):
    letter_counts = {}
    for char in text.lower():
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1
    return letter_counts

def sort_letters(letter_counts):
    return sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)

