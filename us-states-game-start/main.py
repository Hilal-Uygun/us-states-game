import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()
states_len = []
missing_states = []
while len(states_len) < 50:
    answer = screen.textinput(title=f"{len(states_len)}/50 States Correct", prompt="What's another state's name?").title()
    if answer == "Exit":
        for stt in states:
            if stt not in states_len:
                missing_states.append(stt)
        #print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    for state_n in states:
        if answer == state_n:
            states_len.append(state_n)
            coor = data[data.state == state_n]
            new_x = coor.x.tolist()[0]
            new_y = coor.y.tolist()[0]
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(new_x, new_y)
            t.write(state_n)






# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

