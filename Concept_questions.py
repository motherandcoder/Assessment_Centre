def is_isogram(word):
    word = word.lower()
    unique_chars = set()

    for char in word:
        if char in unique_chars:
            return False
        else:
            unique_chars.add(char)

    return True


# Prompt the user to enter a word
user_input = input("Enter a word: ")

# Call the is_isogram function with the user's input and print the result False/True
print(is_isogram(user_input))

