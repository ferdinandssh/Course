import random
from art import logo


def get_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def calculate_score(card):
  if sum(card) > 21 and 11 in card:
    card.remove(11)
    card.append(1)
  score = sum(card)
  return score


def winner(u_score, c_score):
  if u_score == c_score:
    print("It is a draw")
  elif u_score > 21 and c_score > 21:
    print("It is a draw")
  elif u_score == 21:
    print("You win")
  elif c_score == 21:
    print("You lose")
  elif u_score > 21:
    print("You lose")
  elif c_score > 21:
    print("You win")
  elif u_score > c_score:
    print("You win")
  elif u_score < c_score:
    print("You lose")


def play_game():
  print(logo)

  user_card = []
  computer_card = []
  is_game_over = False

  for _ in range(2):
    user_card.append(get_card())
    computer_card.append(get_card())

  user_score = calculate_score(user_card)
  computer_score = calculate_score(computer_card)
  print(f"Your cards: {user_card}, current score: {user_score}")
  print(f"Computer first cards: {computer_card[0]}")

  while not is_game_over:
    #USER CONTINUES
    ask_cont = input(f'Do you want to add card? y or n: ')
    if ask_cont.lower() == 'y':
      user_card.append(get_card())
      user_score = calculate_score(user_card)

    #COMPUTER CONTINUES
    while computer_score < 17:
      computer_card.append(get_card())
      computer_score = calculate_score(computer_card)

    print(f"Your cards: {user_card}, current score: {user_score}")
    print(f"Computer cards: {computer_card}, current score: {computer_score}")

    if user_score == 21 or computer_score == 21 or user_score > 21 or computer_score > 21 or ask_cont.lower(
    ) == 'n':
      winner(user_score, computer_score)
      is_game_over = True
      break


play_game()
