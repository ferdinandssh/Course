from replit import clear
import random
from art import logo,vs
from game_data import data

print(logo)

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def higher(account_a,account_b):
  if account_a["follower_count"] > account_b["follower_count"]:
    return "a"
  else:
    return "b"

def game():
  cont = True
  score = 0
  while cont:
    if score == 0:
      a = get_random_account()          
    b = get_random_account()
    while a == b:
      b = get_random_account()



    a_detail = format_data(a)
    b_detail = format_data(b)

    print(f"Compare A: {a_detail}/n")
    print(vs)
    print(f"Compare B: {b_detail}/n")

    guess = input('Who has more followers? Type "A" or "B": ')

    if guess.lower() == higher(a,b):
      score +=1
      clear()
      print(f'You are right!, your current score {score}')
      if higher(a,b) == 'b':
        a = b
    else:
      cont = False
      print(f'You are wrong!, your final score is {score}')

game()