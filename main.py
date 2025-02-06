from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=600, height=500)
user_bet = screen.textinput(title="Make your own Bet red,orange,blue,green.purple,pink.yellow", prompt="Which turtle will win the race? Enter your color")
colors = ["red", "orange", "blue", 'green', 'yellow', 'purple', 'brown']
y_positions = [-70, -40, -10, 20, 50, 80, 110]
all_turtles = []
turtle_shapes = ["square", "turtle", "circle", "triangle"]# random shapes
#id u dont want random shapes just remove the list and in for loop shape = random.choice(turtle_shapes) change it 

for turtle_index in range(7):
    shape = random.choice(turtle_shapes) 
    new_turtle = Turtle(shape=shape)
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-290, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 260:
            is_race_on = False
            winning_color = turtle.pencolor()
            message = Turtle()
            message.hideturtle()
            message.penup()
            message.goto(0, 0)
            if winning_color == user_bet:
                message.write(f"You win! The {winning_color} turtle is the winner!", align="center", font=("Arial", 16, "normal"))
            else:
                message.write(f"You lose! The {winning_color} turtle is the winner!", align="center", font=("Arial", 16, "normal"))

        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
