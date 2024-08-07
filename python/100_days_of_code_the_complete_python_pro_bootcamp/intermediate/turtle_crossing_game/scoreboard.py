from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1    
        self.penup()
        self.goto(-290,270)        
        self.hideturtle()        
        self.speed("fastest")   
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font = FONT)  
    
    def upgrade_level(self):
        self.level += 1
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align="center", font = FONT) 

    

