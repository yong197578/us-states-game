import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []


def write_state_on_map(state_name, color="black"):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.color(color)
    state_data = data[data.state == state_name]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(state_name, font=("Arial", 10, "normal"))


while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 Guess the State", prompt="Please print state's name").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states, columns=["state"])
        new_data.to_csv("learn.csv", index=False)
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        write_state_on_map(answer_state)

# Show missed states in red
for state in missing_states:
    write_state_on_map(state, color="red")

screen.mainloop()  # Keep the turtle screen open until closed by user
