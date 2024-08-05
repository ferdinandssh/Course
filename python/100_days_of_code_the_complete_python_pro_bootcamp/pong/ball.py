from turtle import Turtle
START_DIRECTION = 1
START_POSITION = (0,0)
START_SPEED = 0.04

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("slowest")
        self.penup()     
        self.setheading(START_DIRECTION)   
        self.x_move = 5
        self.y_move = 5
        self.move_speed = START_SPEED
    
    def move(self):        
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    
    def bounce_x(self):
        self.x_move = self.x_move * -1
        self.move_speed *= 0.5

    def bounce_y(self):
        self.y_move = self.y_move * -1    
    
    def reset_position(self):
        self.goto(0,0)        
        self.bounce_x()
        self.move_speed = START_SPEED


