from words_reference import *
import random

#choose variable
lives = 6
end_game = False
historical_input = []
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(f"the chosen word is {chosen_word}")

word_display = []
for _ in range(word_length):
    word_display += "_"



while not end_game:
  #input guess
  valid_input = False
  while not valid_input:
    guess = input("Guess a letter: ").lower()
    if guess.isalpha() and len(guess) == 1:
      if guess in historical_input:
        print(f"You have already guessed {guess}.")
      else:
        historical_input.append(guess)
        valid_input = True
    else:
      print("Invalid input.")

  #check if guess is in chosen word
  for character in range(0,word_length):
    if chosen_word[character] == guess:
      word_display[character] = guess
  print(word_display)

  #reduce live if guess is not in chosen_word
  if guess not in chosen_word:
    lives -=1
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    print(f"You have {lives} lives left.")

  if lives == 0:
    print("You lose!")
    end_game = True

  if '_' not in word_display:    
    print("You win!")
    end_game = True








