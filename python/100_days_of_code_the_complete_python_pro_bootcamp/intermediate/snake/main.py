from turtle import Turtle ,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

snake = Snake()
food = Food()
score_board = Scoreboard()

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My snake game")

screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)


game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()
    #SNAKE EATING FOOD
    if snake.snake_head.distance(food) < 15:
        food.refresh_food()
        score_board.plus_score()
        snake.extend()
    
    #DETECT COLLISION WITH WALL
    if snake.snake_head.xcor()>280 or snake.snake_head.xcor()<-295 or snake.snake_head.ycor()>295 or snake.snake_head.ycor()<-295:       
        game_is_on = False
        score_board.game_over()
    
    #DETECT COLLISION WITH TAIL
    for segment in snake.segments[1:]:
        # if segment == snake.snake_head:
        #     pass
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()







screen.exitonclick()







