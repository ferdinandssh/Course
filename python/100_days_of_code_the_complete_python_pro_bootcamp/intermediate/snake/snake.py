from turtle import Turtle
START_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]
    
    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)
    
    def add_segment(self,position):        
        snake = Turtle("square")
        snake.speed("fastest")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.segments.append(snake)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        for seg_number in range(len(self.segments)-1,0,-1):
            next_segment_x = self.segments[seg_number-1].xcor()
            next_segment_y = self.segments[seg_number-1].ycor()
            self.segments[seg_number].goto(next_segment_x,next_segment_y)
        self.snake_head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)
    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)
    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)
    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)




