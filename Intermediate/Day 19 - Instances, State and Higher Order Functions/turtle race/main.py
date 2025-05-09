from turtle import Turtle, Screen
import random
import tkinter as tk
from tkinter import messagebox

def start_race():
    is_race_on = False
    screen = Screen()
    screen.setup(width=500, height=400)

    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color: ")
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_positions = [-70, -40, -10, 20, 50, 80]
    all_turtles = []

    for i in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[i])
        new_turtle.goto(x=-230, y=y_positions[i])
        all_turtles.append(new_turtle)


    if user_bet:
        is_race_on = True

    while is_race_on:
    # random_distance = random.randint(0, 10)
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    #print(f"You won! The {winning_color} turtle is the winner!")
                    messagebox.showinfo("Race Result", f"You won! The {winning_color} turtle is the winner!")
                else:
                    #print(f"You lost! The {winning_color} turtle is the winner!")
                    messagebox.showinfo("Race Result", f"You lost! The {winning_color} turtle is the winner!")
                play_again = messagebox.askyesno("Play Again", "Do you want to play again?")

                if play_again:
                    screen.clearscreen()
                    start_race()
                else:
                    screen.bye()
                return
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

start_race()