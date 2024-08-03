import random
from art import logo

print(logo)

print('Welcom to the Number Guessing Game!')
print("I'm thinking the number between 1 and 100")
number = random.randint(1, 100)
print(f'Psst, the correct answer is {number}')

difficulty = input("Choose a difficulty. Type easy or hard: ")

if difficulty == 'easy':
  attempts = 10
elif difficulty == 'hard':
  attempts = 5


def checking_number(guess, num):
  if guess > num:
    print("Too High")
  elif guess < num:
    print("Too Low")
  else:
    print(f"You got it! The answer was {num}")


cont = True
while cont:
  print(f'You have {attempts} attempts remaining to guess the number.')
  guess = int(input('Make a guess: '))
  checking_number(guess, number)
  if guess == number:
    cont = False
  else:
    attempts -= 1
