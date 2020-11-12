import random

word_list="hello jazz soccer school money python".split()


def choose_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    letter_length = "_" * len(word) #provides '-' where an unknown letter is
    guess = False
    guessed_letters = []                #all guessed letters go into array, so they can be checked later to see if they have already been used
    guessed_words = []                  #used when user guesses work right
    tries = 6                           #user gets 6 tries
    print("Let's play Hangman!")
    name=str(input("What is your name? "))
    print("Well lets get started ", name)
    print(hangman_graphic(tries))       #will display hangman when game starts
    print(letter_length)                #display letter length using '-'
    print("\n")

    while not guess and tries > 0:   #this while loop will include all senarios that can happen during the game (loop will end whne there are 0 tries and guesses left 


        #turn users guess into uppercase 
        #if statement if user guessed a repeated letter
            #if user guesses incorrect letter
            #if user guesses something other than a letter
            #if user guesses a correct letter
        #if user guesses correct word



def hangman_graphic(tries):             #lists out the different stages of getting a word wrong (will be referred to in while loop)
    levels = ["""                       
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / /
                   -
                ""","""
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     /
                   -
                ""","""
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |
                   -
                ""","""
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |
                   -
                ""","""
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                ""","""
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """, """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """]
    return levels[tries]


def main():                     #this will be the main function, used to get a word and ask if the user wants to play again
    word = get_word()
    play(word)
    while input("Would you like to play again? 'Y' for yes or 'N' for no").upper() == "Y":
        word = get_word()
        play(word)

