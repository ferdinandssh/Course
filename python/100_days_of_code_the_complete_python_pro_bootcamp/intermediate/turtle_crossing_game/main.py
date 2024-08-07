import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up",fun=player.up)
screen.onkey(key="Down",fun=player.down)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    #COLLISION WITH CAR
    for car in car_manager.all_cars:
        if player.distance(car)<20:
            game_is_on = False
            scoreboard.game_over()
    
    #COLLISION WITH FINISH
    if player.ycor() == 300:
        player.go_to_start_position()        
        car_manager.upgrade_speed()
        scoreboard.upgrade_level()
        scoreboard.update_scoreboard()


screen.exitonclick()