#CHALLENGE 147
def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    return string[::-1].casefold() == string.casefold()



# run palindrome_setence before plindrome function to convert sentence into a comparable-string of characters