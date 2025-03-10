# This is a sample Python script.
import turtle
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
from turtle import Turtle, Screen
screen = Screen()
user_bet = screen.textinput(title="Turtle Race", prompt="Who will win the race? :")
color = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtles = []
i = 0
for _ in color:
    _ = Turtle(shape="turtle")
    _.color(color[i])
    i += 1
    turtles.append(_)
turtle.setup(width=500,height=400)
x = -230
y = -100
for _ in turtles:
    _.penup()
    _.goto(x,y)
    y += 30
is_race_on = False
if user_bet:
    is_race_on = True
while is_race_on:
    for _ in turtles:
        _.forward(random.randint(1,10))
        if _.xcor() > 230:
            is_race_on = False
            if _.pencolor() == user_bet:
                print(f"You win, {_.pencolor()} is the winner")
            else:
                print(f"You lose, {_.pencolor()} is the winner")

screen.exitonclick()