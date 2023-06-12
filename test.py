test = input()

def removeSpaces(word):
    newWord = ""
    for letter in word:
        if ord(letter) != 32:
            newWord+=letter
    return newWord

test = test.lower()
print(test)