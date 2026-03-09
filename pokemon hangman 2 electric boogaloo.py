import random
import csv

def readData():
    array = []
    acceptedExt = ['csv', 'txt']

    file = input('Enter file name:  ')
    
    while file.split('.')[1] not in acceptedExt:
        print('Error: file is not a .csv or .txt file.')
        file = input('Enter file name:  ')

    with open(file, 'rt') as file:
        for row in csv.reader(file):
            array.append(row[0].lower())

    return array


def game(array):
    chosenWord = array[random.randint(0, len(array) - 1)]
    noWrong = 0
    noGuesses = 0
    letter_positions = ['_'] * len(chosenWord)
    while noGuesses < len(chosenWord):
        print(letter_positions)
        guess_letter = input("Guess a letter: ")
        if guess_letter in list(chosenWord):
            for i in range(len(chosenWord)):
                if chosenWord[i] == guess_letter and letter_positions[i] == "_":
                    letter_positions[i] = guess_letter
                    noGuesses += 1
            if '_' not in letter_positions:
                print(f"You guessed the Pokemon! It was {chosenWord[0].upper() + chosenWord[1:]}!")

        else:
            print("Incorrect")
            noWrong += 1
            if noWrong == 10:
                print("You lose!")
                print("the word was " + chosenWord[0].upper() + chosenWord[1:])





pokemon = readData()
running = True
while running:
    game(pokemon)
    again = input('Would you like to play again? (y/n) ')
    while again != 'y' and again != 'n':
        print('Must be \'y\' or \'n\'')
        again = input('Would you like to play again? (y/n) ')
    if again == 'n':
        running = False
