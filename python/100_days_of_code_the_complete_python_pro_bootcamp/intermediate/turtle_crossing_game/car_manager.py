from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        i = random.randint(1,6)
        if i == 1 or i == 2:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)            
            new_car.color(random.choice(COLORS))            
            new_car.penup()
            new_car.goto(250,random.randint(-250,250))
            new_car.back       
            self.all_cars.append(new_car)
    
    def move_car(self):    
        for car in self.all_cars:
            car.backward(self.car_speed)        
    
    def upgrade_speed(self):
        for car in self.all_cars:
            self.car_speed += MOVE_INCREMENT
