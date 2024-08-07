from turtle import Turtle

file_path = "/Users/ferdinand.sanjaya/Documents/Course/python/100_days_of_code_the_complete_python_pro_bootcamp/intermediate/snake/data.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(file_path,mode = 'r') as file:
            self.contents = int(file.read())
        self.high_score = self.contents
        self.color("white")        
        self.penup()
        self.goto(0,270)        
        self.hideturtle()        
        self.speed("fastest")   
        self.update_scoreboard()    
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align="center", font = ("Arial",24,"normal"))        

    def plus_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()
    
    def reset_score_board(self):
        if self.score > self.high_score:
            self.high_score = self.score            
            with open(file_path,mode = 'w') as file:
                file.write(str(self.high_score))
        self.score = 0   
        self.update_scoreboard()

    def game_over(self):        
        self.goto(0,0)        
        self.write(f"GAME OVER! Your score is {self.score}", align="center", font = ("Arial",24,"normal"))        
    
        
