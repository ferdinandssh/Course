import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "/Users/ferdinand.sanjaya/Documents/Course/python/100_days_of_code_the_complete_python_pro_bootcamp/intermediate/us_states_game/blank_states_img.gif"
file = "/Users/ferdinand.sanjaya/Documents/Course/python/100_days_of_code_the_complete_python_pro_bootcamp/intermediate/us_states_game/50_states.csv"
turtle.addshape(image)
turtle.shape(image)

score = 0
df = pd.read_csv(file)
guessed_states = []
is_game_on = True

def print_states(states,color):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.color(color)
    t.speed("fastest")
    state_data = df[df.state==states]
    t.goto(state_data.x.item(),state_data.y.item())
    t.write(state_data.state.item())


while is_game_on == True:
    answer_state = screen.textinput(title = f"{score} out of 50 States Correct",
                                    prompt="What's another state's name?").title()
    all_states = df.state.to_list()
    if answer_state in all_states:
        print_states(answer_state,"black")
        score += 1
        guessed_states.append(answer_state)
    if len(guessed_states) == 50:
        is_game_on = False

    if answer_state.lower() == "exit":
        is_game_on = False
        missing_states = [states for states in all_states if states not in guessed_states]
        for states in missing_states:
            print_states(states,"red")
        #PENGGANTI CODE DARI ISI MISSING STATES
        # missing_states = []
        # for states in all_states:
        #     if states not in guessed_states:
        #         missing_states.append(states)
                # print_states(states,"red")

#TO CLICK COORDINATE IN THE SCREEN
def get_mouse_click_coor(x,y):
    print(x,y)
turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
