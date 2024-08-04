import colorgram
from turtle import Turtle ,Screen
import random

#EXTRACT COLOR
colors = colorgram.extract('/Users/ferdinand.sanjaya/Documents/Course/python/100_days_of_code_the_complete_python_pro_bootcamp/intermediate/hirst_painting/image.jpg', 30)
rgb_color = []
for color in colors:
    r = color.rgb.r/255
    g = color.rgb.g/255
    b = color.rgb.b/255
    rgb_color.append((r,g,b))
    # rgb_color.append(color.proportion)

# random.choice(rgb_color)
tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(135)
tim.forward(300)
tim.setheading(0)
color_number = 0
index = -1
number_of_dots = 100

for i in range (0,int(number_of_dots/10)):
    tim.dot(20,random.choice(rgb_color))
    for j in range(0,int(number_of_dots/10)):        
        tim.forward(40)
        tim.dot(20,random.choice(rgb_color))
        j += 1
    if i%2 ==0:
        tim.setheading(-90)
        tim.forward(40)
        tim.setheading(-180)
    else:
        tim.setheading(-90)
        tim.forward(40)
        tim.setheading(0)
    i +=1

screen = Screen()
screen.exitonclick()