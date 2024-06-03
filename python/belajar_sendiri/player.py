import random

class Player():
    def __init__(self,letter):
        self.letter = letter


class Human(Player):
    def __init__(self,letter):
        super().__init__(letter)
    
    def get_move(self,game):        
        valid_square = False
        while not valid_square:
            square = input(f'Please input your square (0-8):')
            try:
                int_square = int(square)
                if int_square not in game.available_move():                    
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid move. Try again')
        return int_square


class Computer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    
    def get_move(self,game):
        square = random.choice(game.available_move())
        return square