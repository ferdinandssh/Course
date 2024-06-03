import random

def play():
    user = input (f"'r' for rock, 'p' for paper, 's' for scissors:\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print(f"It is a tie, computer choose {computer} and you choose {user}.")
    elif is_win(user, computer):
        print(f"You won, computer choose {computer} and you choose {user}.")
    
    print(f"You lost, computer choose {computer} and you choose {user}.")


def is_win(player1, player2):
    if (player1 == 'r' and player2 =='s') or (player1 == 's' and player2 =='p') or (player1 == 'p' and player2 =='r'):
        return True

print(play())

