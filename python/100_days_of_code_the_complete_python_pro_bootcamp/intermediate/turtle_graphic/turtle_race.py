from turtle import Turtle ,Screen
import random


screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="make your bet", prompt = "which turtle win the race?")
colors = ["red","blue","green","purple","black","orange"]
all_turtles = []


for i in range(0,len(colors)):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230,y=90 - 30*i)
    all_turtles.append(tim)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        random_forward = random.randint(0,10)
        if turtle.pencolor() == 'red':
            turtle.forward(random_forward)
        else:
            turtle.forward(random_forward)
        if turtle.xcor()>230:
            champion = turtle.pencolor()
            if user_bet == champion:
                print(f"The winner is {champion}. Your bet is right")
            else:
                print(f"The winner is {champion}. Your bet is wrong")
            is_race_on = False


screen.exitonclick()