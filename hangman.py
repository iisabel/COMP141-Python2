#!/bin/python3
import random

word_list = ["hello", "jazz", "soccer", "school", "money", "python"]

def play():
    print("Welcome to Hangman!");
    guess = input("\nGuess a letter:\n");
    print(f'You guessed the letter: {guess}')
play()

ef hangman_figures():      #prints hangman after each incorrect guess
    if (guesses == 0):
        print ("--------- ")
        print ("|       | ")
        print ("|         ")
        print ("|         ")
        print ("|         ")
        print ("|         ")
        print ("|         ")
    elif (guesses == 1):
        print ("--------- ")
        print ("|       | ")
        print ("|       O ")
        print ("|         ")
        print ("|         ")
        print ("|         ")
        print ("|         ")
     elif (guesses == 2):
        print ("--------- ")
        print ("|       | ")
        print ("|       O ")
        print ("|       | ")
        print ("|       | ")
        print ("|         ")
        print ("|         ")
     elif (guesses == 3):
        print ("--------- ")
        print ("|       | ")
        print ("|       O ")
        print ("|      \| ")
        print ("|       | ")
        print ("|         ")
        print ("|         ")
     elif (guesses == 4):
        print ("--------- ")
        print ("|       | ")
        print ("|       O ")
        print ("|      \|/")
        print ("|       | ")
        print ("|         ")
        print ("|         ")
~    elif (guesses == 5):
        print ("--------- ")
        print ("|       | ")
        print ("|       O ")
        print ("|      \|/")
        print ("|       | ")
        print ("|      /  ")
        print ("|         ")
~    elif (guesses == 6):
        print ("--------- ")
        print ("|       | ")
        print ("|       O ")
        print ("|      \|/")
        print ("|       | ")
        print ("|      / \ ")
        print ("The Hangman has been completed, you LOSE!\n")
        print ("The word was: \n")
        print ("If you would like to play again enter 1, if you would like to quit enter 0\n")
