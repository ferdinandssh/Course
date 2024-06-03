import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set (string.ascii_uppercase)
    user_guessed = set() #what user has guessed
    lives = 10


    while len(word_letters) > 0 and lives > 0:
        print(f"You have", lives, "lives left.\n", 'You have used these letters:',' '.join(user_guessed),'\n')
        
        #what current word is
        word_list = [letter if letter in user_guessed else '-' for letter in word]
        print('Current word is ',''.join(word_list))
        
        #getting user input
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - user_guessed:
            user_guessed.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('letter is not in word')
        
        elif user_letter in user_guessed:
            print("You have guessed the character. Please try again\n")
        
        else:
            print("Invalid character. Please try again\n")

    #End of hangman
    if lives == 0:
        print("\nYou died. The word was",word)
    else: print('\nCorrect, you have guessed the words',word)

hangman()