import turtle
import pandas


image = "blank_states_img.gif"


screen = turtle.Screen()
screen.addshape(image)


turtle.shape(image)


states = pandas.read_csv("50_states.csv")
list_states = states.state.to_list()

guessd = []

while len(guessd) < 50:
    answer_box = screen.textinput(title=f"{len(guessd)}/50 correct! Guess the state", prompt="type the state name").title()

    if answer_box == "Exit":
        missing_states = [state for state in list_states if state not in guessd]
        # missing_states = []
        # for state in list_states:
        #     if state not in guessd:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        print(missing_states)
        break

    if answer_box in list_states and answer_box not in guessd:
        guessd.append(answer_box)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == answer_box]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_box)

