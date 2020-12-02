import random

word_list="hello tree flower bread pizza jazz soccer school money python paper rain bottle pencil remote book hangman".split()


def choose_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    letter_length = "_" * len(word) 
    guessed = False
    guessed_letters = []                
    guessed_words = []                  
    tries = 6                           
    print("Let's play Hangman!")
    name=str(input("What is your name? "))
    print("Well lets get started ", name)
    print(hangman_graphic(tries))       
    print(letter_length)               
    print("\n")

    while not guessed and tries > 0:   
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                letters_listed = list(letter_length)
                spaces = [i for i, letter in enumerate(word) if letter == guess]
                for index in spaces:
                    letters_listed[index] = guess
                letter_length = "".join(letters_listed)
                if "_" not in letter_length:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                letter_length = word
        else:
            print("Not a valid guess.")
        print(hangman_graphic(tries))
        print(letter_length)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")
                
        

def hangman_graphic(tries):             
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


def main():                     
    word = choose_word()
    play(word)
    while input("Would you like to play again? 'Y' for yes or 'N' for no").upper() == "Y":
        word = choose_word()
        play(word)
        
if __name__ == "__main__":
    main()
