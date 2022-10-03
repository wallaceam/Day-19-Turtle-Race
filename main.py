from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False

user_bet = screen.textinput(title="Which turtle will win the race?", prompt="Red, orange, yellow, green, blue, "
                                                                            "or purple?").lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [165, 99, 33, -33, -99, -165]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost. The {winning_color} turtle is the winner.")
        rand_distance = random.randint(0, 15)
        turtle.forward(rand_distance)

screen.exitonclick()
