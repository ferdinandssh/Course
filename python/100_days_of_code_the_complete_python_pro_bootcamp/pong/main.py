from turtle import Turtle ,Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My pong game")

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="Left", fun=l_paddle.up)
screen.onkey(key="Right", fun=l_paddle.down)

is_game_on = True
while is_game_on == True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #COLLISION WITH TOP AND BOTTOM WALL
    if ball.ycor()>290 or ball.ycor()<-290:
        ball.bounce_y()

    #COLLISION WITH PADDLE
    if (ball.distance(l_paddle) < 50 and ball.xcor()<-340) or (ball.distance(r_paddle) < 50 and ball.xcor()>340) :
        ball.bounce_x()
    
    #COLLISION WITH RIGHT AND LEFT WALL
    if ball.xcor()>390:
        ball.reset_position()
        scoreboard.plus_l_score()

    elif ball.xcor()<-390:
        ball.reset_position()
        scoreboard.plus_r_score()
    
    is_game_on = scoreboard.find_winner()
    

screen.exitonclick()