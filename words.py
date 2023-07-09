def print_upper_words(words):
    """Print out each word on a seperate line, uppercased"""

    for word in words:
        print(word.upper())

def print_upper_words2(words):
    """Print only uppercased words that start with the letter "E" or "e" """

    for word in words:
        if word.startswith("E") or word.startswith("e"):
            print(word.upper())

def print_upper_words3(words, must_start_with):
    """Print uppercased words that start with the first letter of a word that has been given"""

    for word in words: 
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break #break tag is used to break out of the inner loop, that way the function avoids unnecessary iterations and improves efficiency.


