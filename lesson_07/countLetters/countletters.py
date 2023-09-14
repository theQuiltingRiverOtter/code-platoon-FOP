def count_letters(string: str) -> dict:
    """Returns a dictionary of count of each letter in string"""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXY"
    string = string.upper()
    letter_count = {}
    for letter in string:
        if letter in alphabet:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count


print(count_letters("AaBb"))
print(count_letters("This is the song that never ends"))
count_letters(3)
