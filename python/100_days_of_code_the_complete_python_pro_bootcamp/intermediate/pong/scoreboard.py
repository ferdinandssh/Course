from turtle import Turtle
TARGET_SCORE = 5

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")        
        self.penup()
        self.goto(0,270) 
        self.hideturtle()        
        self.speed("fastest")   
        self.update_scoreboard()
        self.winner = ""
    
    def update_scoreboard(self):
        self.write(f"{self.l_score} SCORE {self.r_score}", align="center", font = ("Arial",24,"normal"))        

    def plus_l_score(self):
        self.l_score +=1
        self.clear()
        self.update_scoreboard()
    
    def plus_r_score(self):
        self.r_score +=1
        self.clear()
        self.update_scoreboard()
    
    def find_winner(self):                
        if self.r_score == TARGET_SCORE:
            self.winner = "right"
            self.goto(0,0)
            self.write(f"GAME OVER! The winner is {self.winner}", align="center", font = ("Arial",24,"normal"))
            return False
        elif self.l_score == TARGET_SCORE:
            self.winner = "left"
            self.goto(0,0)
            self.write(f"GAME OVER! The winner is {self.winner}", align="center", font = ("Arial",24,"normal"))
            return False              
        
        return True

        
        


        
