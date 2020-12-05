import random

word_list="hello tree flower bread pizza jazz soccer school money python paper rain bottle pencil remote book hangman".split()


def choose_word():
    word = random.choice(word_list)
    return word.upper()                                                         #turns words to upper case


def play(word):
    letter_length = "_" * len(word)                                             #Allows for player to see how long the word is
    guessed = False
    guessed_letters = []                
    guessed_words = []                  
    tries = 6                                                                   #Player gets 6 tries to guess the word
    print("Let's play Hangman!")
    name=str(input("What is your name? "))
    print("Well lets get started ", name)
    print(hangman_graphic(tries))       
    print(letter_length)               
    print("\n")

    while not guessed and tries > 0:   
        guess = input("Please guess a letter or word: ").upper()    
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:                                        #If player guessed a repeated letter
                print("You already guessed the letter", guess)
            elif guess not in word:                                             #If player guessed a letter not in the word
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:                                                               #If user guessed letter in word
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                letters_listed = list(letter_length)                            #Displays correct letter in correct place for player to see
                spaces = [i for i, letter in enumerate(word) if letter == guess]
                for index in spaces:
                    letters_listed[index] = guess
                letter_length = "".join(letters_listed)
                if "_" not in letter_length:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():                       #If user guessed word already
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:                                                  
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                letter_length = word
        else:                                                                   #Guesses something other than a letter    
            print("Not a valid guess.")

        print(hangman_graphic(tries))
        print(letter_length)
        print("\n")

    if guessed:
        print("Congrats, you guessed the word! You win!")                       #If user wins
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!") #If user loses
                
        

def hangman_graphic(tries):                                                     #Allows for hangman to be displayed after each guess & when game starts
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


def main():                                                             #Allows user the option to play again
    word = choose_word()
    play(word)
    while input("Would you like to play again? 'Y' for yes or 'N' for no").upper() == "Y":
        word = choose_word()
        play(word)
        
if __name__ == "__main__":
    main()
