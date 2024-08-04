from turtle import Turtle ,Screen
import random

tim = Turtle()
tim.shape("turtle")
rgb = (0,0,0)

def random_color():
    r = random.uniform(0,1)
    g = random.uniform(0,1)
    b = random.uniform(0,1)
    color = (r,g,b)
    return color

angle_choice = [90,180,270,360]

## CREATE POLYGON
# for i in range(3,11):
#     num_of_sides = i
#     angle = 360/num_of_sides
#     tim.color(random.choice(colour))
#     for _ in range(num_of_sides):
#         tim.forward(100)
#         tim.left(angle)

#CREATE RANDOM WALK
# for _ in range(200):
#     tim.pensize(10)
#     tim.speed("slow")
#     tim.pencolor(random_color())
#     tim.forward(50)
#     tim.setheading(random.choice(angle_choice))

# #CREATE SPIROGRAPH
# def spirograph(size_of_gap):
#     for _ in range(int(360/size_of_gap)):
#         current_tim_heading = tim.heading()
#         tim.pencolor(random_color())
#         tim.speed("fastest")
#         tim.setheading(current_tim_heading + _)
#         tim.circle(100)
# spirograph(5)


screen = Screen()

#CREATE TURTLE DRAWING
def move_forwards():
    tim.forward(10)
def turn_right():
    tim.setheading(0)
def turn_up():
    tim.setheading(90)
def turn_left():
    tim.setheading(180)
def turn_down():
    tim.setheading(270)            
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.onkey(key="Up", fun=turn_up)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Down", fun=turn_down)
screen.onkey(key="c", fun=clear)

screen.exitonclick()