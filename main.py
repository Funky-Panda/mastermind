import random
import os
from tabulate import tabulate

Allcolours = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown"]

def getColours():
    randomColours = []
    
    for i in range(len(Allcolours)):
        if len(randomColours) < 4:
            randomIndex = random.randrange(0,len(Allcolours))
            randomColours.append(Allcolours[randomIndex])
    
    return randomColours


def createTable(data):
    os.system("clear")

    # Transpose the data list
    transposed_data = list(map(list, zip(*data)))

    table_headers = [f"Attemp {i+1}" for i in range(len(data))]
    table = tabulate(transposed_data, headers=table_headers, tablefmt="grid")

    print(table)

def validateAttempts(correctPositions,correctColours):
    if correctPositions == 4:
        return("Hurrah!")
    elif correctColours == 4:
        return("All rights colours, wrong place")
    elif correctColours > 0:
        return(f"{correctColours} correct colour(s), wrong place")
    elif correctColours !=4:
        return("Wrong colours, wrong places")

def validateGuess(position):
    while True:
        guess = input(f"Position {position}: ")
        guess = removeSpaces(guess.lower())

        if guess not in Allcolours:
            print("please enter a valid colour")
        else:
            break

    return guess
        
def removeSpaces(word):
    newWord = ""
    for letter in word:
        if ord(letter) != 32:
            newWord+=letter
    return newWord

allColoursPicked = []
colours = getColours()

file = open("answer.txt", "w")
file.write(", ".join(colours))
file.close()

correctPositions = 0
correctColours = 0
attempts = 0
while correctPositions < 4:
    pickedColours = []
    correctPositions = 0
    correctColours = 0
    attempts+=1
    for i in range(4):
        guess = validateGuess(i+1)
        pickedColours.append(guess)
        if guess == colours[i]:
            correctPositions += 1
            correctColours+=1
        elif guess in colours:
            correctColours+=1
    allColoursPicked.append(pickedColours)
    createTable(allColoursPicked)

    
    print(validateAttempts(correctPositions,correctColours))