from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

#Challenge 1 draw a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

#Challenge 2 draw a dashed line
for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()






















Screen = Screen()
Screen.exitonclick()